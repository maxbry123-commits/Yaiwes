# HANDOFF — core kernel Yaiwes principal

Índice: [INDICE core kernel Yaiwes principal.md](./INDICE%20core%20kernel%20Yaiwes%20principal.md) · Índice maestro: [README-INDICE.md](./README-INDICE.md)

## Cómo se hizo
- Lista: t126u (110 repos: 107 con URL + Ponytail, Memanto, TimesFM verificados en GitHub).
- Descarga: motor_2 + engine (ENGINE_PATH explícito, DEST_REPO=maxbry123-commits/Yaiwes, DEST_ROOT=`Yaiwes core/core kernel Yaiwes principal`), 5 colas de ~9 + 1 reintento, 2 a la vez. Sin HF, sin LFS, sin Actions, sin force push.
- Movidos: 53 desde `componentes integrar` en un solo commit (renombrado de índice git, sin re-subir blobs).
- Ya presentes en shark imput (enlazados, no descargados): python-sdk, tree-sitter, ast-grep, zoekt, playwright, nats-server, LLMLingua.

## Reanudar / auditar
1. Cada `<slug>/` tiene `code/` + `DOWNLOAD_EXTRACT_MANIFEST.json`.
2. Recuento archivos `code/` = `extracted_tree.files`; si no cuadra, se conserva `_archives/` (fuente completa verificada por sha256).
3. Sin fallidos pendientes (ver cierre final).


---
## Cierre final 2026-10-15 (America/Bogota)
- 65 repos con árbol≠manifiesto: 3227 archivos faltantes recuperados desde `_archives` con motor_1 (CRC + tree hash = manifiesto) y `_archives` borrado. Causa: archivos ignorados por el `.gitignore` del propio repo al hacer `git add`.
- qdrant, autogen, agent-framework: importados sin LFS (punteros LFS quedan como punteros: 1, 51, 2). renovate: importado excluyendo solo `docs/usage/docker.md` (push protection).
- Forense upstream↔destino blob a blob en 152 repos: idénticos (198 archivos alineados con el blob upstream por normalización EOL). Excepciones: renovate (1 excluido) y MoDr (upstream vacío hoy).
- Sin `_archives`, sin duplicados, sin sueltos en `Yaiwes core/`.


---
## Cierre t130u (2026-10-15, America/Bogota) — solo motores canónicos
- Las 4 carpetas publicadas antes con git directo (qdrant, autogen, agent-framework, renovate) se borraron y se re-adquirieron por la ruta permitida: clon superficial local sin smudge LFS → quitar punteros LFS y reglas filter=lfs → ZIP → **motor_1** (CRC + tree hash) → **motor_3** (sha256 por archivo, COLLISION_POLICY=fail) → commit normal. El engine no tiene opción de excluir rutas (detecta LFS por la cabecera `version https://git-lfs.github.com/spec/v1` en archivos ≤1 KB y aborta).
- Igual ruta para los repos con reglas filter=lfs: weaviate, PWABuilder, dgm, memanto, temporal, timesfm; y para IsaacSim (1099 punteros) e IsaacLab (372 punteros), que el engine rechazó.
- renovate: `docs/usage/docker.md` excluido solo por GitHub push protection (credencial de ejemplo Google Cloud Service Account, línea 409); no es LFS.
- Lista 2: 10 repos con **motor_2 + engine** (2 colas, 2 a la vez) y completados desde sus `_archives` con motor_1 + motor_3 (el engine hace `git add` sin `-f` y pierde archivos ignorados por el .gitignore del repo). Genesis = Genesis-Embodied-AI/genesis-world. claude-skills completo (el engine no admite subcarpetas). Sin pesos HF. Gemini Computer Use: solo nota.
- shark imput (18) y memoria (1): `_archives` extraídos con motor_1, verificados contra su manifiesto, copiados con motor_3 y luego borrados.

### Auditorías de cumplimiento (4 pasadas independientes, HEAD de contenido 368e1b77d8de3e6cfacb782ca5bbd2ca2781dbf7)
1. **Reglas de transporte/historia:** compare 3ac08fc53…368e1b77 = ahead 52, behind 0 (solo fast-forward, sin force push); sin `.github`/Actions; sin HF; secretos en docs: 0 coincidencias. PASS.
2. **LFS en todo Yaiwes (shark imput, memoria, Yaiwes core y resto):** 654.122 entradas; 175.091 blobs ≤1 KB leídos + 12 `.gitattributes` grandes → 0 punteros LFS, 0 líneas filter=lfs. PASS.
3. **Completitud (forense blob a blob vs árbol upstream del commit fuente):** 164/164 repos de Yaiwes core idénticos salvo lo anotado (punteros/reglas LFS, renovate docker.md, symlinks); elasticsearch verificado con árbol completo (API truncada); MoDr: upstream hoy vacío, se conserva copia (95 archivos). Repos nuevos/cambiados (41, incl. shark/memoria): 41/41. PASS con esas notas.
4. **Higiene y formato:** 0 `_archives` en todo el repo; 0 duplicados entre carpetas; 0 sueltos en `Yaiwes core/` salvo el README principal; 115 carpetas en core kernel (103 + 12) y 49 en componentes; README principal: 122 entradas, todas con Nombre · URL visible · Micro resumen · LOOP (63 con el LOOP de Antonio del formato 115 y 12 con el de la lista 2). PASS.

### Desviación histórica registrada
- Commits anteriores al cierre t130u (lotes 1–9 de recuperación, 7724e1ecd y las 4 importaciones ya revertidas) escribieron en el índice git directamente (contenido verificado, pero no colocado con motor_3). El contenido actual es idéntico al upstream; esos commits quedan en el historial (sin force push no se pueden reescribir).
