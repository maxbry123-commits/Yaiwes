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
