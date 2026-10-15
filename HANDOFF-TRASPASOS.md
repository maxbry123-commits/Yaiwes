# HANDOFF TRASPASOS — cableado (Yaiwes)

Handoff de reanudación y auditoría de los traspasos T1/T2/T3.  
Índice vivo: [README-INDICE-TRASPASOS.md](./README-INDICE-TRASPASOS.md)  
Zona horaria del usuario: America/Bogota (UTC-5).

---

## 1. Qué está cableado

| Tarea | Origen | Destino repo | Rutas destino |
|---|---|---|---|
| T1 | https://github.com/maxbry123-commits/frontend | https://github.com/maxbry123-commits/ui-yaiwes | `UI YAIWES/`, `UI YAIWES interface/` |
| T2 | https://github.com/maxbry123-commits/frontend/tree/eff1bfe0ab5b47ed1f70506b2c49cca6fd6f0ecb | https://github.com/maxbry123-commits/yaiwes-factory-ui | `fabrica de UI INTERFACE fromtend/`, `T-3000 MOTOR AUTOEVOLUTION 👾/00-ENTRADA/` |
| T3 | https://github.com/maxbry123-commits/osquestador-auditor | https://github.com/maxbry123-commits/Yaiwes | `shark imput/{imput shark core, componentes por integrar}/`, `memoria/{osquestador auditor memoria core, componentes por integrar}/` |

Motores (solo estos):

- Raíz: https://github.com/maxbry123-commits/router-universal-router-inteligente-/tree/main/Motores%20descarga%20extracci%C3%B3n%20b%C3%BAsquedas/%E2%9E%A1%EF%B8%8F%F0%9F%93%82motores%20de%20descarga%20extracci%C3%B3n%20copiado%20movimiento%20archivos%20router-universal-router-inteligente-
- Skill: https://github.com/maxbry123-commits/router-universal-router-inteligente-/blob/main/Motores%20descarga%20extracci%C3%B3n%20b%C3%BAsquedas/%E2%9E%A1%EF%B8%8F%F0%9F%93%82motores%20de%20descarga%20extracci%C3%B3n%20copiado%20movimiento%20archivos%20router-universal-router-inteligente-/%E2%9E%A1%EF%B8%8F%F0%9F%93%82%20skills%20descargar%20extraer%20zip%20copiar%20mover%20archivos%20readme.md
- En uso: **motor_3** (copia por lotes). **motor_1** solo para ZIP sin carpeta extraída. No HF, no LFS, no Actions. No force-push.

Clasificación T3 (v3): shark ~40 comp. (~1,9 GB); memoria ~13 comp. (~1,07 GB); descarte 144 (~11,9 GB). Detalle en box: `/workspace/migra-plan/CLASIFICACION-FINAL.md` + `valor.json`.

---

## 2. Segmentos y STATE_FILE (cómo reanudar)

Estado de trabajo en el box (fuera del árbol Git final): `/workspace/traspasos/state/`

| Seg | Destino | STATE_FILE sugerido | Estado índice |
|---|---|---|---|
| S1 | ui-yaiwes/`UI YAIWES` | `/workspace/traspasos/state/S1.json` | en curso |
| S2 | ui-yaiwes/`UI YAIWES interface` | `/workspace/traspasos/state/S2.json` | en curso |
| S3 | yaiwes-factory-ui/`fabrica de UI INTERFACE fromtend` | `/workspace/traspasos/state/S3.json` | en curso |
| S4 | yaiwes-factory-ui/`T-3000…/00-ENTRADA` | `/workspace/traspasos/state/S4.json` | en curso |
| S5 | Yaiwes/`shark imput/imput shark core` | `/workspace/traspasos/state/S5.json` | en curso |
| S6 | Yaiwes/`shark imput/componentes por integrar` | `/workspace/traspasos/state/S6.json` | en curso |
| S7 | Yaiwes/`memoria/osquestador auditor memoria core` | `/workspace/traspasos/state/S7.json` | en curso |
| S8 | Yaiwes/`memoria/componentes por integrar` | `/workspace/traspasos/state/S8.json` | en curso |

Reanudar un segmento:

1. Leer el JSON de `STATE_FILE` (completed / failed / pending).
2. Relanzar el **mismo** motor con las **mismas** variables absolutas (`SOURCE_DIR`, `DEST_DIR`, `STATE_FILE`, `BATCH_SIZE`, `COLLISION_POLICY=fail`).
3. No crear un STATE_FILE nuevo a medias: uno por segmento, reutilizable.
4. Tras cada lote publicado: `git fetch` + rebase (nunca force); read-back de main.
5. Un agente por segmento; revisión cada ~30 min.

Ejemplo invocación (rutas de ejemplo — sustituir por absolutas reales):

```bash
SOURCE_DIR=… DEST_DIR=… STATE_FILE=/workspace/traspasos/state/S5.json \
BATCH_SIZE=25 COLLISION_POLICY=fail \
python3 motor_3_copy_batches.py
```

Éxito motor: una línea JSON con `verdict=VERIFIED_CLOSED`, `failed=0`, `pending=0`.

---

## 3. Cómo auditar (checklist)

Antes de marcar un segmento PASS (GUIA checklist 1–10):

1. Blob SHA del motor = skill (`git hash-object`); no editar motores.
2. Ninguna llamada HF, `git lfs`, ni workflow en la tarea.
3. Todas las rutas absolutas y no vacías (vacío = CWD → peligro).
4. Destinos dados por el usuario; sin defaults heredados del skill.
5. STATE_FILE / evidencias **fuera** del árbol final del destino.
6. Guardar JSON de salida del motor como evidencia.
7. `COLLISION_POLICY=fail`.
8. Push sin force; commit SHA; read-back de main (lista + hashes) coincide.
9. Sin `.partial` / `.moving` / `.tmp` en destino.
10. Recuento destino = manifiesto; solo entonces `100% PASS`.

Por destino, el agente debe escribir/actualizar `README TRASPASOS.md` (origen@sha, destino, manifiestos, commits, verdict, read-back). Enlaces (pueden estar **pendientes** hasta que el segmento los cree):

- https://github.com/maxbry123-commits/ui-yaiwes/blob/main/README%20TRASPASOS.md — **pendiente**
- https://github.com/maxbry123-commits/yaiwes-factory-ui/blob/main/README%20TRASPASOS.md — **pendiente**
- https://github.com/maxbry123-commits/Yaiwes/blob/main/shark%20imput/README%20TRASPASOS.md — **pendiente**
- https://github.com/maxbry123-commits/Yaiwes/blob/main/memoria/README%20TRASPASOS.md — **pendiente**

---

## 4. Concurrencia en Yaiwes

Otros agentes empujan a `Yaiwes` main a la vez. Reglas:

- Clone/sparse mínimo; tocar **solo** los archivos de esta tarea.
- Antes de push: `git fetch origin main` + `git rebase origin/main` (o pull --rebase).
- **Nunca** `git push --force`.
- Si hay conflicto en archivos ajenos: no resolver inventando; rebase solo de estos dos docs / del segmento propio.

---

## 5. Fuera de alcance hasta nuevo OK

- Borrar origen (frontend / osquestador-auditor) con motor_4 o `git rm`.
- Mover `.github/` o raíces de motores (ya presentes en destino → no hace falta).
- Publicar secretos (token GitHub, HF, passphrase): solo en entorno / `.secrets`, nunca en repo ni en estos markdown.

---

## 6. Enlaces fijos de este handoff

| Archivo | URL |
|---|---|
| Índice | https://github.com/maxbry123-commits/Yaiwes/blob/main/README-INDICE-TRASPASOS.md |
| Este handoff | https://github.com/maxbry123-commits/Yaiwes/blob/main/HANDOFF-TRASPASOS.md |
| Repo Yaiwes | https://github.com/maxbry123-commits/Yaiwes |
| ui-yaiwes | https://github.com/maxbry123-commits/ui-yaiwes |
| yaiwes-factory-ui | https://github.com/maxbry123-commits/yaiwes-factory-ui |
| frontend | https://github.com/maxbry123-commits/frontend |
| osquestador-auditor | https://github.com/maxbry123-commits/osquestador-auditor |
