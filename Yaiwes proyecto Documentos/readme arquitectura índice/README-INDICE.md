# README ÍNDICE — readme arquitectura índice (Yaiwes)

Raíz única de índices y handoffs de los traspasos. Zona horaria: America/Bogota (UTC-5).

## Índice por destino

| Destino | Índice | Handoff | Carpeta |
|---|---|---|---|
| Yaiwes / shark imput | [INDICE shark imput](./INDICE%20shark%20imput.md) | [HANDOFF shark imput](./HANDOFF%20shark%20imput.md) | https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput |
| Yaiwes / memoria | [INDICE memoria](./INDICE%20memoria.md) | [HANDOFF memoria](./HANDOFF%20memoria.md) | https://github.com/maxbry123-commits/Yaiwes/tree/main/memoria |
| Yaiwes core / core kernel Yaiwes principal | [INDICE core kernel](./INDICE%20core%20kernel%20Yaiwes%20principal.md) | [HANDOFF core kernel](./HANDOFF%20core%20kernel%20Yaiwes%20principal.md) | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal |
| Yaiwes core / componentes para integrar al core Yaiwes | [INDICE core componentes](./INDICE%20Yaiwes%20core%20componentes%20para%20integrar%20al%20core%20Yaiwes.md) | [HANDOFF core componentes](./HANDOFF%20Yaiwes%20core%20componentes%20para%20integrar%20al%20core%20Yaiwes.md) | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes |
| ui-yaiwes | https://github.com/maxbry123-commits/ui-yaiwes/blob/main/README%20TRASPASOS.md | (mismo archivo) | https://github.com/maxbry123-commits/ui-yaiwes |
| yaiwes-factory-ui | https://github.com/maxbry123-commits/yaiwes-factory-ui/blob/main/README%20TRASPASOS.md | (mismo archivo) | https://github.com/maxbry123-commits/yaiwes-factory-ui |

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



---
## Cierre final Yaiwes core (2026-10-15)
- core kernel Yaiwes principal: 103 repos + 7 enlazados a shark imput (110/110 de la lista t126u).
- componentes para integrar al core Yaiwes: 49 repos. Los 115 cubiertos: 107 en Yaiwes core + 8 en shark imput.
- Forense blob a blob contra upstream: idéntico salvo renovate (1 archivo excluido por push protection) y MoDr (upstream vacío hoy).


---
## Cierre t130u (2026-10-15)
- core kernel Yaiwes principal: 115 repos (103 lista 1 + 12 lista 2) + 7 enlazados a shark imput. Sin LFS, sin `_archives` en todo Yaiwes. 4 auditorías PASS registradas en cada HANDOFF.


---
## Mini raíces (t132u)
- **Yaiwes core/core kernel Yaiwes principal** — https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal — Núcleo Yaiwes: 115 repos (listas t126u y t130u) verificados contra upstream, con README principal en formato de 4 líneas.
- **Yaiwes core/componentes para integrar al core Yaiwes** — https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes — 49 repos de la lista de 115 pendientes de integrar al core, verificados contra upstream.
- **shark imput** — https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput — Entrada, búsqueda y clasificación de información: core de imput shark + 39 componentes por integrar.
- **memoria** — https://github.com/maxbry123-commits/Yaiwes/tree/main/memoria — Memoria y almacenamiento del orquestador: core de memoria + 13 componentes por integrar.
- **readme arquitectura índice** — https://github.com/maxbry123-commits/Yaiwes/tree/main/readme%20arquitectura%20%C3%ADndice — Índice maestro con índice y handoff cableados por cada destino y las auditorías.
- **claude-notas** — https://github.com/maxbry123-commits/Yaiwes/tree/main/claude-notas — Notas de trabajo de Claude.
- **➡️📂motores de descarga extracción copiado movimiento archivos router-universal-router-inteligente-** — https://github.com/maxbry123-commits/Yaiwes/tree/main/%E2%9E%A1%EF%B8%8F%F0%9F%93%82motores%20de%20descarga%20extracci%C3%B3n%20copiado%20movimiento%20archivos%20router-universal-router-inteligente- — Copia de los motores canónicos (motor_1–4, motor_2 + engine) usada para los traspasos.

## Auditoría t131u (3 pasadas) y limpieza de orígenes
- Pasada 1 (listas): 115 → 107 en Yaiwes core + 8 en shark imput; lista t126u → 104 core + 7 shark; lista 2 → 14/14 (12 nuevos + 2 ya en core); shark imput 40/40 y memoria 13/13 según clasificación v3.
- Pasada 2 (contenido): forense blob a blob de 164 repos de Yaiwes core contra el upstream: idénticos (elasticsearch verificado con árbol completo).
- Pasada 3 (higiene): 0 punteros LFS, 0 filter=lfs, 0 `_archives`, 0 sueltos; duplicado `shark imput/.../prefect` borrado (queda en core kernel, verificado).
- Orígenes borrados tras verificar árbol idéntico por hash: osquestador-auditor (36 carpetas, 2a412c58d), agentes (16, e37a91f91), Agentes-motores-Wordflow-YAIWES (5, 6c58a7378).
