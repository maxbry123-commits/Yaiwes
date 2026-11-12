# ÍNDICE — shark imput

Handoff: [HANDOFF shark imput.md](./HANDOFF%20shark%20imput.md) · Índice maestro: [README-INDICE.md](./README-INDICE.md)

Carpeta: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput

---

## Registro de traspaso (antes `README TRASPASOS.md`) — shark imput (T3-shark)

Fecha: 2026-10-15 ~00:30 COT. Autorizado por Antonio (t107u "Arranca").
Origen: `maxbry123-commits/osquestador-auditor@main` = `89a14a2158f6b963b0ca667c1771af6666146c42` (origen NO modificado, nada borrado).
Destino: `maxbry123-commits/Yaiwes@main` / `shark imput/`.
Motor: `motor_3_copy_batches.py` (router-universal-router-inteligente-, blob `3689924361ce…` = SKILL). COLLISION_POLICY=fail, rutas absolutas, STATE_FILE fuera de origen/destino. Sin HF, sin LFS, sin Actions, sin force push.

## Segmentos
| Seg | Destino | Archivos | Motor | Verdict | sha256 del manifiesto (sha256sum ordenado) |
|---|---|---|---|---|---|
| core | `imput shark core/` | 74 | 1 corrida (3 lotes de 25) | VERIFIED_CLOSED failed=0 pending=0 | `c9b69393579fb30e258dab32901e2be347b9041fb8f93740c0555a5b02b3aa4d` |
| componentes | `componentes por integrar/` | 51661 | 1 corrida (517 lotes de 100) | VERIFIED_CLOSED failed=0 pending=0 | `3ae295d7fa16ad6ca331b3e4be88580d421f0b7ddfd5e591b655f58177abf036` |

Commits: lote 1/2 `738a9cc84d393fcb2ed687aa326998206a09e230` (core + 35 componentes, 27.309 arch); lote 2/2 `1ca98c63a43ab17bcd3dc6c721d98de1abca9615` (FlagEmbedding, prefect, unstructured, trafilatura, duckdb; 24.426 arch). Ambos con fetch+rebase, push normal.

## imput shark core (74 archivos)
- `📂 component acquisition`, `📂 root-only-runtime`, `📂 sharck-v3-parallel-candidate` ← `➡️📂 sharck imput/📂 input sharck code principal/` (sin `📂 componentes open source`).
- `➡️📂 shart imput code Run` ← `➡️📂 Shack imput/`.
- `📁 readme arquitectura sharck imput V2.1.md` ← `➡️📂 sharck imput/` (único readme conservado, t104u).
- No copiado: resto de readmes/handoffs/recovery sueltos y `HF-BRIDGE-DESIGN.md` (basura según t104u / atado a HF), `📂 Craxy wall bitácora stated JSON` (logs/estado de corridas), `📂 workflows reubicados` (GitHub Actions, prohibido), `📂 motores caso` y `📂 motores canónicos copiados` (motores; los canónicos ya están en la raíz de Yaiwes).

## componentes por integrar (40)
| Componente | Origen | Archivos | MB |
|---|---|---|---|
| anthropic-skills | `➡️📂 Shack imput/📂 Componentes para integración sharck imput/skills/anthropic-skills` | 421 | 16 |
| argos-translate | `argos-translate` | 81 | 4 |
| ast-grep | `ast-grep` | 318 | 4 |
| bm25s | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B07-query-search-primitives/bm25s` | 92 | 9 |
| chonkie | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B04-context-engineering/chonkie` | 356 | 25 |
| crawl4ai | `crawl4ai` | 900 | 30 |
| datasketch | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B02-ir-evidence/datasketch` | 126 | 5 |
| duckdb | `duckdb` | 15412 | 271 |
| fastembed | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B07-query-search-primitives/fastembed` | 131 | 3 |
| FlagEmbedding | `➡️📂 Shack imput/📂 Componentes para integración sharck imput/rag/FlagEmbedding` | 1156 | 95 |
| guardrails | `guardrails` | 562 | 17 |
| huggingface-skills | `➡️📂 Shack imput/📂 Componentes para integración sharck imput/skills/huggingface-skills` | 205 | 4 |
| khoj | `khoj` | 704 | 84 |
| LLMLingua | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B04-context-engineering/LLMLingua` | 76 | 9 |
| mcp-registry | `➡️📂 Shack imput/📂 Componentes para integración sharck imput/skills/mcp-registry` | 258 | 56 |
| nats-server | `nats-server` | 498 | 15 |
| open-codebase-index | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B03-code-runtime/open-codebase-index` | 439 | 7 |
| openai-skills | `➡️📂 Shack imput/📂 Componentes para integración sharck imput/skills/openai-skills` | 785 | 9 |
| Perplexica | `Perplexica` | 238 | 37 |
| phoenix | `phoenix` | 7251 | 78 |
| playwright | `playwright` | 3081 | 74 |
| playwright-mcp | `➡️📂 Shack imput/📂 Componentes para integración sharck imput/search/playwright-mcp` | 37 | 1 |
| prefect | → movido a core kernel (duplicado borrado t131u): https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/prefect | — | — |
| pydantic | `pydantic` | 824 | 13 |
| python-sdk | `python-sdk` | 1660 | 19 |
| ragas | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B04-context-engineering/ragas` | 699 | 91 |
| ranx | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B10-retrieval-eval/ranx` | 182 | 36 |
| RapidFuzz | `RapidFuzz` | 193 | 3 |
| repomix | `repomix` | 1187 | 13 |
| searxng | `searxng` | 993 | 23 |
| servers | `servers` | 152 | 2 |
| spaCy | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B04-context-engineering/spaCy` | 1776 | 36 |
| tesseract | `tesseract` | 730 | 10 |
| trafilatura | `➡️📂 sharck imput/📂 input sharck code principal/📂 componentes open source/B01-web-research/trafilatura` | 1173 | 179 |
| tree-sitter | `tree-sitter` | 616 | 7 |
| unstructured | `unstructured` | 1328 | 176 |
| whisperX | `whisperX` | 36 | 18 |
| youtube-transcript-api | `➡️📂 Shack imput/📂 Componentes para integración sharck imput/media-input-router/youtube-transcript-api` | 42 | 3 |
| yt-dlp | `yt-dlp` | 1239 | 15 |
| zoekt | `➡️📂 Shack imput/📂 Componentes para integración sharck imput/code/zoekt` | 347 | 6 |

## Decisiones
- B01-web-research y B02-ir-evidence re-listados completos con clon parcial (sparse): B01 = MinerU, heritrix3, nutch, scira, scrapy, trafilatura, yacy_search_server (sin nuevos); B02 = OpenSearch, RapidFuzz, datasketch, lucene, pyserini, pyterrier, rdflib + **tantivy (nuevo)**. Conservados: trafilatura, datasketch. tantivy → DESCARTE (motor de búsqueda full-text en Rust, redundante con bm25s; misma regla que lucene/OpenSearch). Resto según valor.json v3.
- ZIP: 48 ZIP `<proyecto>_NNNN.zip` (439 MB) en la raíz de 21 componentes son el paquete de descarga del código ya extraído → DESCARTE por duplicado. Comprobado: 30.011 entradas, 29.830 ya presentes extraídas; 181 no presentes (nats-server 107, duckdb 41, crawl4ai 16, otros ≤3; mayormente fixtures/binarios y archivos que el .gitignore del proyecto excluía). Siguen en el origen. ZIP de proyectos no extraídos en shark: ninguno (bm25s_0001/ytmusicapi_0001 descartados en v3) → motor_1 no se ejecutó.
- ZIP internos del propio proyecto (p.ej. playwright/tests/assets, unstructured/example-docs) se conservan como parte del código.
- Nombres de destino planos (`componentes por integrar/<proyecto>`); sin colisiones de nombre.
- `git add -f` para no perder archivos que los .gitignore anidados excluirían.

## Autoauditoría
- Recuento read-back de `origin/main`: core 74/74, componentes 51.661/51.661, 40 carpetas.
- sha256 completo origen(staging)↔destino(worktree): idénticos. Muestra aleatoria de 60 blobs leídos de `origin/main`: 0 diferencias.
- Sin `.partial`, sin symlinks, ningún archivo >95 MB.
- Estado: **VERIFIED_CLOSED**.
