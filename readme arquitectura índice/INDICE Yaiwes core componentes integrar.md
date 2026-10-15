# YAIWES — BASE DE SOFTWARE
## BLOQUE 1/4 — KERNEL, REGLAS, PLANIFICACIÓN Y ESTADO

### 1. Soar
1. Nombre: Soar
2. URL visible: https://github.com/SoarGroup/SoarGroup.github.io
3. Micro resumen: Arquitectura basada en estado, reglas y selección de operadores. Interesa principalmente su patrón de ciclo de decisión.
4. LOOP: ESTADO → OPERADORES POSIBLES → COMPARAR → SELECCIONAR → APLICAR → NUEVO ESTADO
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/SoarGroup.github.io/ — pendiente de descarga

### 2. OpenNARS
1. Nombre: OpenNARS
2. URL visible: https://github.com/opennars/opennars
3. Micro resumen: Sistema simbólico con conceptos, creencias, objetivos, tareas, operadores e inferencia.
4. LOOP: MEMORIA → TAREA/CONCEPTO → REGLAS → INFERENCIA → NUEVOS HECHOS/TAREAS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/opennars/ — pendiente de descarga

### 3. OpenCog Hyperon / MeTTa
1. Nombre: OpenCog Hyperon / MeTTa
2. URL visible: https://github.com/trueagi-io/hyperon-experimental
3. Micro resumen: Metagrafos, pattern matching, tipos y razonamiento simbólico. Mejor como laboratorio que como dependencia crítica V1.
4. LOOP: HECHOS/GRAFO → MATCH → REGLA → TRANSFORMACIÓN → NUEVO GRAFO
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/hyperon-experimental/ — pendiente de descarga

### 4. Apache KIE / Drools
1. Nombre: Apache KIE / Drools
2. URL visible: https://github.com/apache/incubator-kie
3. Micro resumen: Motor de reglas, eventos y decisiones. Permite sacar muchas pequeñas decisiones fuera de la LLM.
4. LOOP: HECHOS → MATCH REGLAS → REGLAS ACTIVAS → ACCIÓN → NUEVOS HECHOS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/incubator-kie/ — pendiente de descarga

### 5. durable_rules
1. Nombre: durable_rules
2. URL visible: https://github.com/jruizgit/rules
3. Micro resumen: Motor de reglas con eventos, hechos, statecharts, flowcharts y temporizadores.
4. LOOP: EVENTO/HECHO → RETE → REGLA → STATE/FLOW → ACCIÓN
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/rules/ — pendiente de descarga

### 6. Soufflé
1. Nombre: Soufflé
2. URL visible: https://github.com/souffle-lang/souffle
3. Micro resumen: Datalog compilado. Útil para dependencias, deducciones y propagación de estados.
4. LOOP: HECHOS + REGLAS → DATALOG → ITERAR → PUNTO FIJO → HECHOS DERIVADOS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/souffle/ — pendiente de descarga

### 7. egglog
1. Nombre: egglog
2. URL visible: https://github.com/egraphs-good/egglog
3. Micro resumen: Datalog + e-graphs/equality saturation. Conserva varias soluciones equivalentes antes de seleccionar.
4. LOOP: EXPRESIÓN → REWRITE → ALTERNATIVAS → SATURACIÓN → EXTRAER MEJOR
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/egglog/ — pendiente de descarga

### 8. SWI-Prolog
1. Nombre: SWI-Prolog
2. URL visible: https://github.com/SWI-Prolog/swipl-devel
3. Micro resumen: Motor lógico maduro para hechos, reglas y consultas deterministas.
4. LOOP: HECHOS + REGLAS → CONSULTA → UNIFICACIÓN → BACKTRACKING → RESPUESTA
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/swipl-devel/ — pendiente de descarga

### 9. Microsoft Z3
1. Nombre: Microsoft Z3
2. URL visible: https://github.com/Z3Prover/z3
3. Micro resumen: Solver SMT. Puede funcionar como Sheriff matemático de permisos, restricciones e incompatibilidades.
4. LOOP: RESTRICCIONES → SOLVER → SAT / UNSAT → PERMITIR / BLOQUEAR
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/z3/ — pendiente de descarga

### 10. Google OR-Tools
1. Nombre: Google OR-Tools
2. URL visible: https://github.com/google/or-tools
3. Micro resumen: CP-SAT, routing, scheduling y asignación de recursos.
4. LOOP: TAREAS + RECURSOS + COSTES + RESTRICCIONES → SOLVER → PLAN FACTIBLE/ÓPTIMO
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/or-tools/ — pendiente de descarga

### 11. Apache Calcite
1. Nombre: Apache Calcite
2. URL visible: https://github.com/apache/calcite
3. Micro resumen: Optimización mediante reescrituras y comparación de planes según coste.
4. LOOP: PLAN → REWRITE → PLAN A/B/C → COST MODEL → PLAN ELEGIDO
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/calcite/ — pendiente de descarga

### 12. BehaviorTree.CPP
1. Nombre: BehaviorTree.CPP
2. URL visible: https://github.com/BehaviorTree/BehaviorTree.CPP
3. Micro resumen: Árboles de comportamiento, acciones asíncronas y comportamiento reactivo.
4. LOOP: CONDICIÓN → ACTION → SUCCESS/FAIL → RAMA → SIGUIENTE ACTION
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/BehaviorTree.CPP/ — pendiente de descarga

### 13. NetworkX
1. Nombre: NetworkX
2. URL visible: https://github.com/networkx/networkx
3. Micro resumen: Librería Python de grafos. Candidato directo para DAG, dependencias, ciclos y rutas.
4. LOOP: NODOS + EDGES → GRAFO → VALIDAR → READY SET / PATH / ORDER
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/networkx/ — pendiente de descarga

### 14. Kubernetes Controller Pattern
1. Nombre: Kubernetes
2. URL visible: https://github.com/kubernetes/kubernetes
3. Micro resumen: Interesa principalmente el patrón de reconciliación entre estado deseado y estado real.
4. LOOP: ESTADO DESEADO − ESTADO REAL → DELTA → WORKQUEUE → RECONCILE → NUEVO ESTADO
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/kubernetes/ — pendiente de descarga

### 15. Temporal
1. Nombre: Temporal
2. URL visible: https://github.com/temporalio/temporal
3. Micro resumen: Workflows durables, timers, retries, task queues y recuperación después de caídas.
4. LOOP: EVENTO → WORKFLOW STATE → ACTIVITY → CHECKPOINT → WAIT/RETRY → RESUME
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/temporal/ — pendiente de descarga

### 16. SQLite
1. Nombre: SQLite
2. URL visible: https://github.com/sqlite/sqlite
3. Micro resumen: Base local para tareas, estados, triggers, eventos, permisos, evidencias y receipts.
4. LOOP: EVENTO → TRANSACTION → STATE STORE → COMMIT → SIGUIENTE TRIGGER
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/sqlite/ — pendiente de descarga

### 17. NATS
1. Nombre: NATS
2. URL visible: https://github.com/nats-io/nats-server
3. Micro resumen: Bus ligero de eventos/mensajes para cuando YAIWES distribuya procesos.
4. LOOP: EVENT PRODUCER → SUBJECT → NATS → SUBSCRIBER → HANDLER
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/nats-server (ya presente en shark imput — no se descarga de nuevo)

### 18. RabbitMQ
1. Nombre: RabbitMQ
2. URL visible: https://github.com/rabbitmq/rabbitmq-server
3. Micro resumen: Cola de mensajes con ACK/NACK, retry y dead-letter.
4. LOOP: PUBLISH → QUEUE → CONSUME → ACK/NACK → RETRY/DLQ
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/rabbitmq-server/ — pendiente de descarga

### 19. Celery
1. Nombre: Celery
2. URL visible: https://github.com/celery/celery
3. Micro resumen: Cola distribuida de tareas Python. Útil como referencia de workers y resultados.
4. LOOP: TASK → BROKER → WORKER → RESULT → RETRY/COMPLETE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/celery/ — pendiente de descarga

### 20. systemd
1. Nombre: systemd
2. URL visible: https://github.com/systemd/systemd
3. Micro resumen: Lifecycle real: start, stop, watchdog, timeout, restart y kill.
4. LOOP: START → RUNNING → WATCHDOG → HEALTH? → CONTINUE / KILL / RESTART
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/systemd/ — pendiente de descarga

### 21. Bazel
1. Nombre: Bazel
2. URL visible: https://github.com/bazelbuild/bazel
3. Micro resumen: Build incremental basado en dependencias. Reejecuta únicamente lo afectado.
4. LOOP: INPUTS → DEPENDENCY GRAPH → DIRTY NODES → BUILD DELTA → CACHE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/bazel/ — pendiente de descarga

### 22. Differential Dataflow
1. Nombre: Differential Dataflow
2. URL visible: https://github.com/TimelyDataflow/differential-dataflow
3. Micro resumen: Computación incremental sin recalcular todo el sistema.
4. LOOP: CAMBIO Δ → PROPAGAR Δ → ACTUALIZAR AFECTADOS → NUEVO RESULTADO
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/differential-dataflow/ — pendiente de descarga

### 23. pyahocorasick
1. Nombre: pyahocorasick
2. URL visible: https://github.com/WojciechMula/pyahocorasick
3. Micro resumen: Aho-Corasick para reconocer miles de términos/patrones rápidamente en el input.
4. LOOP: INPUT → AUTÓMATA → MATCH MÚLTIPLE → TAGS/INTENT → ÍNDICE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/pyahocorasick/ — pendiente de descarga

### 24. Open Policy Agent
1. Nombre: Open Policy Agent — OPA
2. URL visible: https://github.com/open-policy-agent/opa
3. Micro resumen: Motor independiente de políticas allow/deny.
4. LOOP: REQUEST + STATE + POLICY → EVALUATE → ALLOW / DENY
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/opa/ — pendiente de descarga

### 25. CEL
1. Nombre: Common Expression Language / cel-go
2. URL visible: https://github.com/cel-expr/cel-go
3. Micro resumen: Expresiones deterministas pequeñas para condiciones y triggers.
4. LOOP: STATE + EXPRESSION → EVALUATE → TRUE/FALSE → TRANSITION
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/cel-go/ — pendiente de descarga

### 26. CUE
1. Nombre: CUE
2. URL visible: https://github.com/cue-lang/cue
3. Micro resumen: Definición, unificación y validación de configuración/constraints.
4. LOOP: MANIFEST + CONSTRAINTS → UNIFY → VALIDATE → VALID / ERROR
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/cue/ — pendiente de descarga

### 27. Pydantic
1. Nombre: Pydantic
2. URL visible: https://github.com/pydantic/pydantic
3. Micro resumen: Contratos y modelos tipados Python para las fronteras del Kernel.
4. LOOP: RAW INPUT → PYDANTIC MODEL → VALIDATE → OBJETO TIPADO
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/pydantic (ya presente en shark imput — no se descarga de nuevo)

### 28. python-jsonschema
1. Nombre: python-jsonschema
2. URL visible: https://github.com/python-jsonschema/jsonschema
3. Micro resumen: Validación independiente de documentos JSON contra contratos JSON Schema.
4. LOOP: JSON + SCHEMA → VALIDATOR → PASS / ERRORS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/jsonschema/ — pendiente de descarga

# YAIWES — BASE DE SOFTWARE
## BLOQUE 2/4 — INPUT SHARK, MEMORIA, BÚSQUEDA Y AGENTES CONVERTIBLES

### 29. spaCy
1. Nombre: spaCy
2. URL visible: https://github.com/explosion/spaCy
3. Micro resumen: NLP determinista para tokens, entidades, dependencias y patrones.
4. LOOP: TEXTO → PARSE → ENTIDADES/DEPENDENCIAS → HECHOS/ACCIONES
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/spaCy (ya presente en shark imput — no se descarga de nuevo)

### 30. Apache UIMA
1. Nombre: Apache UIMA
2. URL visible: https://github.com/apache/uima-uimaj
3. Micro resumen: Pipeline de analizadores independientes que enriquecen progresivamente el input.
4. LOOP: TEXTO → ANOTADOR A → B → C → ESTRUCTURA ENRIQUECIDA
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/uima-uimaj/ — pendiente de descarga

### 31. PaddleOCR
1. Nombre: PaddleOCR
2. URL visible: https://github.com/PaddlePaddle/PaddleOCR
3. Micro resumen: OCR y extracción de layout/tablas/documentos.
4. LOOP: PDF/IMAGEN → OCR/LAYOUT → TEXTO + ESTRUCTURA → INPUT SHARK
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/PaddleOCR/ — pendiente de descarga

### 32. Vespa
1. Nombre: Vespa
2. URL visible: https://vespa.ai/
3. Micro resumen: Motor de búsqueda masivo con texto, vectores, filtros y ranking.
4. LOOP: INGEST → INDEX → RETRIEVE → RANK → TOP RESULTS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/vespa/ — pendiente de descarga

### 33. OpenSearch
1. Nombre: OpenSearch
2. URL visible: https://opensearch.org/
3. Micro resumen: Búsqueda BM25, vectorial, híbrida y analytics.
4. LOOP: DOCUMENTOS → INDEX → QUERY → RANK → FRAGMENTOS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/OpenSearch/ — pendiente de descarga

### 34. Apache Solr
1. Nombre: Apache Solr
2. URL visible: https://solr.apache.org/
3. Micro resumen: Búsqueda distribuida full-text/vector basada en Lucene.
4. LOOP: DOCS → DISTRIBUTED INDEX → QUERY → MERGE → RESULTS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/solr/ — pendiente de descarga

### 35. Elasticsearch
1. Nombre: Elasticsearch
2. URL visible: https://www.elastic.co/elasticsearch/
3. Micro resumen: Motor distribuido de búsqueda y analytics.
4. LOOP: INGEST → INDEX → SEARCH → SCORE → RESULT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/elasticsearch/ — pendiente de descarga

### 36. Qdrant
1. Nombre: Qdrant
2. URL visible: https://qdrant.tech/
3. Micro resumen: Base vectorial para búsqueda semántica de contextos y capacidades.
4. LOOP: CHUNK → EMBEDDING → VECTOR STORE → QUERY → TOP MATCHES
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/qdrant/ — pendiente de descarga

### 37. Milvus
1. Nombre: Milvus
2. URL visible: https://milvus.io/
3. Micro resumen: Vector database especializada en escalas grandes.
4. LOOP: VECTORS → INDEX → ANN SEARCH → FILTER → RESULTS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/milvus/ — pendiente de descarga

### 38. Weaviate
1. Nombre: Weaviate
2. URL visible: https://weaviate.io/
3. Micro resumen: Motor vectorial/híbrido para recuperación semántica.
4. LOOP: OBJECTS → VECTOR/INDEX → HYBRID QUERY → FUSION → RESULTS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/weaviate/ — pendiente de descarga

### 39. Typesense
1. Nombre: Typesense
2. URL visible: https://typesense.org/
3. Micro resumen: Search relativamente ligero con keyword y vector.
4. LOOP: DOCS → INDEX → KEYWORD/VECTOR → RANK → RESULT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/typesense/ — pendiente de descarga

### 40. Apache Lucene
1. Nombre: Apache Lucene
2. URL visible: https://lucene.apache.org/
3. Micro resumen: Librería base para índices invertidos y búsqueda.
4. LOOP: DOCUMENT → INDEX → QUERY → SCORE → HITS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/lucene/ — pendiente de descarga

### 41. Meilisearch
1. Nombre: Meilisearch
2. URL visible: https://github.com/meilisearch/meilisearch
3. Micro resumen: Buscador ligero para fichas, componentes, errores y documentación.
4. LOOP: FICHAS → INDEX → SEARCH → FILTER/RANK → TOP RESULTS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/meilisearch/ — pendiente de descarga

### 42. Zoekt
1. Nombre: Zoekt
2. URL visible: https://github.com/sourcegraph/zoekt
3. Micro resumen: Buscador especializado de código fuente.
4. LOOP: SOURCE CODE → INDEX → SYMBOL/TEXT QUERY → MATCHES
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/zoekt (ya presente en shark imput — no se descarga de nuevo)

### 43. CLI-Anything
1. Nombre: CLI-Anything
2. URL visible: https://github.com/HKUDS/CLI-Anything
3. Micro resumen: Convierte software existente en CLI/harness programático. Muy importante para transformar software en motores YAIWES.
4. LOOP: SOFTWARE → ANALIZAR OPERACIONES → CLI/HARNESS → COMMANDS → TEST → REGISTRY
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/CLI-Anything/ — pendiente de descarga

### 44. ECC — Everything Claude Code
1. Nombre: ECC / Everything Claude Code
2. URL visible: https://github.com/affaan-m/ECC
3. Micro resumen: Biblioteca de skills, agentes, hooks, reglas, memoria y workflows. YAIWES debería extraerlos y compilarlos a software.
4. LOOP: SKILLS/RULES/HOOKS → EXTRACT → COMPONENT-IR → PYTHON WORKFLOW/MOTOR
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/ECC/ — pendiente de descarga

### 45. DeepSeek Harness
1. Nombre: DeepSeek Harness
2. URL visible: https://github.com/deepseek-ai/deepseek-harness
3. Micro resumen: Harness modular donde modelos, tools, loops y sesiones pueden ser plugins.
4. LOOP: PROFILE → PLUGIN TREE → SERVICES/EVENTS → EXECUTION LOOP → RESULT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/deepseek-harness/ — pendiente de descarga

### 46. Hermes Agent
1. Nombre: Hermes Agent
2. URL visible: https://github.com/NousResearch/hermes-agent
3. Micro resumen: Agente con muchas tools/plugins. YAIWES debe extraer las capacidades y convertir Hermes en proveedor de motores.
4. LOOP: HERMES REPO → SCAN → CAPABILITIES → NORMALIZE → YAIWES REGISTRY
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/hermes-agent/ — pendiente de descarga

### 47. OpenClaw
1. Nombre: OpenClaw
2. URL visible: https://github.com/openclaw/openclaw
3. Micro resumen: Sistema con tools, skills, plugins, workflows y automatización. Debe convertirse en biblioteca de capacidades.
4. LOOP: OPENCLAW → DISCOVERY → TOOL/SKILL/WORKFLOW → NORMALIZE → MOTOR
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/openclaw/ — pendiente de descarga

### 48. LangChain
1. Nombre: LangChain
2. URL visible: https://github.com/langchain-ai/langchain
3. Micro resumen: Framework para modelos, tools y cadenas. Útil para estudiar wrappers/adapters.
4. LOOP: INPUT → CHAIN/MODEL → TOOL → RESULT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/langchain/ — pendiente de descarga

### 49. LangGraph
1. Nombre: LangGraph
2. URL visible: https://github.com/langchain-ai/langgraph
3. Micro resumen: Workflows/grafos con estado. Interesa su patrón, no darle autoridad sobre YAIWES.
4. LOOP: STATE → NODE → EDGE/CONDITION → NODE → CHECKPOINT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/langgraph/ — pendiente de descarga

### 50. OpenAI Agents SDK
1. Nombre: OpenAI Agents SDK
2. URL visible: https://github.com/openai/openai-agents-python
3. Micro resumen: Function tools, agents, handoffs, guardrails y outputs estructurados.
4. LOOP: RUNNER → AGENT → TOOL/HANDOFF → GUARDRAIL → OUTPUT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/openai-agents-python/ — pendiente de descarga

### 51. Haystack
1. Nombre: Haystack
2. URL visible: https://github.com/deepset-ai/haystack
3. Micro resumen: Componentes y pipelines modulares; interesante para convertir pipelines completos en capacidades.
4. LOOP: COMPONENTS → PIPELINE → EXECUTE → OUTPUT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/haystack/ — pendiente de descarga

### 52. PydanticAI
1. Nombre: PydanticAI
2. URL visible: https://github.com/pydantic/pydantic-ai
3. Micro resumen: Toolsets y function tools agrupables en pools de capacidades.
4. LOOP: PYTHON FUNCTIONS → TOOLSET → FILTER/EXPOSE → CALL → VALIDATE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/pydantic-ai/ — pendiente de descarga

### 53. Microsoft Agent Framework
1. Nombre: Microsoft Agent Framework
2. URL visible: https://github.com/microsoft/agent-framework
3. Micro resumen: Framework actual de Microsoft para agents y workflows.
4. LOOP: EXECUTORS → EDGES → WORKFLOW → RUN → CHECKPOINT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/agent-framework/ — pendiente de descarga

### 54. Strands Harness SDK
1. Nombre: Strands Harness SDK
2. URL visible: https://github.com/strands-agents/harness-sdk
3. Micro resumen: Agent harness con control de tools, sesiones, hooks, budgets y guardrails.
4. LOOP: HARNESS → MODEL → TOOL → HOOK/GUARDRAIL → RESULT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/harness-sdk/ — pendiente de descarga

### 55. AutoGen
1. Nombre: AutoGen
2. URL visible: https://github.com/microsoft/autogen
3. Micro resumen: Framework multiagente legado para proyectos nuevos; útil como referencia.
4. LOOP: AGENT → MESSAGE → AGENT/TOOL → RESPONSE → LOOP
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/autogen/ — pendiente de descarga

### 56. MCP Python SDK
1. Nombre: MCP Python SDK
2. URL visible: https://github.com/modelcontextprotocol/python-sdk
3. Micro resumen: Protocolo para exponer capacidades fuera de YAIWES. Debe vivir en el borde, no en el Kernel.
4. LOOP: YAIWES CAPABILITY → MCP SERVER ↔ CLIENT → EXTERNAL SYSTEM
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/python-sdk (ya presente en shark imput — no se descarga de nuevo)

### 57. Google ARTEMIS
1. Nombre: Google ARTEMIS
2. URL visible: https://github.com/google/artemis
3. Micro resumen: Automatización/pruebas de Android. Puede transformarse en AndroidEngine.
4. LOOP: TASK → DEVICE STATE → ACTION → DEVICE → OBSERVE → VERIFY
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/artemis/ — pendiente de descarga

### 58. Strix
1. Nombre: Strix
2. URL visible: https://github.com/usestrix/strix
3. Micro resumen: Plataforma de análisis de seguridad. Interesa el patrón análisis→validación→reporte.
4. LOOP: APP → ANALYZE → FINDING → VALIDATE → REPORT/FIX
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/strix/ — pendiente de descarga

# YAIWES — BASE DE SOFTWARE
## BLOQUE 3/4 — CODE DISCOVERY, QA, BROWSER, UI Y RUNTIME

### 59. Tree-sitter
1. Nombre: Tree-sitter
2. URL visible: https://github.com/tree-sitter/tree-sitter
3. Micro resumen: Parser incremental multi-lenguaje. Base fuerte para Source Analyzer.
4. LOOP: SOURCE → PARSER → SYNTAX TREE → QUERY → FUNCTIONS/CLASSES/CALLS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/tree-sitter (ya presente en shark imput — no se descarga de nuevo)

### 60. Joern
1. Nombre: Joern
2. URL visible: https://github.com/joernio/joern
3. Micro resumen: Convierte código en Code Property Graph con relaciones de control y datos.
4. LOOP: SOURCE → CPG → GRAPH QUERY → CALL/DATA/CONTROL RELATIONS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/joern/ — pendiente de descarga

### 61. ast-grep
1. Nombre: ast-grep
2. URL visible: https://github.com/ast-grep/ast-grep
3. Micro resumen: Búsqueda y reescritura estructural usando AST.
4. LOOP: CODE → AST PATTERN → MATCH → REPORT/REWRITE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/ast-grep (ya presente en shark imput — no se descarga de nuevo)

### 62. Semgrep
1. Nombre: Semgrep
2. URL visible: https://github.com/semgrep/semgrep
3. Micro resumen: Análisis estático multi-lenguaje mediante reglas.
4. LOOP: SOURCE → RULES → STATIC SCAN → MATCHES → FINDINGS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/semgrep/ — pendiente de descarga

### 63. OSS Review Toolkit
1. Nombre: OSS Review Toolkit — ORT
2. URL visible: https://github.com/oss-review-toolkit/ort
3. Micro resumen: Auditoría de dependencias, licencias y compliance.
4. LOOP: REPO → DEPENDENCIES → LICENSE/POLICY → REPORT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/ort/ — pendiente de descarga

### 64. Syft
1. Nombre: Syft
2. URL visible: https://github.com/anchore/syft
3. Micro resumen: Genera SBOM de repos, archivos e imágenes.
4. LOOP: SOURCE/IMAGE → DISCOVER PACKAGES → SBOM → REGISTRY
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/syft/ — pendiente de descarga

### 65. OSV-Scanner
1. Nombre: OSV-Scanner
2. URL visible: https://github.com/google/osv-scanner
3. Micro resumen: Detecta vulnerabilidades conocidas en dependencias.
4. LOOP: DEPENDENCIES/SBOM → OSV MATCH → VULNERABILITIES → POLICY
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/osv-scanner/ — pendiente de descarga

### 66. Difftastic
1. Nombre: Difftastic
2. URL visible: https://github.com/Wilfred/difftastic
3. Micro resumen: Diff estructural que entiende sintaxis.
4. LOOP: OLD CODE + NEW CODE → PARSE → STRUCTURAL DIFF → CHANGESET
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/difftastic/ — pendiente de descarga

### 67. Ajv
1. Nombre: Ajv
2. URL visible: https://github.com/ajv-validator/ajv
3. Micro resumen: Validador JSON Schema muy rápido para JS/TS.
4. LOOP: JSON → COMPILED SCHEMA → VALIDATE → PASS/ERROR
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/ajv/ — pendiente de descarga

### 68. Wasmtime
1. Nombre: Wasmtime
2. URL visible: https://github.com/bytecodealliance/wasmtime
3. Micro resumen: Runtime WebAssembly aislado para ejecutar componentes en cuarentena.
4. LOOP: COMPONENTE → WASM SANDBOX → RUN → TEST → PROMOTE/REJECT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/wasmtime/ — pendiente de descarga

### 69. Dagger
1. Nombre: Dagger
2. URL visible: https://github.com/dagger/dagger
3. Micro resumen: Motor programable para build, test, package y deploy.
4. LOOP: SOURCE → BUILD → TEST → PACKAGE → ARTIFACT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/dagger/ — pendiente de descarga

### 70. OpenTelemetry Collector
1. Nombre: OpenTelemetry Collector
2. URL visible: https://github.com/open-telemetry/opentelemetry-collector
3. Micro resumen: Recoge traces, logs y métricas de motores y triggers.
4. LOOP: EVENTS → COLLECT → PROCESS → EXPORT → OBSERVE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/opentelemetry-collector/ — pendiente de descarga

### 71. in-toto
1. Nombre: in-toto
2. URL visible: https://github.com/in-toto/in-toto
3. Micro resumen: Registra la cadena de pasos y artefactos ejecutados.
4. LOOP: INPUT → STEP → RECORD METADATA → NEXT STEP → VERIFY CHAIN
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/in-toto/ — pendiente de descarga

### 72. Cosign
1. Nombre: Cosign / Sigstore
2. URL visible: https://github.com/sigstore/cosign
3. Micro resumen: Firma y verifica artefactos antes de activarlos.
4. LOOP: ARTIFACT → SIGN → SIGNATURE → VERIFY → ALLOW/DENY
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/cosign/ — pendiente de descarga

### 73. Renovate
1. Nombre: Renovate
2. URL visible: https://github.com/renovatebot/renovate
3. Micro resumen: Detecta y propone actualizaciones de dependencias.
4. LOOP: DEPENDENCY SCAN → NEW VERSION → PROPOSAL → TEST → APPROVE/REJECT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/renovate/ — pendiente de descarga

### 74. Playwright
1. Nombre: Playwright
2. URL visible: https://github.com/microsoft/playwright
3. Micro resumen: Browser automation y QA. Debe convertirse en BrowserEngine.
4. LOOP: TRIGGER → BROWSER ACTION → DOM/PAGE → EVIDENCE → VERIFY
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/playwright (ya presente en shark imput — no se descarga de nuevo)

### 75. GrapesJS
1. Nombre: GrapesJS
2. URL visible: https://github.com/GrapesJS/grapesjs
3. Micro resumen: Editor visual web con componentes, estilos, commands y storage.
4. LOOP: PAGE MODEL → ADD/MOVE/STYLE → STORAGE → HTML/CSS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/grapesjs/ — pendiente de descarga

### 76. Puck
1. Nombre: Puck
2. URL visible: https://github.com/puckeditor/puck
3. Micro resumen: Editor visual React basado en componentes configurables.
4. LOOP: REGISTER COMPONENTS → DRAG/CONFIG → JSON DATA → RENDER
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/puck/ — pendiente de descarga

### 77. JSONForms
1. Nombre: JSONForms
2. URL visible: https://github.com/eclipsesource/jsonforms
3. Micro resumen: Genera formularios a partir de JSON Schema y UI Schema.
4. LOOP: JSON SCHEMA + UI SCHEMA → RENDERER → FORM → DATA
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/jsonforms/ — pendiente de descarga

### 78. Node-RED
1. Nombre: Node-RED
2. URL visible: https://github.com/node-red/node-red
3. Micro resumen: Programación visual basada en eventos/nodos.
4. LOOP: EVENT → NODE → WIRE → NODE → OUTPUT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/node-red/ — pendiente de descarga

### 79. Blockly
1. Nombre: Blockly
2. URL visible: https://github.com/RaspberryPiFoundation/blockly
3. Micro resumen: Programación visual mediante bloques. Puede generar DSL/workflows.
4. LOOP: BLOCKS → CONNECTION GRAPH → GENERATED DSL/CODE → EXECUTE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/blockly/ — pendiente de descarga

### 80. QuickJS
1. Nombre: QuickJS
2. URL visible: https://github.com/bellard/quickjs
3. Micro resumen: Motor JavaScript pequeño y embebible.
4. LOOP: JS SCRIPT → QUICKJS VM → RESULT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/quickjs/ — pendiente de descarga

### 81. Pyodide
1. Nombre: Pyodide
2. URL visible: https://github.com/pyodide/pyodide
3. Micro resumen: Python sobre WebAssembly para navegador.
4. LOOP: PYTHON → WASM RUNTIME → EXECUTE → RESULT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/pyodide/ — pendiente de descarga

### 82. Sandpack
1. Nombre: Sandpack
2. URL visible: https://github.com/codesandbox/sandpack
3. Micro resumen: Toolkit de editores/previews de código en navegador.
4. LOOP: FILES/CODE → BUNDLER → PREVIEW → RESULT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/sandpack/ — pendiente de descarga

### 83. Dexie.js
1. Nombre: Dexie.js
2. URL visible: https://github.com/dexie/Dexie.js
3. Micro resumen: Wrapper tipado/práctico de IndexedDB.
4. LOOP: OBJECT → DEXIE → INDEXEDDB → QUERY/UPDATE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/Dexie.js/ — pendiente de descarga

### 84. localForage
1. Nombre: localForage
2. URL visible: https://github.com/localForage/localForage
3. Micro resumen: Almacenamiento web simple con fallback.
4. LOOP: KEY/VALUE → LOCALFORAGE → STORAGE → VALUE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/localForage/ — pendiente de descarga

### 85. PouchDB
1. Nombre: PouchDB
2. URL visible: https://github.com/apache/pouchdb
3. Micro resumen: Base local con capacidad de replicación/sincronización.
4. LOOP: LOCAL DOC → DB → CHANGE LOG → OPTIONAL REPLICATION
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/pouchdb/ — pendiente de descarga

### 86. Tauri
1. Nombre: Tauri
2. URL visible: https://github.com/tauri-apps/tauri
3. Micro resumen: Empaqueta frontend web como software desktop/móvil.
4. LOOP: WEB UI → TAURI RUNTIME/IPC → NATIVE PACKAGE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/tauri/ — pendiente de descarga

### 87. Capacitor
1. Nombre: Capacitor
2. URL visible: https://github.com/ionic-team/capacitor
3. Micro resumen: Lleva aplicaciones web a Android/iOS y APIs nativas.
4. LOOP: WEB APP → CAPACITOR BRIDGE → NATIVE APIs → APK/IOS
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/capacitor/ — pendiente de descarga

### 88. PWABuilder
1. Nombre: PWABuilder
2. URL visible: https://github.com/pwa-builder/PWABuilder
3. Micro resumen: Empaquetado de PWA para plataformas instalables.
4. LOOP: WEB/PWA → MANIFEST CHECK → PACKAGE → PLATFORM ARTIFACT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/PWABuilder/ — pendiente de descarga

### 89. whisper.cpp
1. Nombre: whisper.cpp
2. URL visible: https://github.com/ggml-org/whisper.cpp
3. Micro resumen: Transcripción local de audio. Motor externo, no controlador.
4. LOOP: AUDIO → WHISPER ENGINE → TEXT → INPUT SHARK
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/whisper.cpp/ — pendiente de descarga

# YAIWES — BASE DE SOFTWARE
## BLOQUE 4/4 — AUTOEVOLUCIÓN E INVESTIGACIÓN COGNITIVA

### 90. AHE
1. Nombre: Agentic Harness Engineering — AHE
2. URL visible: https://github.com/china-qijizhifeng/agentic-harness-engineering
3. Micro resumen: Investiga/evoluciona componentes de un harness usando evaluación y cambios controlados.
4. LOOP: HARNESS → EVALUATE → TRACE ANALYSIS → MUTATE → TEST → ACCEPT/REJECT ↺
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/agentic-harness-engineering/ — pendiente de descarga

### 91. AutoSkill / SkillEvo
1. Nombre: AutoSkill
2. URL visible: https://github.com/ECNU-ICALK/AutoSkill
3. Micro resumen: Extrae experiencia y crea/mejora skills reutilizables.
4. LOOP: TRAJECTORY → EXTRACT EXPERIENCE → CREATE/MERGE SKILL → EVALUATE → PROMOTE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/AutoSkill/ — pendiente de descarga

### 92. CoEvoSkills
1. Nombre: CoEvoSkills
2. URL visible: https://github.com/Zhang-Henry/CoEvoSkills
3. Micro resumen: Evolución/generación y comprobación de skills.
4. LOOP: EXPERIENCE → SKILL CANDIDATE → VERIFY → EVOLVE → ACCEPT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/CoEvoSkills/ — pendiente de descarga

### 93. Memento-Skills
1. Nombre: Memento-Skills
2. URL visible: https://github.com/Memento-Teams/Memento-Skills
3. Micro resumen: Skills recuperables/persistentes con ciclos de ejecución y reflexión.
4. LOOP: READ SKILL → EXECUTE → REFLECT → CANDIDATE → TEST → PROMOTE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/Memento-Skills/ — pendiente de descarga

### 94. OpenEvolve
1. Nombre: OpenEvolve
2. URL visible: https://github.com/algorithmicsuperintelligence/openevolve
3. Micro resumen: Evolución automática de programas/código mediante evaluación.
4. LOOP: PROGRAM → MUTATE → EVALUATE → SCORE → SELECT → NEXT GENERATION
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/openevolve/ — pendiente de descarga

### 95. Darwin Gödel Machine
1. Nombre: Darwin Gödel Machine
2. URL visible: https://github.com/jennyzzt/dgm
3. Micro resumen: Modificación iterativa de código validada mediante benchmarks.
4. LOOP: CURRENT CODE → CANDIDATE MODIFICATION → BENCHMARK → BETTER? → PROMOTE/ARCHIVE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/dgm/ — pendiente de descarga

### 96. GEPA
1. Nombre: GEPA
2. URL visible: https://github.com/gepa-ai/gepa
3. Micro resumen: Optimización evolutiva/reflexiva de prompts, código y configuraciones.
4. LOOP: CANDIDATE → EXECUTE → TRACE → REFLECT → MUTATE → EVALUATE → SELECT ↺
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/gepa/ — pendiente de descarga

### 97. AFlow
1. Nombre: AFlow
2. URL visible: https://github.com/XiangJinyu/AFlow_
3. Micro resumen: Búsqueda y optimización automática de workflows agentic.
4. LOOP: WORKFLOW CANDIDATE → EXECUTE/EVAL → SEARCH → NEW WORKFLOW → SCORE ↺
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/AFlow_/ — pendiente de descarga

### 98. AgentEvolver
1. Nombre: AgentEvolver
2. URL visible: https://github.com/modelscope/AgentEvolver
3. Micro resumen: Investigación de agentes que evolucionan usando experiencia acumulada.
4. LOOP: EXPERIENCE → ATTRIBUTE → GENERATE/EVOLVE → EVALUATE → UPDATE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/AgentEvolver/ — pendiente de descarga

### 99. EvolveR
1. Nombre: EvolveR
2. URL visible: https://github.com/KnowledgeXLab/EvolveR
3. Micro resumen: Destila principios de trayectorias pasadas y los reutiliza.
4. LOOP: TRAJECTORY → DISTILL PRINCIPLE → MEMORY → RETRIEVE → NEXT RUN
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/EvolveR/ — pendiente de descarga

---

# INVESTIGACIÓN COGNITIVA
# Estos proyectos se estudian para extraer mecanismos.
# No son necesariamente dependencias directas del Kernel.

### 100. LightZero / MuZero
1. Nombre: LightZero / MuZero
2. URL visible: https://github.com/opendilab/LightZero
3. Micro resumen: Planificación y búsqueda mediante modelos aprendidos y búsqueda de árbol.
4. LOOP: STATE → SIMULATE ACTIONS → SEARCH TREE → VALUE → ACTION
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/LightZero/ — pendiente de descarga

### 101. DreamerV3
1. Nombre: DreamerV3
2. URL visible: https://github.com/danijar/dreamerv3
3. Micro resumen: Aprende un modelo del mundo y razona sobre futuros simulados.
4. LOOP: OBSERVE → WORLD MODEL → IMAGINE TRAJECTORIES → VALUE → ACTION
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/dreamerv3/ — pendiente de descarga

### 102. HRM
1. Nombre: Hierarchical Reasoning Model — HRM
2. URL visible: https://github.com/sapientinc/HRM
3. Micro resumen: Investigación de razonamiento jerárquico.
4. LOOP: PROBLEM → HIGH-LEVEL REASONING → LOW-LEVEL REFINEMENT → ANSWER
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/HRM/ — pendiente de descarga

### 103. TRM
1. Nombre: Tiny Recursive Models
2. URL visible: https://github.com/SamsungSAILMontreal/TinyRecursiveModels
3. Micro resumen: Razonamiento mediante iteraciones recursivas.
4. LOOP: INPUT → RECURSIVE STEP → UPDATE STATE → STOP CONDITION → OUTPUT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/TinyRecursiveModels/ — pendiente de descarga

### 104. Huginn
1. Nombre: Huginn / recurrent-pretraining
2. URL visible: https://github.com/seal-rg/recurrent-pretraining
3. Micro resumen: Profundidad recurrente reutilizando bloques de computación.
4. LOOP: INPUT → RECURRENT BLOCK ↺ N → FINAL STATE → OUTPUT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/recurrent-pretraining/ — pendiente de descarga

### 105. MoDr
1. Nombre: Mixture-of-Depth-Recurrent Transformers
2. URL visible: https://github.com/zhangxjohn/MoDr
3. Micro resumen: Arquitectura de rutas/profundidades recurrentes.
4. LOOP: INPUT → SELECT DEPTH/ROUTE → RECURRENT COMPUTE → OUTPUT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/MoDr/ — pendiente de descarga

### 106. Continuous Thought Machines
1. Nombre: CTM
2. URL visible: https://github.com/SakanaAI/continuous-thought-machines
3. Micro resumen: Investigación sobre dinámica temporal interna de razonamiento.
4. LOOP: INPUT → TEMPORAL DYNAMICS → ITERATE → CONVERGENCE → OUTPUT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/continuous-thought-machines/ — pendiente de descarga

### 107. COCONUT
1. Nombre: COCONUT
2. URL visible: https://github.com/facebookresearch/coconut
3. Micro resumen: Razonamiento continuo en representación latente.
4. LOOP: TOKENS → LATENT THOUGHT ↺ → DECODE → ANSWER
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/coconut/ — pendiente de descarga

### 108. Large Concept Model
1. Nombre: Large Concept Model — LCM
2. URL visible: https://github.com/facebookresearch/large_concept_model
3. Micro resumen: Procesamiento sobre conceptos de alto nivel en lugar de tokens aislados.
4. LOOP: INPUT → CONCEPT REPRESENTATION → CONCEPT MODEL → OUTPUT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/large_concept_model/ — pendiente de descarga

### 109. LLaDA
1. Nombre: LLaDA
2. URL visible: https://github.com/ML-GSAI/LLaDA
3. Micro resumen: Modelo de lenguaje basado en difusión/masking.
4. LOOP: MASKED STATE → DENOISE ↺ → TEXT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/LLaDA/ — pendiente de descarga

### 110. Dream
1. Nombre: Dream / Dream-Coder
2. URL visible: https://github.com/DreamLM/Dream
3. Micro resumen: Generación de texto/código mediante procesos tipo difusión.
4. LOOP: MASKED/NOISY REPRESENTATION → DENOISE ↺ → CODE/TEXT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/Dream/ — pendiente de descarga

### 111. BLT
1. Nombre: Byte Latent Transformer
2. URL visible: https://github.com/facebookresearch/blt
3. Micro resumen: Arquitectura que opera a nivel de bytes/representaciones latentes.
4. LOOP: BYTES → LATENT PATCHES → TRANSFORM → BYTES
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/blt/ — pendiente de descarga

### 112. V-JEPA 2
1. Nombre: V-JEPA 2
2. URL visible: https://github.com/facebookresearch/vjepa2
3. Micro resumen: Aprende/predice representaciones de futuros estados visuales.
4. LOOP: OBSERVATION → LATENT STATE → PREDICT FUTURE → COMPARE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/vjepa2/ — pendiente de descarga

### 113. ACT-R
1. Nombre: ACT-R
2. URL visible: https://github.com/asmaloney/ACT-R
3. Micro resumen: Arquitectura cognitiva con memoria, percepción y reglas de producción.
4. LOOP: PERCEPTION/MEMORY → PRODUCTION MATCH → SELECT → ACTION
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/ACT-R/ — pendiente de descarga

### 114. Nengo
1. Nombre: Nengo
2. URL visible: https://github.com/nengo/nengo
3. Micro resumen: Framework para modelar y simular arquitecturas neuronales/cognitivas.
4. LOOP: MODEL → NEURAL NETWORK → SIMULATE → STATE/OUTPUT
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/nengo/ — pendiente de descarga

### 115. Spaun
1. Nombre: Spaun
2. URL visible: https://github.com/ctn-archive/spaun1.0
3. Micro resumen: Arquitectura cognitiva neuronal integrada usada como referencia investigativa.
4. LOOP: PERCEPTION → COGNITIVE MODULES → ACTION/RESPONSE
5. Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20integrar/spaun1.0/ — pendiente de descarga

# PRINCIPIO DE INTEGRACIÓN YAIWES

NO construir:

SOFTWARE A → FRAMEWORK B → FRAMEWORK C → FRAMEWORK D → AGENTE

Construir:

SOFTWARE / REPO / SKILL
→ ANALIZAR
→ COMPONENT-IR
→ EXTRAER CAPACIDADES
→ COMPILAR MOTOR/TOOL/WORKFLOW
→ TEST
→ REGISTRY YAIWES

Y durante ejecución:

INPUT
→ KERNEL PYTHON
→ WORKFLOW
→ STATE
→ TRIGGER
→ MOTOR
→ VERIFY
→ SIGUIENTE STATE

Solo cuando un nodo requiere inteligencia:

TRIGGER
→ REASONING_REQUIRED
→ QWEN / CLAUDE / MOTOR IA
→ RESULT.JSON
→ CERRAR IA
→ VALIDATOR
→ KERNEL CONTINÚA



