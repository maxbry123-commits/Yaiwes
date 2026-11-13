#!/usr/bin/env python3
from __future__ import annotations
import hashlib, json, os, pathlib, random, shutil, subprocess, tempfile, time

SCHEMA = "yaiwes.frontend.move-batches.v1"
SOURCE_DIR = pathlib.Path(os.getenv("SOURCE_DIR", "")).expanduser()
DEST_DIR = pathlib.Path(os.getenv("DEST_DIR", "")).expanduser()
STATE_FILE = pathlib.Path(os.getenv("STATE_FILE", ".motor4-move-state.json")).expanduser()
BATCH_SIZE = int(os.getenv("BATCH_SIZE", "25"))
COLLISION_POLICY = os.getenv("COLLISION_POLICY", "fail").lower()
MAX_BATCHES = int(os.getenv("MAX_BATCHES", "0"))

# ================= MODE=git (2026-11-13, autorizado por el owner en el chat actual) =================
# Mueve rutas DENTRO de un repo de GitHub: hasta BATCH_SIZE rutas en UN solo commit + push normal (nunca force).
# No descarga el contenido de ningun archivo y no crea copia de trabajo: solo trae el indice de carpetas (blob:none, sin checkout).
# Mover = la ruta destino apunta al MISMO objeto git que tenia la ruta origen, y la ruta origen se quita.
# Sin LFS, sin GitHub Actions. La autenticacion la resuelve el entorno git (R4): este codigo no lee tokens.
# Entradas: MODE=git REPO=owner/repo BRANCH=<rama> MOVES_FILE=<json [{"src":"a/x","dst":"b/x"}, ...]>  (+ BATCH_SIZE, COLLISION_POLICY)
MODE = os.getenv("MODE", "disk").lower()
REPO = os.getenv("REPO", "").strip()
BRANCH = os.getenv("BRANCH", "").strip()
MOVES_FILE = os.getenv("MOVES_FILE", "").strip()
PUSH_ATTEMPTS = max(8, min(500, int(os.getenv("PUSH_ATTEMPTS", "30"))))


def git(args, cwd, check=True, lazy=False, data=None):
    # GIT_NO_LAZY_FETCH=1: si algun paso intentara bajar contenido de archivos, falla en vez de descargarlo. Solo fetch/push hablan con el remoto.
    e = dict(os.environ); e["GIT_TERMINAL_PROMPT"] = "0"
    if not lazy: e["GIT_NO_LAZY_FETCH"] = "1"
    p = subprocess.run(["git"] + args, cwd=cwd, env=e, input=data, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    out = p.stdout.decode("utf-8", "surrogateescape")
    if check and p.returncode: raise RuntimeError("COMMAND_FAILED:git " + args[0] + ":" + out[-1500:])
    return p.returncode, out


def entry(repo, rev, path):
    """(mode, type, sha) de una ruta en un commit, o None. No descarga contenido."""
    _, out = git(["ls-tree", "-z", rev, "--", path], repo)
    for rec in out.split("\0"):
        if "\t" in rec:
            meta, name = rec.split("\t", 1)
            if name == path:
                mode, typ, sha = meta.split(); return mode, typ, sha
    return None


def fetch_head(repo):
    for attempt in range(1, 7):
        rc, out = git(["-c", "http.lowSpeedLimit=1000", "-c", "http.lowSpeedTime=60", "fetch", "--depth=1", "--filter=blob:none", "origin", BRANCH], repo, check=False, lazy=True)
        if rc == 0: return git(["rev-parse", "FETCH_HEAD"], repo)[1].strip()
        time.sleep(min(10 * attempt, 60))
    raise RuntimeError("SOURCE_REF_GAP:" + out[-300:])


def git_mode():
    def stop(verdict, detail): raise SystemExit(json.dumps({"schema": SCHEMA, "mode": "git", "verdict": verdict, "detail": detail}, ensure_ascii=False))
    if not REPO or not BRANCH or not MOVES_FILE: stop("INPUT_GAP", "REPO, BRANCH y MOVES_FILE son obligatorios en MODE=git")
    moves = [(m["src"].strip("/"), m["dst"].strip("/")) for m in json.loads(pathlib.Path(MOVES_FILE).expanduser().read_text())]
    if not moves: stop("INPUT_GAP", "MOVES_FILE vacio")
    dsts = [d for _, d in moves]; srcs = [s for s, _ in moves]
    if len(set(dsts)) != len(dsts) or len(set(srcs)) != len(srcs): stop("INPUT_GAP", "src o dst repetido en MOVES_FILE")
    for s, d in moves:
        if not s or not d: stop("INPUT_GAP", "src/dst vacio")
        if s == d or d.startswith(s + "/"): stop("DEST_INSIDE_SOURCE_GAP", s)
        if s.startswith(d + "/"): stop("SOURCE_INSIDE_DEST_GAP", s)
    url = REPO if "://" in REPO else "https://github.com/" + REPO.removesuffix(".git") + ".git"
    results, errors, commits = {}, {}, []
    with tempfile.TemporaryDirectory(prefix="yaiwes-move-git-") as td:
        repo = td; git(["init", "-q"], repo); git(["remote", "add", "origin", url], repo)
        git(["config", "user.name", "yaiwes-move-engine"], repo); git(["config", "user.email", "yaiwes-move-engine@users.noreply.github.com"], repo)
        for start in range(0, len(moves), BATCH_SIZE):
            batch = moves[start:start + BATCH_SIZE]
            try:
                for attempt in range(1, PUSH_ATTEMPTS + 1):
                    head = fetch_head(repo); git(["read-tree", head], repo); plan = []; local = {}
                    for s, d in batch:
                        se, de = entry(repo, head, s), entry(repo, head, d)
                        if se is None:
                            if de is not None: local[s] = "VERIFIED_EXISTING_AFTER_MOVE"; continue
                            raise RuntimeError("SOURCE_MISSING_AND_DEST_UNVERIFIED:" + s)
                        if se[0] == "120000" or se[1] not in ("tree", "blob"): raise RuntimeError("SOURCE_SYMLINK_GAP:" + s)
                        if de is not None and de[2] != se[2]:
                            if COLLISION_POLICY == "skip": local[s] = "SKIPPED_COLLISION"; continue
                            if COLLISION_POLICY != "replace": raise RuntimeError("DESTINATION_COLLISION:" + d)
                        if de is not None: git(["rm", "-r", "-f", "-q", "--cached", "--", d], repo)
                        git(["rm", "-r", "-f", "-q", "--cached", "--", s], repo)
                        if se[1] == "tree":
                            # se reescriben solo las entradas del indice (ruta nueva -> mismo objeto); no se toca ni se baja ningun contenido
                            rows = [r for r in git(["ls-tree", "-r", "-z", se[2]], repo)[1].split("\0") if "\t" in r]
                            if not rows: raise RuntimeError("EMPTY_SOURCE_TREE:" + s)
                            info = "".join(f"{m.split()[0]} {m.split()[2]}\t{d}/{n}\0" for m, n in (r.split("\t", 1) for r in rows))
                            git(["update-index", "-z", "--index-info"], repo, data=info.encode("utf-8", "surrogateescape"))
                        else: git(["update-index", "--add", "--cacheinfo", f"{se[0]},{se[2]},{d}"], repo)
                        plan.append((s, d, se[2], "DEST_IDENTICAL_SOURCE_REMOVED" if de is not None and de[2] == se[2] else "MOVED_VERIFIED"))
                    if not plan: results.update(local); break
                    tree = git(["write-tree", "--missing-ok"], repo)[1].strip()
                    commit = git(["commit-tree", tree, "-p", head, "-m", f"move(motor_4): {len(plan)} rutas"], repo)[1].strip()
                    rc, out = git(["push", "origin", f"{commit}:refs/heads/{BRANCH}"], repo, check=False, lazy=True)
                    if rc == 0:
                        new = fetch_head(repo)  # read-back sobre lo publicado
                        for s, d, sha, status in plan:
                            got = entry(repo, new, d)
                            if got is None or got[2] != sha: raise RuntimeError("READBACK_HASH_MISMATCH:" + d)
                            if entry(repo, new, s) is not None: raise RuntimeError("SOURCE_STILL_PRESENT:" + s)
                            local[s] = status
                        results.update(local); commits.append(commit); break
                    low = out.lower()
                    if any(k in low for k in ("rate limit", "secondary rate", "too many requests", "429")): time.sleep(min(120 * attempt, 600))
                    elif any(k in low for k in ("non-fast-forward", "fetch first", "[rejected]", "stale info", "remote rejected", "cannot lock ref")): time.sleep(min(2 * attempt, 10) + random.random())
                    else: raise RuntimeError("COMMAND_FAILED:git push:" + out[-1500:])
                else:
                    raise RuntimeError("PUBLISH_RATE_LIMIT_GAP")
            except RuntimeError as e:
                for s, _ in batch:
                    if s not in results: errors[s] = str(e)
                if COLLISION_POLICY == "fail": break
    total = len(moves); done = len(results)
    print(json.dumps({"schema": SCHEMA, "mode": "git", "repo": REPO, "branch": BRANCH, "batch_size": BATCH_SIZE, "collision_policy": COLLISION_POLICY,
                      "total": total, "moved_or_verified": done, "failed": len(errors), "pending": total - done - len([s for s in errors if s not in results]),
                      "commits": commits, "results": results, "errors": errors, "content_downloaded": False,
                      "verdict": "VERIFIED_CLOSED" if done == total and not errors else "GAPS_PENDING"}, ensure_ascii=False, sort_keys=True))

# ================= MODE=disk (original, sin cambios) =================

def guard_roots():
    if not str(SOURCE_DIR) or not str(DEST_DIR):
        raise RuntimeError("SOURCE_DIR and DEST_DIR required")
    s = SOURCE_DIR.resolve(); d = DEST_DIR.resolve()
    if s == d or s in d.parents:
        raise RuntimeError("DEST_INSIDE_SOURCE_GAP")
    if d in s.parents:
        raise RuntimeError("SOURCE_INSIDE_DEST_GAP")


def sha256_file(p: pathlib.Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()


def first_manifest():
    if not SOURCE_DIR.is_dir():
        raise RuntimeError("SOURCE_DIR_NOT_FOUND")
    rows = []
    for p in sorted((x for x in SOURCE_DIR.rglob("*") if x.is_file()), key=lambda x: x.relative_to(SOURCE_DIR).as_posix()):
        if p.is_symlink():
            raise RuntimeError("SOURCE_SYMLINK_GAP:" + p.relative_to(SOURCE_DIR).as_posix())
        if p.resolve() == STATE_FILE.resolve():
            continue
        rows.append({"rel": p.relative_to(SOURCE_DIR).as_posix(), "bytes": p.stat().st_size, "sha256": sha256_file(p)})
    return rows


def load_state():
    files = first_manifest()
    fresh = {"schema": SCHEMA, "manifest": files, "completed": {}, "failed": {}, "batches": 0}
    if not STATE_FILE.exists():
        return fresh
    old = json.loads(STATE_FILE.read_text())
    by_rel = {r["rel"]: r for r in files}
    completed = {}
    for rel, status in old.get("completed", {}).items():
        row = by_rel.get(rel); dst = DEST_DIR / rel
        if row and dst.is_file() and sha256_file(dst) == row["sha256"]:
            completed[rel] = status
    fresh["completed"] = completed
    fresh["batches"] = old.get("batches", 0)
    return fresh


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    tmp = STATE_FILE.with_name(STATE_FILE.name + ".tmp")
    tmp.write_text(json.dumps(state, indent=2, sort_keys=True) + "\n")
    os.replace(tmp, STATE_FILE)


def move_verified(row):
    rel = pathlib.PurePosixPath(row["rel"]); src = SOURCE_DIR / rel; dst = DEST_DIR / rel
    dst.parent.mkdir(parents=True, exist_ok=True)
    if not src.exists():
        if dst.exists() and sha256_file(dst) == row["sha256"]:
            return "VERIFIED_EXISTING_AFTER_MOVE"
        raise RuntimeError("SOURCE_MISSING_AND_DEST_UNVERIFIED:" + row["rel"])
    if sha256_file(src) != row["sha256"]:
        raise RuntimeError("SOURCE_CHANGED:" + row["rel"])
    if dst.exists():
        dsha = sha256_file(dst)
        if dsha == row["sha256"]:
            src.unlink(); return "DEST_IDENTICAL_SOURCE_REMOVED"
        if COLLISION_POLICY == "skip":
            return "SKIPPED_COLLISION"
        if COLLISION_POLICY != "replace":
            raise RuntimeError("DESTINATION_COLLISION:" + row["rel"])
    tmp = dst.with_name(dst.name + ".moving")
    if tmp.exists(): tmp.unlink()
    shutil.move(str(src), str(tmp))
    if sha256_file(tmp) != row["sha256"]:
        if not src.exists(): shutil.move(str(tmp), str(src))
        raise RuntimeError("MOVE_HASH_MISMATCH:" + row["rel"])
    os.replace(tmp, dst)
    if sha256_file(dst) != row["sha256"]:
        raise RuntimeError("READBACK_HASH_MISMATCH:" + row["rel"])
    return "MOVED_VERIFIED"


def cleanup_empty_dirs():
    if not SOURCE_DIR.exists(): return
    for d in sorted((x for x in SOURCE_DIR.rglob("*") if x.is_dir()), key=lambda x: len(x.parts), reverse=True):
        try: d.rmdir()
        except OSError: pass


def main():
    if not 1 <= BATCH_SIZE <= 100:
        raise SystemExit(json.dumps({"schema": SCHEMA, "verdict": "INPUT_GAP", "detail": "BATCH_SIZE must be 1..100"}))
    if COLLISION_POLICY not in {"fail", "skip", "replace"}:
        raise SystemExit(json.dumps({"schema": SCHEMA, "verdict": "INPUT_GAP", "detail": "COLLISION_POLICY must be fail|skip|replace"}))
    if MODE == "git":
        return git_mode()
    if MODE != "disk":
        raise SystemExit(json.dumps({"schema": SCHEMA, "verdict": "INPUT_GAP", "detail": "MODE must be git|disk"}))
    try:
        guard_roots()
    except RuntimeError as e:
        raise SystemExit(json.dumps({"schema": SCHEMA, "verdict": "INPUT_GAP", "detail": str(e)}))
    state = load_state(); completed = state.setdefault("completed", {}); batches = 0
    while True:
        pending = [r for r in state["manifest"] if r["rel"] not in completed]
        if not pending or (MAX_BATCHES and batches >= MAX_BATCHES): break
        for row in pending[:BATCH_SIZE]:
            try:
                status = move_verified(row); completed[row["rel"]] = status; state.setdefault("failed", {}).pop(row["rel"], None)
            except Exception as e:
                state.setdefault("failed", {})[row["rel"]] = str(e)
        batches += 1; state["batches"] = state.get("batches", 0) + 1; save_state(state)
        if state.get("failed") and COLLISION_POLICY == "fail": break
    cleanup_empty_dirs()
    total = len(state["manifest"]); done = len(completed); failed = len(state.get("failed", {})); pending_count = total - done
    source_remaining = sum(1 for p in SOURCE_DIR.rglob("*") if p.is_file()) if SOURCE_DIR.exists() else 0
    result = {
        "schema": SCHEMA, "batch_size": BATCH_SIZE, "collision_policy": COLLISION_POLICY,
        "total": total, "moved_or_verified": done, "failed": failed, "pending": pending_count,
        "source_files_remaining": source_remaining, "batches_total": state.get("batches", 0),
        "state_file": str(STATE_FILE), "verdict": "VERIFIED_CLOSED" if pending_count == 0 and failed == 0 else "GAPS_PENDING"
    }
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))

if __name__ == "__main__": main()
