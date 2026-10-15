# README ÍNDICE TRASPASOS — Yaiwes

Índice único de los traspasos en curso (2026-10-14, America/Bogota).  
Solo se usan los motores canónicos (motor_3 copia; motor_1 extracción ZIP si hace falta).  
**Prohibido:** Hugging Face, Git LFS, GitHub Actions.

Fuente de plan (box, no en este repo): `/workspace/migra-plan/` (`ORGANIZACION.md`, `CLASIFICACION-FINAL.md` v3, `valor.json`) y `/workspace/motores-review/GUIA.md`.

---

## 1. Motores (únicos permitidos)

| Uso | Motor | Notas |
|---|---|---|
| Copiar por lotes | `motor_3_copy_batches.py` | sha256 por archivo; `COLLISION_POLICY=fail`; STATE_FILE nuevo por segmento; rutas absolutas |
| Extraer ZIP ya publicados | `motor_1_extract_only.py` | CRC + tree hash; solo si quedan ZIP sin carpeta extraída |
| Borrar origen | `motor_4` / `git rm` | **Solo con OK explícito al final** — no arrancado |

- Carpeta canónica de motores:  
  https://github.com/maxbry123-commits/router-universal-router-inteligente-/tree/main/Motores%20descarga%20extracci%C3%B3n%20b%C3%BAsquedas/%E2%9E%A1%EF%B8%8F%F0%9F%93%82motores%20de%20descarga%20extracci%C3%B3n%20copiado%20movimiento%20archivos%20router-universal-router-inteligente-
- SKILL canónico (descargar / extraer ZIP / copiar / mover):  
  https://github.com/maxbry123-commits/router-universal-router-inteligente-/blob/main/Motores%20descarga%20extracci%C3%B3n%20b%C3%BAsquedas/%E2%9E%A1%EF%B8%8F%F0%9F%93%82motores%20de%20descarga%20extracci%C3%B3n%20copiado%20movimiento%20archivos%20router-universal-router-inteligente-/%E2%9E%A1%EF%B8%8F%F0%9F%93%82%20skills%20descargar%20extraer%20zip%20copiar%20mover%20archivos%20readme.md

Veredicto de método: **copiar con motor_3** (sparse del origen, push por lotes). El flujo ZIP del engine baja el repo entero y sube ~2×; no se usa para estas tareas.

---

## 2. Las 3 tareas

### Tarea 1 — frontend → ui-yaiwes (main)
| Seg | Origen | Destino | Motor | Estado |
|---|---|---|---|---|
| S1 | `maxbry123-commits/frontend` → `UI YAIWES/` | `ui-yaiwes` → `UI YAIWES/` | motor_3 | **en curso** |
| S2 | `maxbry123-commits/frontend` → `UI YAIWES interface/` | `ui-yaiwes` → `UI YAIWES interface/` | motor_3 | **en curso** |

### Tarea 2 — frontend@eff1bfe → yaiwes-factory-ui (main)
| Seg | Origen | Destino | Motor | Estado |
|---|---|---|---|---|
| S3 | `frontend@eff1bfe` → `fabrica de UI INTERFACE fromtend/` | `yaiwes-factory-ui` → mismo nombre | motor_3 | **en curso** |
| S4 | `frontend@eff1bfe` → `T-3000 MOTOR AUTOEVOLUTION 👾/00-ENTRADA/` | `yaiwes-factory-ui` → mismo path | motor_3 | **en curso** |

Origen raíz 1: https://github.com/maxbry123-commits/frontend/tree/eff1bfe0ab5b47ed1f70506b2c49cca6fd6f0ecb/fabrica%20de%20UI%20INTERFACE%20fromtend  
Origen raíz 2: https://github.com/maxbry123-commits/frontend/tree/eff1bfe0ab5b47ed1f70506b2c49cca6fd6f0ecb/T-3000%20MOTOR%20AUTOEVOLUTION%20%F0%9F%91%BE/00-ENTRADA

### Tarea 3 — osquestador-auditor → Yaiwes (main)
| Seg | Origen | Destino | Motor | Estado |
|---|---|---|---|---|
| S5 | OA → core shark (code principal sin OSS + code Run + docs; readme arquitectura V2.1) | `Yaiwes/shark imput/imput shark core/` | motor_3 | **en curso** |
| S6 | OA → componentes shark (lista blanca v3) | `Yaiwes/shark imput/componentes por integrar/` | motor_3 | **en curso** |
| S7 | OA → core memoria orquestador | `Yaiwes/memoria/osquestador auditor memoria core/` | motor_3 | **hecho** (084eab5) |
| S8 | OA → componentes memoria/almacenamiento (lista blanca v3) | `Yaiwes/memoria/componentes por integrar/` | motor_3 | **hecho** (4e84727; README 10d492b) |

Árbol destino T3:

```
Yaiwes/
├── shark imput/
│   ├── imput shark core/
│   ├── componentes por integrar/
│   └── README TRASPASOS.md          ← pendiente
├── memoria/
│   ├── osquestador auditor memoria core/
│   ├── componentes por integrar/
│   └── README TRASPASOS.md          ← hecho (10d492b)
├── README-INDICE-TRASPASOS.md       ← este archivo
└── HANDOFF-TRASPASOS.md
```

---

## 3. Reglas de clasificación (T3) — resumen v3

Criterio (Antonio):  
- **Shark imput:** entrada, búsqueda, clasificación de información.  
- **Memoria:** memoria y almacenamiento del orquestador.  
- **Descarte:** agentes genéricos, basura, repetidos, archivados, UI/fuentes sin rol, dependencias pip genéricas, servidores redundantes.

Totales v3 (`valor.json` + `CLASIFICACION-FINAL.md` v3):

| Destino | Elementos | Tamaño aprox |
|---|---|---|
| shark imput/componentes por integrar | 40 | ~1.900 MB |
| memoria/componentes por integrar | 13 | ~1.066 MB |
| memoria core (+ evidencias propias) | core | &lt;1 MB |
| **DESCARTE** | 144 | ~11,9 GB (+ ZIPs/readmes/basura) |

Readme: se conserva **solo** `📁 readme arquitectura sharck imput V2.1.md` (va en S5). El resto de sueltos S9 → descarte.  
Copia por **subcarpeta en lista blanca**, no carpeta OSS completa.  
Origen no se borra hasta OK final.

---

## 4. README TRASPASOS por destino (memoria de trabajo / auditoría)

Un README TRASPASOS por destino de segmento. Estado al crear este índice:

| Destino | Archivo | Estado |
|---|---|---|
| ui-yaiwes | https://github.com/maxbry123-commits/ui-yaiwes/blob/main/README%20TRASPASOS.md | **pendiente** (aún no existe en main) |
| yaiwes-factory-ui | https://github.com/maxbry123-commits/yaiwes-factory-ui/blob/main/README%20TRASPASOS.md | **pendiente** |
| Yaiwes / shark imput | https://github.com/maxbry123-commits/Yaiwes/blob/main/shark%20imput/README%20TRASPASOS.md | **pendiente** |
| Yaiwes / memoria | https://github.com/maxbry123-commits/Yaiwes/blob/main/memoria/README%20TRASPASOS.md | **hecho** (10d492b; lotes 084eab5 + 4e84727) |

Cada uno debe registrar: origen repo@sha+ruta, destino, manifiesto archivos/bytes, sha256 tree, commits de lote, verdict motor (`VERIFIED_CLOSED`, failed=0, pending=0), read-back de main, checklist GUIA §§1–10.

---

## 5. Estado global

| Ítem | Valor |
|---|---|
| Método | motor_3 (copia); motor_1 solo si hay ZIP sin extraer en destino |
| HF / LFS / Actions | no |
| Borrado de origen | no (espera OK) |
| Segmentos S1–S6 | **en curso** |
| Segmentos S7–S8 (memoria) | **hecho** (084eab5, 4e84727, 10d492b) |
| T4 core componentes | **en planificación** |
| Autoauditoría | obligatoria antes de marcar PASS |

Handoff cableado (cómo reanudar / auditar): [HANDOFF-TRASPASOS.md](./HANDOFF-TRASPASOS.md)


---

## 6. core componentes

Nueva tarea (T4) — descarga + extracción de **115** repos GitHub hacia:

`Yaiwes/Yaiwes core/componentes integrar/`

| Ítem | Valor |
|---|---|
| Destino | `Yaiwes core/componentes integrar/` (repo Yaiwes, main) |
| Cantidad | 115 repos (lista canónica en box: `/workspace/descarga-115/lista.txt`) |
| Rango | SoarGroup/SoarGroup.github.io … ctn-archive/spaun1.0 |
| Sitios web resueltos a GitHub (9) | vespa.ai→vespa-engine/vespa; opensearch.org→opensearch-project/OpenSearch; solr.apache.org→apache/solr; elastic.co/elasticsearch→elastic/elasticsearch; qdrant.tech→qdrant/qdrant; milvus.io→milvus-io/milvus; weaviate.io→weaviate/weaviate; typesense.org→typesense/typesense; lucene.apache.org→apache/lucene |
| Motores | **solo** `motor_2` (descarga) + **engine** + `motor_1` (extracción); **4 motores** en paralelo (lotes ~29 repos c/u) |
| Prohibido | Hugging Face, Git LFS, GitHub Actions, force-push |
| Estado | **en planificación** |

Reparto previsto (4 motores / lotes):

| Motor | Ítems lista.txt | Repos (aprox.) |
|---|---|---|
| M1 | 1–29 | SoarGroup … explosion/spaCy |
| M2 | 30–58 | apache/uima-uimaj … usestrix/strix |
| M3 | 59–87 | tree-sitter … ionic-team/capacitor |
| M4 | 88–115 | pwa-builder/PWABuilder … ctn-archive/spaun1.0 |

Handoff de reanudación / auditoría de esta tarea: [HANDOFF-TRASPASOS.md](./HANDOFF-TRASPASOS.md) § core componentes.
