# README TRASPASOS — memoria (T3)

- **Qué:** componentes de memoria y almacenamiento conservados (clasificación v3, `valor.json`) + núcleo propio de memoria del orquestador.
- **Desde:** `maxbry123-commits/osquestador-auditor` @ `89a14a2158f6b963b0ca667c1771af6666146c42` (main). Origen NO modificado ni borrado.
- **Hacia:** `maxbry123-commits/Yaiwes` main → `memoria/`.
- **Motor:** `motor_3_copy_batches.py` (blob `3689924361ce…`, = SKILL), rutas absolutas, `COLLISION_POLICY=fail`, `BATCH_SIZE=100`, STATE_FILE nuevo por segmento fuera de origen/destino. Sin HF, sin LFS, sin Actions.

| Segmento | Destino | Archivos | Lotes motor | Verdict | sha256 manifiesto (sha256sum ordenado) |
|---|---|---|---|---|---|
| S7 | `osquestador auditor memoria core/` | 57 | 1 | VERIFIED_CLOSED failed=0 pending=0 | `93a34e284589ba6631168f82fbdda0e416949fd04a865a514a5307e17599153d` |
| S8 | `componentes por integrar/` | 22,269 | 223 | VERIFIED_CLOSED failed=0 pending=0 | `c862f79362ee66e5797d1a12a1dee764975ef43e954ae35b4ba6249e3b3333f1` |

**S7 core (17 elementos + 1 json):** Agente motores…, DOCUMENTOS-MAXBRY, Desplegar…, Documentos proyectos…, IMPORTED_CODE, MEMORY_STACK.md, Método de trabajo…, Notas de trabajo grock gpt…, PIPELINE osquestador auditor memoria, PIPELINE-osquestador-auditor-memoria, ROUTER_HF_MEMORY_WIRING.md, Refactoria…, Skills de trabajos…, conectividad con Router inteligente universal, la coneccion de todos los repos con el almacenamiento de huggueface, skills agente…, ➡️📂 readme arquitectura…, RDC_ADDITIONAL_COMPONENTS_EVIDENCE.json.

**S8 componentes (13):**
| Proyecto | Archivos | MB | sha256 (16) |
|---|---|---|---|
| FalkorDB | 659 | 13 | c714b973091320c3 |
| GraphRAG | 908 | 21 | aa86df38af32653c |
| Graphify | 878 | 24 | c281f89f073d34bf |
| MemOS | 1974 | 42 | 2487dd3ae20f8185 |
| faiss | 1091 | 15 | ecb1b7d5007fc67d |
| fastapi | 3141 | 60 | c150e9f8f61b8f24 |
| graphiti | 361 | 30 | b6b2b5082da48dc9 |
| litestream | 291 | 6 | 009c09effbfa5355 |
| llama_index | 9843 | 769 | fb0eb1d70cd30c12 |
| ollama | 1348 | 56 | 2025f0182a521cfd |
| python-diskcache | 82 | 2 | f3a718be1a21848f |
| restic | 1396 | 55 | 9b6961db91d79ac6 |
| sqlite-vec | 297 | 4 | 7c48ebf12f67361d |

**ZIP:** ningún ZIP conservado para memoria en v3 (aiomysql/asyncpg/docmost/qdrant descartados) → motor_1 no aplica.

**Commits:** lote 1 `084eab5dff` (core + 12 componentes), lote 2 `4e847276a7` (llama_index). Push normal con fetch+rebase, sin force.

**Autoauditoría:** sha256 de cada archivo origen = destino (S7 y S8 idénticos); 0 `.partial`/`.moving`; read-back main: 22,326 archivos en `memoria/` = 57 + 22,269; 0 symlinks, 0 archivos >95 MB, 0 punteros LFS; descartes no copiados. **Estado: 100% PASS ✅**
