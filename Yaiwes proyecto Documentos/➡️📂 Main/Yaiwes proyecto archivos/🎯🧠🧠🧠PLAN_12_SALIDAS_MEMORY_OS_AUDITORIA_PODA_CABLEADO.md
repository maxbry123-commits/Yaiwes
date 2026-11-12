# PLAN CERRADO — MEMORY OS · 12 SALIDAS MÁXIMAS

Estado: propuesta de ejecución. No implica código instalado ni cambios en GitHub.
Fecha de elaboración: 2026-10-25.
Repositorio: `maxbry123-commits/router-universal-router-inteligente-`, rama `main`.
Raíz exclusiva de implementación: `chat-router/memoria/`.

## 0. Mandato congelado

Construir MEMORY OS, **sistema operativo de memoria, almacenamiento y contexto**, NO un agente, chatbot, orquestador de agentes, SDK de agentes ni desplegador.

La arquitectura previamente definida **NO se sustituye**:

```
CLIENTE EXTERNO (chat, ROOM, herramienta o agente)
    → MEMORY CONTROLLER
    → PLANILLA + ÍNDICE + HANDOFF
    → CONTEXT PACK → CLIENTE EXTERNO
    → MEMORY GATE → RESULTADO ESTRUCTURADO / STATE DELTA
    → VALIDACIÓN → PLANILLA → NORMAL / ALERTA
    → MICROKERNEL OPCIONAL (3 REFUTACIONES, 12 CHECKPOINTS)
    → MEMORY EVENT BUS → HANDOFF ACTUALIZADO → ESPERA
```

Seis motores invariables: Project Manager, Index Engine, Anchor Engine, Memory Event Bus, Context Builder, Handoff Engine. Subsistemas auxiliares no son nuevos orquestadores: Storage Providers, Document Ingest/Audit, Resource/Capability Registry, Carousel de triggers, Microkernel excepcional y API/Tools de lectura.

**Normal:** cero inferencias LLM; microkernel OFF. **Excepción:** solicitud autorizada al LLM existente, solo si alerta validada requiere juicio semántico, comprobada y auditada. Ningún componente decide autónomamente invocar LLM ni herramientas externas.

## 1. Fronteras absolutas

No tocar ni reemplazar `chat/backend/mvp/memoria.py`, `chat/backend/mvp/hf_store.py`, `chat/backend/mvp/trabajos.py`, `plugins/hf_storage/`, herramientas existentes, `router/integration/chat_mvp/memoria_loader.py` ni frontend cableado. No se fusionan las memorias. Si la integración solo pudiera hacerse cambiando alguno, producir un PATCH PROPUESTO aparte y marcar BLOQUEADO hasta autorización; no ejecutarlo.

Destino preferente del código nuevo: `chat-router/memoria/memory_os/` con `kernel/`, `contracts/`, `engines/`, `adapters/`, `extensions/`, `integrations/`, `tests/`, `docs/`. El código ajeno en `componentes/` queda intacto; toda poda se entrega como inventario y adaptadores (o parche separado propuesto) hasta validación de licencia y equivalencia.

En `chat-router/memoria/arquitectura/` existen `INPUT-BLOCK-ANTONIO.md` (original literal) y `README-ARQUITECTURA-MEMORIA-ALMACENAMIENTO.md`, que gobiernan el alcance; los 20 MD aportados son entradas para contraste, no permisos para cambiar el diseño. En el README `README-DOS-SISTEMAS-DE-MEMORIA.md` hay propuestas de gobierno general de agentes (S7): **no incorporarlas al MEMORY OS**, salvo la observación de estados como datos.

La comunicación entre edificios del router será solamente mediante contrato HTTP autenticado: no importaciones cruzadas. Los SDK de agentes (OpenAI Agents, Strands, PydanticAI, Haystack) y MCP son solo adaptadores de consumo de Memory Tools, nunca el runtime del sistema.

## 2. Hallazgos iniciales comprobados, no auditoría exhaustiva

- `memoria-yaiwes/memoria_yaiwes/__init__.py` contiene `SQLiteAdapter`, `GraphSQLiteAdapter`, `ComponentAdapter`, `QdrantLocalAdapter` y `MemoryFacade`.
- `memoria-yaiwes/memoria_yaiwes/runtime_adapters.py` contiene `GraphitiAdapter`, `GraphifyCodeAdapter`, `MemantoAdapter` y `build_llm_client`; documenta un vector derivado de 256 dimensiones no semánticas. Hay rutas heredadas con nombres de carpetas antiguas que requieren comprobación de path: **no considerarlas cableadas hasta prueba real**.
- `hf_datasets/plugin.py` ofrece `status/search/info/splits/rows/repo_tree`: NO equivale a descarga general de >100 GB, administración de LoRA ni carga de modelos.
- `componentes/` tiene 16 familias visibles: PyGithub, Sentence-Transformers, aiomysql, asyncpg, chroma, graphify, graphiti, llama_index, memanto, phoenix, postgres, prometheus, qdrant-client, qdrant, redis-py, redis. Algunas contienen archivos ZIP fragmentados y código fuente amplio. Tener copia de fuente NO equivale a servicio funcional ni autoriza copiar código sin revisión de licencia.
- `memoria-yaiwes/tests/` tiene pruebas, pero existen advertencias previas de fallos por rutas heredadas. Todo cambio deberá comparar baseline contra resultados nuevos.

## 3. Formato obligatorio de CADA salida

Una salida entrega su componente o grupo de componentes, sin esperar hasta el final para entregar instrucciones:

1. `SALIDA_XX_AUDITORIA_FUENTES.md`: SHA/commit, árbol de archivos, APIs/funciones reales, dependencias, licencias, riesgos y líneas/rutas examinadas; EXISTE/PARCIAL/NO EXISTE/NO VERIFICADO.
2. `SALIDA_XX_PODA_ADAPTACION.md`: tabla **CONSERVAR / ENVOLVER / PODAR DEL RUNTIME / DIFERIR / EXCLUIR**, razón, qué cualidad se preserva, prueba de equivalencia y ubicación final. Nunca borrar un repositorio proveedor por comodidad.
3. `SALIDA_XX_CODE/`: Python funcional únicamente del Memory OS + manifiestos/contracts/migrations necesarios; mantener el código de proveedor original intacto salvo parche aislado y permitido.
4. `SALIDA_XX_INTEGRACION.md`: cómo enchufa con seis motores, contratos, Trigger Carousel, scopes, eventos y restauración. Instrucciones de config sin secretos.
5. `SALIDA_XX_TESTS/` + `SALIDA_XX_RESULTADOS.md`: pruebas ejecutadas de verdad, resultados crudos y verificación de frontera/no regresión.
6. `SALIDA_XX.zip`: código e instrucciones **de esa salida**. El ZIP global único e instalador se construyen en la salida 12.

Si el proveedor requiere levantar servicios externos o GPU, distinguir **ADAPTADOR LISTO** de **INTEGRACIÓN VERIFICADA EN SERVICIO REAL**. Nunca reportar PASS no ejecutado.

## 4. Plan: 12 salidas máximas

| Salida | Componentes/fuentes que se auditan | Entrega técnica y poda central | Gate mínimo |
|---|---|---|---|
| **01 — Núcleo y compatibilidad** | `memoria-yaiwes/` (2 Python principales, `indices/`, `project-memory/`, 5 tests), arquitectura congelada, ZIP previos SOLO como candidatos | Memory Controller determinista; cinco contratos versionados: MemoryABI, StateDelta, MemoryEvent, ContextPack y ResourceManifest; namespaces proyecto/subproyecto/tarea; SQLite YAIWES adaptado sin duplicarlo; planilla+index+handoff; source receipts y migraciones reversibles | Identidad/scope, instrucciones literales con hash, aislamiento A/B, sin LLM, original intacto |
| **02 — Base durable SQL** | `componentes/postgres`, `asyncpg`, `aiomysql` (3) | StorageAdapter transaccional opcional, pool, versión optimista, WAL/outbox, migraciones idempotentes. SQLite usable por defecto con persistencia real definida; SQL externos OPCIONALES, no exigir nuevo servidor | Commit/rollback, concurrencia CAS, recuperación; no modifica memoria del chat |
| **03 — Eventos, caché y carrusel** | `componentes/redis`, `redis-py` (2), Mavis/Max sobre batching/colas | EventBus durable y outbox en el store escogido; `TriggerCarousel` con registro cerrado, slots de procesadores, prioridad/cuotas/backpressure, dedup/idempotencia, reintentos finitos, dead-letter, fairness; Redis opcional | Eventos una sola vez a nivel estado; revocación, filtro de scope, ninguna acción de agente |
| **04 — Hugging Face de gran tamaño** | `hf_datasets/` y MD de datasets/LoRA >100GB | ResourceRegistry HF: manifest repo/type/revision/hash/licencia/tamaño/scopes, range/lazy/streaming donde API lo permita, caché con cuotas, invalidación, reanudación verificable; NO cargar modelos ni entrenarlos | Descarga selectiva, límites, no >100GB automático, secretos fuera de registros |
| **05 — Graphiti** | `componentes/graphiti/code`, `runtime_adapters.py`, manifiestos y tests originales | GraphAdapter de relaciones temporales, versiones/procedencia; opt-in. Aislar cliente LLM y embeddings que Graphiti puede requerir; si no hay backend compatible, retornar NOT_AVAILABLE y mantener grafo local | 0 LLM normal; hechos citados; recuperación al apagarse proveedor |
| **06 — Graphify** | `componentes/graphify/code`, `runtime_adapters.py` | CodeGraphAdapter para AST, dependencias, rutas, símbolos, mapa del código, reindex incremental por hash y revision; exponer a Index Engine | Sin ejecutar código escaneado; no indexar otro scope; equivalencia de referencias |
| **07 — Memanto y memoria incremental** | `componentes/memanto/code`, dos documentos Lyrie, Tencent Memory adjunto | ReconciliationAdapter batch bajo demanda; portabilidad de ideas verificadas (FTS, memory tiers, reglas, integridad/backup/dedup), sin runtime de agente ni resúmenes automáticos; conflictos NO autocorrigen originales | no sobrescritura silenciosa; contradicciones con evidencia; microkernel OFF si rutina |
| **08 — Búsqueda documental y embeddings** | `Sentence-Transformers`, `chroma`, `llama_index` (3) | SearchAdapter por niveles: ID exacto → SQLite FTS5/BM25 → BM25S si disponible → embeddings/vectores opcionales → fusión RRF. LlamaIndex solo como conectores, nunca loop de agente | respuesta exacta con referencia original, límites de contexto, aislamiento, sin vector obligatorio |
| **09 — Vector y grafo especializado** | `qdrant`, `qdrant-client` (2) | VectorProvider opcional; esquemas/colecciones aisladas, filtros de scope obligatorios en servidor, versionado, borrado lógico, reindexado y fallback; ningún Qdrant server desplegado por el core | aislamiento en el lado del servidor, fail-close ante filtro no aplicable, fallback FTS5 |
| **10 — Ingesta/auditor documental** | GAP maestro, `SALIDA_2_v2_A/B/C`, base 12k líneas, OCR/Obsidian/n8n de MD, fuentes verificadas que existan | InputAdapter y KnowledgeABI: congelar raw, hash, OCR opcional, metadatos, conflictos/versiones/provenance, 4 flujos documentales deterministas, puntos de control; reutilizar MCP como exposición, no clonar servidor inseguro | documentos originales inmutables, no acceso arbitrario por path, input no dispara código |
| **11 — Observabilidad y recursos** | `PyGithub`, `prometheus`, `phoenix` (3), Resource Brain/Evolution | CapabilityRegistry por manifest/version/health/flags/quarantine/canary + métricas/trazas + lector GitHub restringido; cron de reconciliación ligera de recursos y callbacks al Carousel, no auto-deploy | no secretos en logs, no descargas ni pushes no aprobados, alta solo tras test/canary |
| **12 — Cableado final, Context Pack, Microkernel y entrega** | Integración de salidas 01–11, `context_composer.py` y `source_of_truth.py` SOLO por adaptador; MCP/HTTP/tool wrappers; vistas UI si pertenecen a este SO | ContextPack Zero-Recall, 6 memory tools, MemoryGate, triggers planilla/handoff, 3 refutaciones solo ante alerta, 12 checkpoints deterministas, bitácora/mapa/Crazy Wall como proyecciones, prueba E2E y 1 solo ZIP final, README instalación/rollback/env/smoke/operación | pytest + integración real donde sea accesible, prohibición de imports entre edificios, no regresión del chat, reporte de pendientes reales |

## 5. El «Carrusel de Componentes» es software, no un agente

Definición: **rotación/encadenamiento determinista de capacidades de memoria por eventos**, con catálogo aprobado, condiciones tipadas y cola duradera. Cada procesador es una función/capability, no una personalidad, agente, planner o modelo.

```
INPUT / FILE_CHANGED / MEMORY_CONFLICT / HANDOFF_UPDATED
  → MemoryGate y scope
  → EventBus transaccional
  → TriggerCarousel (selección de regla aprobada y prioridad)
  → Slot de capability (Index / OCR / Graph / Audit / HF...)
  → resultado tipado + evidencia
  → StateDelta validado
  → actualización planilla, índice y handoff
  → ACK / siguiente slot / cola muerta, sin bucle libre
```

Ejemplo de DAG determinista: `document.changed → hash → dedup → index → (graph si cambió AST) → audit → context_pack.invalidate → notification`. Slots OFF si capability/servicio no está disponible, permiso no concede ampliar scope, y **no se envía solicitud privilegiada al agente por texto**. Para conflictos que necesitan interpretación, `memory.conflict → alert → microkernel REVIEW` y permanece OFF si no hay autorización.

Elementos obligatorios: contratos JSON-schema; `trigger_id`, `event_id`, `project_id`, `source_version`, `idempotency_key`, tiempo límite, política de reintentos, cancelación, rastreo de efecto, backpressure, circuit breaker, feature flag y registro de evidencias. No hay posibilidad de `eval`, shell arbitraria, auto-registrar permisos ni auto-recursión.

## 6. Inventario de fuentes del usuario

20 MD adjuntos contabilizados (10 primera tanda + 10 segunda) deben aparecer en un `SOURCE_LEDGER.md` con: título original exacto, SHA256, tamaño, líneas, requisitos extraídos, decisiones «incluida / adaptada / excluida», justificación y salida que lo implementa. No usar la cifra de líneas o la presencia de código pegado como prueba de implementación. Documentos heredados sobre agentes/monitores/despliegue son **referencias de patrones**, no órdenes de incorporar sus runtimes. Además, añadir `INPUT-BLOCK-ANTONIO.md`, arquitectura existente, dos README y propuestas previas para preservar trazabilidad.

Se requerirá revisión de compatibilidad de licencias, versiones, submódulos, ZIP partidos y trazas de origen antes de extraer o vender código de terceros. No asumir «licencia abierta» universal.

## 7. Bloqueos, pruebas y política de aceptación

- Gate A, arquitectura: seis motores, ninguna gestión de agentes, ninguna LLM en ruta normal.
- Gate B, datos: fuente original inmutable, hashes versionados, scopes y anclas en backend, migración reversible; chat intacto.
- Gate C, código: pruebas unitarias, contratos, errores negativos, recuperación, no-regresión, resultados de benchmark medidos (no estimaciones 100x).
- Gate D, integración: HTTP autenticado entre edificios, SDK/MCP solo adaptadores, pruebas de cableado del branch verificado.
- Gate E, terceros: licensing + manifest + SHA + pruebas de capacidad + fail-close + monitorización y rollback.
- Gate F, entrega: todas las funciones de matriz cubiertas o explícitamente BLOQUEADAS (nunca PASS simulado); instalador dry-run/apply/rollback sin sobrescribir originales.

No subir ni modificar en GitHub, Space, HF, Cloudflare o Vercel sin solicitud específica de ejecución y verificación de los permisos/cableados reales. Ninguna salida debe afirmar «listo para producción» si solo tiene pruebas locales.

## 8. Puntos que permanecen abiertos y no deben suponerse resueltos

- Persistencia real del destino MEMORY OS: SQLite duradero local / HF remoto / PostgreSQL externo según disponibilidad; esto NO significa migrar `mvp/memoria.py`.
- El commit/base SHA para cada salida debe reconfirmarse antes de producir parches; `main` puede avanzar.
- `Graphiti` puede requerir LLM/embeddings reales para ciertas funciones; delimitar adaptación determinista vs componente opcional.
- Archivos ZIP troceados pueden contener versiones distintas del árbol extraído; auditar sus manifiestos sin ejecutar archivos desconocidos.
- El README de convivencia incluye gobierno de agentes propuesto (S7), fuera de alcance.
