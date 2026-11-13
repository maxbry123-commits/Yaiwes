#!/usr/bin/env python3
from __future__ import annotations
import concurrent.futures, json, os, pathlib, shutil, subprocess, sys, tempfile, threading, time

SCHEMA = "yaiwes.frontend.download-extract-queue.v1"
QUEUE_FILE = pathlib.Path(os.getenv("QUEUE_FILE", "queue.json")).expanduser()
STATE_FILE = pathlib.Path(os.getenv("STATE_FILE", ".motor2-queue-state.json")).expanduser()
ENGINE_PATH = pathlib.Path(os.getenv("ENGINE_PATH", str(pathlib.Path(__file__).resolve().parent / "download_extract_engine.py"))).expanduser()
INDEX_PATH_RAW = os.getenv("INDEX_PATH", "").strip()
INDEX_PATH = pathlib.Path(INDEX_PATH_RAW).expanduser() if INDEX_PATH_RAW else None
MAX_RETRIES = int(os.getenv("MAX_RETRIES", "3"))
LOOP_SLEEP_SECONDS = float(os.getenv("LOOP_SLEEP_SECONDS", "0"))
ITEM_DELAY_SECONDS = float(os.getenv("ITEM_DELAY_SECONDS", "2"))
RATE_LIMIT_COOLDOWN_SECONDS = float(os.getenv("RATE_LIMIT_COOLDOWN_SECONDS", "120"))
MAX_ITEMS_PER_RUN = int(os.getenv("MAX_ITEMS_PER_RUN", "0"))
# 2026-11-13 (owner): WORKERS = cuantos items de la cola se procesan A LA VEZ dentro de este mismo motor (1 = modo secuencial de siempre).
# Con WORKERS>1 el engine recibe LOCK_DIR (junto al STATE_FILE, fuera de las raices): carril unico de push por destino + NET_SLOTS.
# MIN_FREE_GIB = espacio libre minimo en la carpeta temporal antes de arrancar un item (espera; agotada la espera: INSUFFICIENT_SPACE_GAP).
WORKERS = max(1, min(100, int(os.getenv("WORKERS", "1"))))
MIN_FREE_GIB = float(os.getenv("MIN_FREE_GIB", "2"))
SPACE_WAIT_SECONDS = float(os.getenv("SPACE_WAIT_SECONDS", "1800"))
STATE_LOCK = threading.Lock()


def load_queue():
    data = json.loads(QUEUE_FILE.read_text())
    if isinstance(data, dict): data = data.get("queue", [])
    if not isinstance(data, list): raise RuntimeError("QUEUE_FORMAT_INVALID")
    out = []
    for i, row in enumerate(data):
        if not isinstance(row, dict) or not row.get("source_repo"):
            raise RuntimeError(f"QUEUE_ITEM_INVALID:{i}")
        item = dict(row); item.setdefault("source_ref", "HEAD"); item.setdefault("slug", item["source_repo"].rstrip("/").removesuffix(".git").split("/")[-1]); item.setdefault("publish", False)
        item["id"] = item.get("id") or f"{i+1:04d}:{item['slug']}"
        out.append(item)
    return out


def load_state(queue):
    if STATE_FILE.exists(): return json.loads(STATE_FILE.read_text())
    return {"schema": SCHEMA, "created_at": int(time.time()), "items": {x["id"]: {"status": "PENDING", "attempts": 0, "slug": x["slug"], "source_repo": x["source_repo"]} for x in queue}}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_name(STATE_FILE.name + ".tmp")
    tmp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, STATE_FILE)


def run_item(item):
    env = dict(os.environ)
    env.update({
        "SOURCE_REPO": item["source_repo"], "SOURCE_REF": str(item.get("source_ref", "HEAD")), "SLUG": item["slug"],
        "DEST_REPO": item.get("dest_repo", env.get("DEST_REPO", "")),
        "DEST_BRANCH": item.get("dest_branch", env.get("DEST_BRANCH", "main")),
        "DEST_ROOT": item.get("dest_root", env.get("DEST_ROOT", "")),
        "PUBLISH": "1" if item.get("publish") else "0",
        # 2026-11-13 (owner): rutas por item (lista o texto); vacio = repo completo
        "SOURCE_PATHS": "\n".join(item["source_paths"]) if isinstance(item.get("source_paths"), list) else str(item.get("source_paths", env.get("SOURCE_PATHS", ""))),
        "SOURCE_PATHS_FILE": str(item.get("source_paths_file", env.get("SOURCE_PATHS_FILE", ""))),
    })
    p = subprocess.run([sys.executable, str(ENGINE_PATH)], env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    lines = [x.strip() for x in p.stdout.splitlines() if x.strip()]
    payload = None
    for line in reversed(lines):
        try:
            obj = json.loads(line)
            if isinstance(obj, dict): payload = obj; break
        except json.JSONDecodeError: pass
    if p.returncode != 0 or not payload:
        raise RuntimeError((p.stdout or "ENGINE_NO_JSON_OUTPUT")[-3000:])
    if payload.get("verdict") != "VERIFIED_CLOSED":
        raise RuntimeError("ENGINE_NOT_CLOSED:" + json.dumps(payload, ensure_ascii=False)[-2000:])
    return payload


def wait_space():
    deadline = time.time() + SPACE_WAIT_SECONDS
    while shutil.disk_usage(tempfile.gettempdir()).free < MIN_FREE_GIB * 1024 ** 3:
        if time.time() > deadline: raise RuntimeError("INSUFFICIENT_SPACE_GAP")
        time.sleep(5)


def run_parallel(by_id, state):
    """Mismo ciclo de vida por item que el modo secuencial, pero WORKERS items a la vez. El estado se guarda bajo candado."""
    os.environ.setdefault("LOCK_DIR", str(STATE_FILE.resolve().parent / ".motor-locks"))
    # carpeta temporal propia de este motor (junto a su STATE_FILE): lo que dejo una corrida cortada se limpia al arrancar y no llena el disco
    tmp = STATE_FILE.resolve().parent / (".motor-tmp-" + STATE_FILE.name)
    shutil.rmtree(tmp, ignore_errors=True); tmp.mkdir(parents=True, exist_ok=True)
    os.environ["TMPDIR"] = str(tmp); tempfile.tempdir = str(tmp)
    todo = [(i, x) for i, x in by_id.items()]
    with STATE_LOCK:
        for item_id, item in todo:
            state["items"].setdefault(item_id, {"status": "PENDING", "attempts": 0, "slug": item["slug"], "source_repo": item["source_repo"]})
    todo = [(i, x) for i, x in todo if state["items"][i].get("status") != "VERIFIED_CLOSED" and state["items"][i].get("attempts", 0) < MAX_RETRIES]
    if MAX_ITEMS_PER_RUN: todo = todo[:MAX_ITEMS_PER_RUN]

    def work(pair):
        item_id, item = pair; row = state["items"][item_id]
        while True:
            with STATE_LOCK:
                if row.get("status") == "VERIFIED_CLOSED" or row.get("attempts", 0) >= MAX_RETRIES: return
                row["attempts"] = row.get("attempts", 0) + 1; row["status"] = "RUNNING"; save_state(state)
            pause = ITEM_DELAY_SECONDS
            try:
                wait_space(); result = run_item(item)
                with STATE_LOCK: row["result"] = result; row["status"] = "VERIFIED_CLOSED"; row.pop("error", None)
            except Exception as e:
                err = str(e).lower()
                with STATE_LOCK: row["error"] = str(e); row["status"] = "FAILED" if row["attempts"] >= MAX_RETRIES else "RETRY_PENDING"
                if any(k in err for k in ("rate_limit", "rate limit", "secondary rate", "429")): pause = RATE_LIMIT_COOLDOWN_SECONDS
                elif row["status"] == "RETRY_PENDING": pause = min(5 * row["attempts"], 60)
            with STATE_LOCK: save_state(state); write_index(state)
            if row["status"] in ("VERIFIED_CLOSED", "FAILED"): return
            time.sleep(pause)

    with concurrent.futures.ThreadPoolExecutor(max_workers=WORKERS) as pool:
        list(pool.map(work, todo))


def balance(state):
    rows = list(state["items"].values()); total = len(rows)
    success = [r for r in rows if r.get("status") == "VERIFIED_CLOSED"]
    download_ok = sum(1 for r in success if r.get("result", {}).get("source_commit"))
    extract_ok = sum(1 for r in success if r.get("result", {}).get("extraction_verified") is True)
    publish_ok = sum(1 for r in success if r.get("result", {}).get("publish", {}).get("verdict") == "PUBLISHED_AND_EXTRACTED_READBACK_VERIFIED")
    failed = sum(1 for r in rows if r.get("status") == "FAILED")
    pending = total - len(success) - failed
    return {"total": total, "download_verified": download_ok, "extraction_verified": extract_ok, "published_readback_verified": publish_ok, "failed": failed, "pending": pending}


def write_index(state):
    if INDEX_PATH is None:
        return
    rows = []
    for item_id, row in sorted(state["items"].items()):
        result = row.get("result", {}); repo = row.get("source_repo", ""); slug = row.get("slug", item_id)
        source_url = repo if repo.startswith("http") else ("https://github.com/" + repo if repo else "")
        rows.append((slug, source_url, row.get("status", "PENDING"), result.get("source_commit", "")))
    text = ["# Índice de componentes open source", "", "Generado automáticamente por Motor 2 — cola descarga + extracción persistente.", "", "| Componente | Repositorio fuente | Estado | Commit fuente |", "|---|---|---|---|"]
    for slug, url, status, commit in rows:
        link = f"[{url}]({url})" if url else "—"; text.append(f"| {slug} | {link} | {status} | `{commit}` |")
    text += ["", "## Balance", "", "```json", json.dumps(balance(state), indent=2, sort_keys=True), "```", ""]
    INDEX_PATH.parent.mkdir(parents=True, exist_ok=True); INDEX_PATH.write_text("\n".join(text))


def main():
    if not QUEUE_FILE.exists() or not ENGINE_PATH.exists():
        raise SystemExit(json.dumps({"schema": SCHEMA, "verdict": "INPUT_GAP", "detail": "QUEUE_FILE or ENGINE_PATH missing"}))
    queue = load_queue(); state = load_state(queue); by_id = {x["id"]: x for x in queue}
    processed = 0
    progress = WORKERS == 1
    if WORKERS > 1: run_parallel(by_id, state)
    while progress:
        progress = False
        for item_id, item in by_id.items():
            row = state["items"].setdefault(item_id, {"status": "PENDING", "attempts": 0, "slug": item["slug"], "source_repo": item["source_repo"]})
            if row.get("status") == "VERIFIED_CLOSED" or row.get("attempts", 0) >= MAX_RETRIES: continue
            if row.get("cooldown_until", 0) > time.time(): continue
            progress = True; row["attempts"] = row.get("attempts", 0) + 1; row["status"] = "RUNNING"; save_state(state)
            try:
                result = run_item(item); row["result"] = result; row["status"] = "VERIFIED_CLOSED"; row.pop("error", None)
            except Exception as e:
                row["error"] = str(e); row["status"] = "FAILED" if row["attempts"] >= MAX_RETRIES else "RETRY_PENDING"
                err = str(e).lower()
                if any(k in err for k in ("rate_limit", "rate limit", "secondary rate", "429")):
                    row["cooldown_until"] = int(time.time() + RATE_LIMIT_COOLDOWN_SECONDS)
                    time.sleep(RATE_LIMIT_COOLDOWN_SECONDS)
                elif row["status"] == "RETRY_PENDING":
                    time.sleep(min(5 * row["attempts"], 60))
            save_state(state); write_index(state)
            processed += 1
            if MAX_ITEMS_PER_RUN and processed >= MAX_ITEMS_PER_RUN: progress = False; break
            time.sleep(ITEM_DELAY_SECONDS + LOOP_SLEEP_SECONDS)
    b = balance(state); write_index(state)
    verdict = "VERIFIED_CLOSED" if b["pending"] == 0 and b["failed"] == 0 else "GAPS_PENDING"
    print(json.dumps({"schema": SCHEMA, "balance": b, "state_file": str(STATE_FILE), "index_path": str(INDEX_PATH) if INDEX_PATH else "", "verdict": verdict}, ensure_ascii=False, sort_keys=True))

if __name__ == "__main__": main()
