# RIU MEMORY OS — ARQUITECTURA CONSOLIDADA, ANTES DEL CÓDIGO

**Estado:** propuesta de arquitectura para revisión, NO implementación ni despliegue.  
**Decisión rectora:** sistema operativo de **memoria, documentos y contexto**; no un agente, no un chatbot, no el SO general de agentes.  
**Prioridad normativa:** las instrucciones explícitas del usuario y el flujo MEMORY CONTROLLER → PLANILLA/ÍNDICE/HANDOFF → CONTEXT PACK → MEMORY GATE → DELTA → MICROKERNEL CONDICIONAL prevalecen sobre propuestas incompatibles de los anexos.  
**Regla LLM:** 0 llamadas a LLM en la ruta operativa normal. El microkernel semántico es un puerto externo opcional, apagado por defecto y activable solo ante una alerta validada con autorización. No contiene clientes de modelos ni infiere de manera permanente.

## 1. PROPÓSITO Y FRONTERA

Memory OS registra fuentes originales, organiza proyectos/subproyectos/temas/tareas, indexa, recupera, ancla, construye Context Packs, valida evidencia, actualiza estado mediante deltas, conserva handoffs y audita integridad. El cliente externo puede ser Chat, ROOM, Harness, un editor, una LLM o un programa ordinario. El cliente **NO necesita ser un agente**.

**Dentro de Memory OS:** ingesta de conocimiento, normalización, clasificación determinista, hashes, versiones, procedencia, deduplicación, OCR opcional, parsing, fragmentación, búsquedas, grafos de conocimiento, auditoría documental, Event Bus de memoria, sincronización de estado, capacidades/plugins de memoria, índices, anclas, memoria HOT/WARM/COLD, enlaces HF y avisos de cambios de contexto.

**Fuera:** planificación y ejecución de agentes, delegación, proveedores LLM, failover de modelos, navegador/computadora, sandbox de ejecución de código, refactoría, despliegue general, gestor de credenciales, scheduler general, watchdog de ejecución 10 min–48 h, permisos de ejecución de herramientas ajenas a memoria, comunicación directa entre agentes. Memory OS **lee** sus estados por contratos; nunca toma control de ellos. El watchdog interno solo vigila la salud e ingesta de memoria.

## 2. TOPOLOGÍA EXTERNA Y DIAGRAMA PRINCIPAL

```text
USUARIO / CLIENTE EXTERNO (CHAT, ROOM, HARNESS, OTRO SOFTWARE)
                     │ HTTP autenticado / MCP
                     ▼
              MEMORY API / GATE
                     │ valida identidad, scope y capacidad
                     ▼
            MEMORY CONTROLLER
                     │
     ┌───────────────┼────────────────┐
     ▼               ▼                ▼
 PLANILLA/STATE  INDEX/SEARCH     HANDOFF/PROFILE
     │               │                │
     └───────────────┼────────────────┘
                     ▼
                CONTEXT PACK
                     │ respuesta de DATOS al cliente
                     ▼
           CLIENTE EXTERNO TRABAJA
                     │ request memory_read / output delta
                     ▼
                MEMORY GATE
                     │ schema + policy + evidencia
                     ▼
       STATE DELTA + EVENT BUS + AUDITOR
                     │
               ┌─────┴─────┐
               ▼           ▼
             NORMAL      ALERTA
               │           │
               │      MICROKERNEL OFF→REVIEW
               │           │ si se autoriza análisis semántico
               │           ▼
               │       REVISIÓN EXTERNA OPCIONAL
               │       3 REFUTACIONES + 12 CHECKPOINTS
               │           │ propuesta, nunca control
               └─────┬─────┘
                     ▼
         COMMIT VERSIONADO + HANDOFF
                     │
              CONTEXT UPDATE EVENT
                     ▼
          MEMORY OS INACTIVO / ESPERA
```

**Corrección conceptual importante:** un ``AGENTE ON/OFF`` del diagrama original significa *cliente externo activo/inactivo*. Memory OS nunca enciende ni apaga agentes. Se comunica con el Runtime externo y publica disponibilidad/continuidad de contexto; el Runtime decide cuándo ejecutar sus tareas.

## 3. UN KERNEL PEQUEÑO, SEIS MOTORES LÓGICOS Y CAPACIDADES INTERCAMBIABLES

Kernel determinista (ruta, inyección, validación, estado; sin semántica/LLM) y seis motores lógicos dentro del **mismo servicio** al iniciar, no seis servidores:

| Motor | Responsabilidad | NO hace |
|---|---|---|
| Project/Sheet Manager | Jerarquía global→proyecto→subproyecto→tema→objetivo→tarea; planilla tipada, profile, versiones | Planificar/reasignar agentes |
| Index/Retrieval Engine | Inventario, hash, chunks, BM25/FTS5, índices especializados, relaciones, búsqueda selectiva | Inferencia permanente |
| Anchor/Policy Engine | Anclas estrictas por ámbito; privacidad y provenance; inyección autorizada | Dar permisos a un agente |
| Memory Event Bus | Outbox transaccional, triggers de *memoria*, idempotencia, workers de ingestión, reintentos | Despachar tareas generales del sistema |
| Context Pack Builder | Prioridad de fuentes, top-k, presupuesto de tokens, Zero-Recall, push de deltas | Generar respuesta a la pregunta del usuario |
| Handoff/Continuity Engine | Estado verificado, checkpoints, bitácora, evidencia, carry-forward, recuperación | Concluir tareas externas sin prueba |

Capacidades opcionales por contrato común, registradas por **Capability Registry**: Obsidian vault, Graphiti, Graphify, Tencent, Memanto, OCR, BM25S, embeddings/vector, GitHub lector, HF Dataset/Bucket, Phoenix/Prometheus, búsqueda temporal, auditor documental. La arquitectura puede crecer a muchas capacidades sin introducir sus nombres dentro del kernel.

El **Meta Kernel** propuesto en anexos se reduce, dentro de MEMORY OS, a *Capability Registry/Lifecycle*: manifest, version/hash, función, permisos de memoria, dependencias, health, coste y activación. No se duplica el Meta Kernel del SO general.

## 4. MODELO CANÓNICO DE DATOS

Separar lógicamente **tres vistas** sin tres fuentes de verdad:

- **PROFILE**: definición y arquitectura del proyecto, restricciones, identidad, task/anchor activo.
- **INDEX**: dónde están los originales, recursos, enlaces, chunks, versiones, entidades, claims, evidencias.
- **HANDOFF**: estado confirmado, decisiones, gaps, resultado, siguiente paso, checkpoints y links originales.

La **planilla única** integra y referencia estas vistas. Es JSON con esquema, sin reemplazar originales. Campos mínimos:

```json
{
  "schema": "riu.memory-os/v1",
  "owner_id": "owner-01",
  "scope": {"project_id": "router", "subproject_id": "frontend", "topic_id": "team-qwen", "task_id": "T-104"},
  "version": 7,
  "source": {"master_input_ref": "SRC-001", "sha256": "<hash-original>", "immutable": true},
  "objective": {"id": "OBJ-1", "summary": "Verificar selector", "source_ref": "SRC-001"},
  "state": {"status": "IN_PROGRESS", "phase": "VERIFY", "progress": "3/5"},
  "workflow": {"contract_ref": "WF-001", "dependencies": ["T-103"], "next": "TEST"},
  "memory": {"anchor_ref": "ANC-001", "profile_ref": "PRO-001", "index_ref": "IDX-001", "handoff_ref": "HOF-103"},
  "rules": ["RULE-001"], "skills": [{"id": "SK-01", "source_ref": "SRC-SK-01", "required": true}],
  "claims": [{"id": "CLM-001", "status": "SUPPORTED", "evidence_refs": ["EV-001"]}],
  "tags": ["frontend", "verification"],
  "alerts": [], "microkernel": {"status": "OFF", "review_ref": null},
  "closure": {"required_evidence": ["TEST-001"], "status": "PENDING"},
  "updated_at": "<utc timestamp>"
}
```

**Objetos canónicos**: Source (inmutable, bytehash y revisión), Artifact (blob/documento), Chunk (offsets/origen), Project/Sheet, Anchor, Tag, SkillRef, Claim, Evidence, Relation/Edge, StateDelta, MemoryEvent, Handoff, Checkpoint, ContextPack y ResourceManifest. IDs no reutilizables, timestamps UTC, scope explícito, versión y provenance en todos.

**Estados epistemológicos**: `ORIGINAL` (fuente), `VERIFIED`, `SUPPORTED`, `UNVERIFIED`, `HYPOTHESIS`, `CONFLICTED`, `REJECTED`, `SUPERSEDED`, `STALE`. Ningún comentario de un modelo se convierte por sí solo en hecho verificado ni en aprobación del usuario. Los originales permanecen accesibles por hash/revisión. Las eliminaciones autorizadas deben producir tombstones y respetar política de privacidad/retención, no perderse en un simple resumen.

**Memory ABI:** envelope versionado `schema, resource_id, scope, kind, source_ref, content_ref, hash, version, tags, provenance, confidence, visibility, created_at, updated_at, payload` que une OCR, GitHub, documentos, APIs y memoria sin forzar un solo formato interno. Las propuestas de los anexos llamadas Knowledge ABI y Artifact Runtime convergen aquí.

## 5. CINCO CAPAS FUNCIONALES Y TRES TEMPERATURAS (SON EJES DIFERENTES)

**Capas de contexto**: (1) Estado/planilla activa, (2) índice y fragmentos relevantes, (3) instrucciones/skills originales vinculadas al alcance, (4) contratos de workflow y handoff recibidos del Runtime externo, (5) revisión microkernel excepcional.

**Temperaturas de almacenamiento**: HOT = RAM/IndexedDB copia visual del estado inmediato; WARM = SQLite FTS5 y metadatos transaccionales; COLD = originales inmutables, blobs versionados, vault/HF. **No** duplicar copias canónicas en HOT.

**Tiers de conocimiento**: L0 RAW (original), L1 WORKING (sesión), L2 TASK, L3 PROJECT, L4 LONG-TERM reutilizable. Los L0–L3 de Tencent se mapean a un proveedor opcional, sin añadir un segundo gobierno de almacenamiento.

Se mantienen índices de proyectos, documentos, conversaciones, código, APIs, skills, workflows y artefactos, pero se implementan como **tipos/particiones dentro de la misma infraestructura de índice**, no bases de datos duplicadas.

## 6. INGESTA Y AUDITORÍA DOCUMENTAL CON 0 LLM

```text
INPUT AUTORIZADO → REGISTRO SOURCE ORIGINAL → SHA256
 → MIME/SCHEMA → PROJECT/SCOPE → DEDUP EXACTA → VERSIÓN
 → PARSE/OCR OPCIONAL → CHUNKS + OFFSETS + METADATOS
 → FTS5 / BM25 (BM25S si corpus grande, mmap) → ENTIDADES/RELACIONES DETERMINISTAS
 → CLAIMS/EVIDENCE → CHEQUEOS → ÍNDICES + OUTBOX EVENT → HANDOFF/ESTADO
```

Conservar las cualidades del Auditor documental anexo: inventario, Jaccard/huellas para near duplicates, conflicto de versiones sin resolver silenciosamente, árbol de documentos y objetivos, referencias/handoff, 4 workflows declarativos de memoria (`document.new`, `document.audit`, `document.tree`, `project.taskindex`). Las acciones antiguamente llamadas `agent persistir/haystack/auditor/arbolista/plandex/hermes/swe` se convierten en **capacidades deterministas**; se omiten los planners de LLM y la escritura libre a repositorios. Extractores heurísticos entregan `CANDIDATE`, no tareas autorizadas.

Regla contra pérdida: el control de frontera exige 100% de documentos incluidos en inventario y cero conflictos irresueltos **para un cierre certificado del corpus**, no para impedir lecturas parciales ni que otros proyectos trabajen. Conservar original, offsets, SHA, fuente, revisión y licencia del artefacto.

## 7. RETRIEVAL ADAPTATIVO Y ZERO-RECALL

- Ruta rápida: hoja de estado + perfil + handoff → ContextPack; **sin búsqueda inicial** cuando basta.
- Exacto por ID/ruta/hash/tag → SQLite FTS5 BM25 y filtros por scope/ancla → resultados top-3/5 con snippet y provenance.
- Si falta evidencia: índice BM25S de grandes corpus, relaciones Graphiti/Graphify, vector/embeddings (modelo local no generativo) *opt-in*, fusion RRF, temporal y claims.
- Microkernel para casos ambiguos: único punto en que una **LLM externa opcional** puede ayudar a interpretar. `NOT_FOUND` si no hay evidencia y **nunca inventar**.
- `ContextPack` debe dar las instrucciones exactas vigentes, presupuesto de tokens, citas/offset, estado confirmado, referencias por abrir y marcador de datos no confiables. `source_of_truth` resuelve precedencias sin permitir que el texto de documentos ejecute comandos.

**Context Push/Ping**: suscripciones `owner_id+scope+session_id+topic/anchor+version`. El bus emite `context.changed` con `delta` y `ref`, no un prompt interminable ni inyección arbitraria durante un turno ya enviado. Conexiones SSE/websocket/HTTP pueden entregar actualizaciones a clientes que optaron por ellas. Reconexión con cursor y replay versionado. Watch por documento ON/OFF y digest de cambios. Esto conserva el `Context Injection Loop` de los anexos pero con autoridad en el software.

## 8. ANCLAS Y PERMISOS DE MEMORIA

Scopes jerárquicos `owner → project → subproject → topic → task`. Ancla temporal/persistente, STRICT por defecto, configurable exclusivamente por director/software autorizado. Aplique la restricción **en SQL/servidor antes de seleccionar** (no después del retrieval). En `memory_read`, comprobar `owner, scope, resource, allowed_source, version`. `external_memory=false` significa que no se consulta fuera del ámbito, aunque el modelo lo pida. No se pueden superar los scopes pasando el ID de otro recurso.

Mantener separadas: permiso `memory.read` y autorización `memory.write/propose/commit`, `memory.anchor.manage`, `memory.microkernel.request`, `memory.resource.register`. Las tools orientadas a LLM son solo lectura, salvo protocolo de propuestas no canónicas.

## 9. EVENT BUS, TRIGGERS Y RECUPERACIÓN (SOLO MEMORIA)

Eventos permitidos, por ejemplo: `source.ingested`, `document.changed`, `index.stale`, `project.created`, `topic.pinned`, `skill.bound`, `task.state_observed`, `memory.conflict`, `claim.unverified`, `context.requested`, `handoff.committed`, `resource.health.changed`, `context.changed`.

Cada actualización de estado y su evento outbox quedan en **la misma transacción**. Consumidor con `event_id/idempotency_key`, lease y checkpoint; después del ACK, efectos observables con `side_effect_receipt`. Retiro/reintento controlado y dead-letter si falla. No semántica de 'exactly once' para llamadas HTTP externas: asegurar deduplicación/idempotencia, y registrar efectos. Scanner de archivos por evento + conciliación periódica, sin sondeo CPU permanente. Notificador con backpressure y límites de frecuencia.

El bus NO activa agentes ni decide una nueva tarea externa; solamente marca `handoff.ready` o `context.changed` para que el orquestador/Runtime externo lo consuma.

## 10. AUDITORÍAS, REFUTACIONES Y MICROKERNEL

**Siempre determinista**: pruebas de integridad, hashes, autorizaciones, schema, conflicto, cardinalidad, completitud, versiones, procedencia, duplicados, confidencialidad y no-regresión.

**12 checkpoints:** 01 INPUT inmutable, 02 OBJETIVO enlazado, 03 SCOPE permitido, 04 PLAN versionado, 05 TASK/HANDOFF coherente, 06 DEPENDENCIAS válidas, 07 MEMORY TOOLS autorizadas, 08 SKILLS originales y sus pasos vinculados, 09 EVIDENCIA auténtica/procedente, 10 INTEGRIDAD sin contradicción silenciosa, 11 PROGRESO/delta/checkpoint consistente, 12 CIERRE con condiciones y evidencia confirmada.

**3 refutaciones especializadas en memoria:** R1 fidelidad al input/restricciones, R2 completitud/huérfanos/evidencia, R3 contradicción/versiones/fuentes. Pueden ejecutarse con reglas y resultados `PASS|FAIL|UNKNOWN`. Si queda incertidumbre **semántica real** y permiso explícito, microkernel OFF→REVIEW→ON→VERIFY→OFF: envía al adaptador LLM externo SOLO la controversia y fuentes pertinentes; recibe **propuesta en JSON**; software valida y registra; nunca promueve hipótesis a hechos automáticamente, cambia políticas o activa herramientas generales.

**Detector de alucinaciones**: verificador de claims/source/evidence que marca no verificables, no un detector mágico de veracidad. Sin fuentes devuelve `UNVERIFIED`, bloquea cierre certificado. La autoría y la certeza nunca se inventan.

Los anexos describen 4 refutaciones de documento y 12 pasos de Ask Council: las primeras se conservan como **tests deterministas de auditoría documental**, pero Ask Council multi-LLM NO se trasplanta a la ruta normal ni se convierte en una segunda arquitectura. Solo conservar condiciones útiles para el microkernel opcional.

## 11. STORAGE Y DURABILIDAD

**Fuente transaccional de estado única**: SQLite WAL en un volumen persistente de **un único escritor** para instalación simple; PostgreSQL si se requiere escritura distribuida/múltiples instancias. Elegir UNA como fuente de verdad por despliegue. HF buckets/datasets o vault guardan blobs y exportaciones/versiones, NO son sustituto de transacciones para estado concurrente.

- Originales: append-only por SHA y `source_revision` (o referencias remotas firmadas y recuperables), guardados en HF/vault/object storage; claves y ACL fuera del prompt.
- Metadatos: SQLite FTS5, relación SQLite ligera o adaptador Graphiti/Graphify, `events`, `outbox`, `indexes`, `sheet`, `handoff`, `sources`, `claims`, `evidence`, `resources`, `anchors`, `revisions`.
- Backups: snapshots consistentes, manifest SHA256, reconstrucción de índices, comprobación en restauración. No se llama 'persistente' al disco efímero de un Space.
- UI: IndexedDB como cache offline versionada (no autoridad, no secretos); sync de deltas con expected_version/CAS, conflictos visibles.
- Historial chat `/memoria` existente puede truncar registros; nunca guardar la única copia de instrucciones históricas en una cola con truncado.

## 12. RESOURCE BRAIN Y HUGGING FACE >100 GB

Los anexos contienen datasets/modelos/adaptadores LoRA de gran tamaño. Memory OS NO entrena, NO levanta modelos ni realiza despliegues generales; sí inventaría, indexa, verifica, registra y ofrece recursos y enlaces. Un **Resource Manifest** mínimo: `id, kind, provider, repo_id, revision/commit, allow_patterns, size_bytes, sha256, license, visibility, auth_scope, quota, status, last_check, refs`. El `Resource Acquisition Adapter` resuelve manifest/version pinneada, autenticación delegada, streaming/range cuando se soporte, discos/cuotas/checksum, y descarga **solo el recurso solicitado, tras aprobación y verificación**, sin `trust_remote_code` por defecto. Ningún download ejecuta automáticamente el contenido.

**Evolution System** se aplica únicamente a *extensiones de memoria*: descubrir→fijar SHA/licencia→auditar→adaptar contrato→tests→canary→registrar→activar. No copiamos código externo a ciegas, ni convertimos un recurso en una LLM/agente. No prometer rendimiento 100x sin benchmarks: adaptar cache LRU, batching, async pipeline, mmap y deduplicación solamente a ingesta/lectura.

## 13. INTERFACES / PROTOCOLOS

Servidor memory-only HTTP + MCP, manteniendo frontera de dos edificios. La memoria del Edificio 1 se comunica con proveedores del Edificio 2 **solo HTTP firmado/autenticado** y viceversa; ni imports directos `router/↔plugins/`, ni acceso de terceros al `banco`.

**Lecturas para clientes**: `memory_profile`, `memory_index`, `memory_anchor`, `memory_read`, `memory_search`, `memory_handoff`, opcional `memory_related`, `memory_timeline`, `memory_audit`, `memory_context`. **Escrituras de control**: `/memory/ingest`, `/memory/delta/propose`, `/memory/delta/commit`, `/memory/anchor/set`, `/memory/resource/register` protegidas por roles/capabilities, no expuestas libremente a las LLM. Endpoints siempre versionados (`/memory-os/v1/...`) para no romper rutas `/memoria` actuales.

Contrato `GET_CONTEXT(scope, task_id, max_tokens, pinned)` → pack `{context_id, version, sections, evidence_refs, source_refs, budget, missing, provenance}`. `SAVE_STATE_DELTA(expected_version, actor, authorization_ref, proposed_delta, evidence_refs)` → `REJECTED|CONFLICT|COMMITTED` y número de versión; nunca `completed` sin evidencia de fuente auténtica y aprobación externa correspondiente.

**ROUTER/HARNESS** usan Memory OS como una herramienta externa. `ContextPack` es datos; el cliente decide si los adjunta a su modelo. Memory OS no importa SDK de Qwen/Claude, ni herramientas de agentes, ni gobierna prompts generales.

## 14. UI DUAL Y VISTAS

Extensión sobre panel blanco minimalista actual, activo azul: selector proyecto/subproyecto/tema, ancla, fuente vigente, hoja compacta, índice, handoff, skills ligados, conflictos, diff/versiones, proveniencia, alertas, microkernel OFF/REVIEW, salud de conectores y consumo de contexto. En móvil panel compacto plegable, no reescribir frontend. Sincronización de cambios con IndexedDB/versiones.

Tres vistas derivadas, **sin almacenes independientes**: bitácora (`events`), mapa mental (`scope + goal/task hierarchy`), Crazy Wall (`claims/source/evidence/relation graph`). El usuario puede revisar propuestas; la UI no concede permisos por sí sola.

## 15. MATRIZ DE ADAPTACIÓN — ANEXOS (CONSERVAR CUALIDADES, NO SU ARQUITECTURA DE AGENTES)

| Fuente entregada | Propiedad aprovechada en Memory OS | Fuera de alcance / adaptación |
|---|---|---|
| Base de creación auditor y memoria (12.6k líneas) | kernel ROUTE/INJECT, Resource Brain, BM25S, watch/push, OCR, discovery, manifest, context packs | eliminar agent-loop/descarga ejecutable arbitraria |
| Pendientes Obsidian/Graphify/Graphiti/n8n | filesystem vault, graph, parsing incremental, workflows declarativos | no insertar todo en un agent kernel, no exigir UI externa |
| Arquitectura maestra WORKFLOW↔MEMORY | Master Input literal, ABI, goals/tasks refs, claims, Evidence Graph, budgets, StateDelta, RRF, ContextPack | workflow general/LLM/council externo, solo contratos |
| Auditoría MD núcleo | HOT/WARM/COLD, checkpoints, MCP, provenance, hashes, restic, revisiones | quitar spawn subagents y LLM-router del subsistema |
| Auditor A núcleo (Python) | contracts, WAL, journal, atomic writes, circuit breaker, registry | convertir AgentAdapter en Processor/CapabilityAdapter sin motor IA |
| Auditor B plugins | OCR, inbox, Obsidian, hashes, Jaccard, árbol, grafos, handoff, 4 workflows | renombrar agentes a procesadores; aislar notificaciones |
| Auditor C MCP | read tools y contrato de puente | no exponer queue_doc sin auth; no puertos sin acceso seguro |
| GAP auditor documentos | claim verification pendiente; integración proveedor real, frontera auditable | no asumir adaptadores verificados porque exista manifest |
| GAP maestro / documento maestro | Registry/ABI, Dependency Resolver de capacidades, State Manager, policy, pruebas, lifecycle | 80–500 microservicios generales no son alcance MEMORY OS |
| Deepseck.md | inventario de plugins/módulos y gap meta kernel | afirmaciones `100%` históricas requieren cotejo de repo/commit |
| Lyrie DOC-A y DOC-02 | FTS, memoria incremental, backup, checksum drift, project/rules/entities, dedup, import/export | no copiar TS/Bun literalmente ni asumir licencias |
| Tencent memoria | tiers L0–L3, provider seleccionable, atomic/scenario/core memory, RRF | no permitir que proveedor reescriba memoria canónica |
| 03_MEMORIA_GRAPHITI | native capability, scope, privacidad, temporal edges, OCR | Graphiti real opcional y validado, no requisito pesado |
| 04_EVOLUTION_SYSTEM | pin de origen, SHA, licencia, sandbox/canary, registry | solo promocionar extensiones de memoria, no agentes |
| Mavis Connectivity | conectores configurables, circuit breaker, least privilege, secrets broker | no crear otro vault/banco ni conectores de deploy genéricos |
| Mavis Parallel 100x | mmap, batch, dedup, async/backpressure, cache | aplicar solo procesos de memoria; sin promesa '100x' |
| MAX System 100x | idempotency, outbox, checkpoint, recovery, escalado gradual | no multi-sandbox/ejecución de agentes propia |
| HF Dataset/LoRA >100GB | manifests, revision pin, descarga diferida, streaming, hash, cuota | no montar ni entrenar modelos desde memoria |
| ZIP V1/V2/V3 previos | extraer únicamente funcionalidades correctas de memoria después de tests | excluir deployment/team/failover/scheduler general/sentinel agente |

**Conflictos entre fuentes (resueltos por prioridad del usuario)**:
1. “Agentes internos” en plugins → **procesadores deterministas** con manifests, no modelos.
2. “Kernel conoce todo y todo vive dentro del agente” → kernel neutral que ROUTE/INJECT; proveedores solo por ABI.
3. “90/10 LLM” vs requisito “0 LLM salvo microkernel” → **0/opt-in** prevalece.
4. “80–500 microservicios” vs seis motores → seis módulos lógicos; capacidades extensibles, sin microservicios obligatorios.
5. “Descargar/ejecutar todos los datasets/modelos” → registrar y descarga diferida estrictamente aprobada.
6. “State DB en HF bucket” → DB transaccional persistente; HF para originales/backup/artefactos.
7. “Sustituir chat/harness” → preservar contratos, exponer `/memory-os/v1`, cambios mínimos.

## 16. INTEGRACIÓN REAL CON RIU (POR VALIDAR ANTES DE CODIFICAR)

**Archivos de repo ya identificados en lectura previa de main:** `chat/backend/mvp/memoria.py` (respaldo HF truncable), `hf_store.py`, `trabajos.py` (best effort, NO cola transaccional), `plugins/memoria/memoria_yaiwes/__init__.py` (`MemoryFacade`), `runtime_adapters.py`, `router/cognitive_control_plane/context_composer.py`, `source_of_truth.py`, `router/integration/chat_mvp/memoria_loader.py`, `chat/frontend/chat-ancla.js`, `contexto.js`, `proyecto.js`, `handoff-editor.js`, `pendientes-panel.js`, `panel-chat.js` y `api.js`.

**No declarar cableado comprobado** hasta: reconfirmar SHA/rama del repo, leer interfaces actuales, comparar rutas que ya existen, comprobar dónde se persiste SQLite en producción, revisar autenticación, comprobar no duplicar inyección de `contexto.js`, revisar truncados y secreto/token. Nunca modificar arquitectura cross-building por import directo.

## 17. PASADAS DE REVISIÓN ARQUITECTÓNICA ANTES DE PROGRAMAR

**Pasada A — Fronteras:** cada módulo se etiqueta `MEMORY CORE`, `PROVIDER ADAPTER`, `EXTERNAL CONTRACT` o `OUT OF SCOPE`. Ningún chatbot, agente, LLM-router, sandbox ejecutor o deploy general en CORE.

**Pasada B — Fidelidad:** cruza toda capacidad fuente→destino→contrato→test y verifica: raw original, planilla, scopes, profile/index/handoff, tags, provenance, versiones, HA/backup, OCR, resource >100GB, watch context, claims, L0-L4 y HOT/WARM/COLD.

**Pasada C — Operación:** caídas y reintentos, idempotencia, gran corpus, contaminación de scope, historial truncado, caché frío, anotación offline, CAS, licencias, desconexión HF, graph/vector deshabilitado, microkernel OFF, ninguna LLM en ruta normal.

**Pasada D — Integración no destructiva:** probar contra snapshot de repo, diffs mínimos; tests contratuales HTTP/MCP y seguridad, DB schema migration y rollback, UI sin romper, resource quotas, benchmarks token/latencia, staging y canary antes de producción.

**Criterios de aceptación comprobables:** 0 llamadas LLM en operaciones normales; originales con hash y replay; 0 contaminación entre proyectos; anclas en servidor; fuente transaccional durable; tools read-only por defecto; ningún `COMPLETED` aceptado sin evidencia; microkernel inactivo sin autorización; 4 workflows documentales probados; recuperación sin duplicados; índice reconstruible; restitución backup; Context Pack acotado; datos 100GB indexables sin descargar todo; 6 motores sin nuevos servicios forzados; ningún cambio en agente/chatbot fuera de conector UI/API.

## 18. DECISIONES TÉCNICAS CONDICIONALES

- SQLite WAL es la opción inicial **solo si** volumen persistente, un escritor y concurrencia compatible; si existen réplicas/varios escritores, PostgreSQL para estado; no ambos como maestros.
- Graphiti/Neo4j, BM25S, Qdrant, FAISS, Memanto/Tencent y OCR son capabilities seleccionables. Conectores deben ser reales, no `PASS` simulado; estado `UNAVAILABLE` si no configurados.
- Para 100GB+, no cargarlos en RAM ni requerir descarga de dataset completo; indexar metadata/manifests y recuperar fragmentos bajo demanda.
- Una skill original sigue íntegra y con versión; TAG determina vinculación, no permiso para ejecutar instrucciones externas.
- El SO general continúa tomando decisiones de ejecución, riesgos y aprobaciones; memoria solamente informa.

## 19. PRÓXIMO PASO: SOLO REVISIÓN POR CLAUDE, NO CODIFICAR

Entregar este diseño a Claude para auditoría de alcance, coherencia y cualidades preservadas; pedir matriz `CAPACIDAD | FUENTE | DESTINO MEMORY OS | PRUEBA | GAP | CAMBIO MÍNIMO`, incompatibilidades y un contrato ABI refinado. Solo tras aprobación del diseño escribir Python. No instalar los ZIP V2/V3 previos tal como están.
