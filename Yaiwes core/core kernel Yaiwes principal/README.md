# README PRINCIPAL — core kernel Yaiwes principal

Componentes de la lista core kernel (t125u/t126u). Formato: Nombre · URL visible · Micro resumen · LOOP.
Carpeta: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal
Hermana: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes
Índice maestro: https://github.com/maxbry123-commits/Yaiwes/blob/main/readme%20arquitectura%20%C3%ADndice/README-INDICE.md

Convención por componente: `<slug>/code/` (HEAD extraído) + `DOWNLOAD_EXTRACT_MANIFEST.json`. `_archives/` borrado en todos tras verificar `code/` contra el manifiesto y contra el árbol upstream (forense blob a blob).
CLI-Anything: **no tocar** (se movió sin modificar contenido).

## 1. ECC
1. Nombre: ECC (affaan-m/ECC)
2. URL visible: https://github.com/affaan-m/ECC
3. Micro resumen: Biblioteca de skills, agentes, hooks, reglas, memoria y workflows. YAIWES debería extraerlos y compilarlos a software.
4. LOOP: SKILLS/RULES/HOOKS → EXTRACT → COMPONENT-IR → PYTHON WORKFLOW/MOTOR
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/ECC — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 2. agentskills
1. Nombre: agentskills (agentskills/agentskills)
2. URL visible: https://github.com/agentskills/agentskills
3. Micro resumen: Specification and documentation for Agent Skills
4. LOOP: ENTRADA → agentskills → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/agentskills — descargado

## 3. apscheduler
1. Nombre: apscheduler (agronholm/apscheduler)
2. URL visible: https://github.com/agronholm/apscheduler
3. Micro resumen: Task scheduling library for Python
4. LOOP: ENTRADA → apscheduler → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/apscheduler — descargado

## 4. MetaClaw
1. Nombre: MetaClaw (aiming-lab/MetaClaw)
2. URL visible: https://github.com/aiming-lab/MetaClaw
3. Micro resumen: 🦞 Just talk to your agent — it learns and EVOLVES 🧬.
4. LOOP: ENTRADA → MetaClaw → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/MetaClaw — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 5. ajv
1. Nombre: ajv (ajv-validator/ajv)
2. URL visible: https://github.com/ajv-validator/ajv
3. Micro resumen: Validador JSON Schema muy rápido para JS/TS.
4. LOOP: JSON → COMPILED SCHEMA → VALIDATE → PASS/ERROR
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/ajv — movido desde los 115

## 6. openevolve
1. Nombre: openevolve (algorithmicsuperintelligence/openevolve)
2. URL visible: https://github.com/algorithmicsuperintelligence/openevolve
3. Micro resumen: Evolución automática de programas/código mediante evaluación.
4. LOOP: PROGRAM → MUTATE → EVALUATE → SCORE → SELECT → NEXT GENERATION
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/openevolve — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 7. syft
1. Nombre: syft (anchore/syft)
2. URL visible: https://github.com/anchore/syft
3. Micro resumen: Genera SBOM de repos, archivos e imágenes.
4. LOOP: SOURCE/IMAGE → DISCOVER PACKAGES → SBOM → REGISTRY
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/syft — movido desde los 115

## 8. pouchdb
1. Nombre: pouchdb (apache/pouchdb)
2. URL visible: https://github.com/apache/pouchdb
3. Micro resumen: Base local con capacidad de replicación/sincronización.
4. LOOP: LOCAL DOC → DB → CHANGE LOG → OPTIONAL REPLICATION
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/pouchdb — movido desde los 115

## 9. ast-grep
1. Nombre: ast-grep (ast-grep/ast-grep)
2. URL visible: https://github.com/ast-grep/ast-grep
3. Micro resumen: Búsqueda y reescritura estructural usando AST.
4. LOOP: CODE → AST PATTERN → MATCH → REPORT/REWRITE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/ast-grep — ya en shark imput (enlazado, no descargado)

## 10. semantic-router
1. Nombre: semantic-router (aurelio-labs/semantic-router)
2. URL visible: https://github.com/aurelio-labs/semantic-router
3. Micro resumen: Superfast AI decision making and intelligent processing of multi-modal data.
4. LOOP: ENTRADA → semantic-router → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/semantic-router — descargado

## 11. quickjs
1. Nombre: quickjs (bellard/quickjs)
2. URL visible: https://github.com/bellard/quickjs
3. Micro resumen: Motor JavaScript pequeño y embebible.
4. LOOP: JS SCRIPT → QUICKJS VM → RESULT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/quickjs — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 12. litellm
1. Nombre: litellm (BerriAI/litellm)
2. URL visible: https://github.com/BerriAI/litellm
3. Micro resumen: The fastest, litest AI Gateway. Rust core with Python SDK. Call 100+ LLM APIs in OpenAI (or native) format with cost tracking, guardrails, load balancing, and logging [Bedrock, Azure, OpenAI, Anthropic, OpenAI, VertexAI, vLLM, Nvidia NIM]
4. LOOP: ENTRADA → litellm → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/litellm — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 13. dramatiq
1. Nombre: dramatiq (Bogdanp/dramatiq)
2. URL visible: https://github.com/Bogdanp/dramatiq
3. Micro resumen: A fast and reliable background task processing library for Python 3.
4. LOOP: ENTRADA → dramatiq → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/dramatiq — descargado

## 14. wasmtime
1. Nombre: wasmtime (bytecodealliance/wasmtime)
2. URL visible: https://github.com/bytecodealliance/wasmtime
3. Micro resumen: Runtime WebAssembly aislado para ejecutar componentes en cuarentena.
4. LOOP: COMPONENTE → WASM SANDBOX → RUN → TEST → PROMOTE/REJECT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/wasmtime — movido desde los 115

## 15. cel-go
1. Nombre: cel-go (cel-expr/cel-go)
2. URL visible: https://github.com/cel-expr/cel-go
3. Micro resumen: Expresiones deterministas pequeñas para condiciones y triggers.
4. LOOP: STATE + EXPRESSION → EVALUATE → TRUE/FALSE → TRANSITION
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/cel-go — movido desde los 115

## 16. celery
1. Nombre: celery (celery/celery)
2. URL visible: https://github.com/celery/celery
3. Micro resumen: Cola distribuida de tareas Python. Útil como referencia de workers y resultados.
4. LOOP: TASK → BROKER → WORKER → RESULT → RETRY/COMPLETE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/celery — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 17. agentic-harness-engineering
1. Nombre: agentic-harness-engineering (china-qijizhifeng/agentic-harness-engineering)
2. URL visible: https://github.com/china-qijizhifeng/agentic-harness-engineering
3. Micro resumen: Investiga/evoluciona componentes de un harness usando evaluación y cambios controlados.
4. LOOP: HARNESS → EVALUATE → TRACE ANALYSIS → MUTATE → TEST → ACCEPT/REJECT ↺
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/agentic-harness-engineering — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 18. sandpack
1. Nombre: sandpack (codesandbox/sandpack)
2. URL visible: https://github.com/codesandbox/sandpack
3. Micro resumen: Toolkit de editores/previews de código en navegador.
4. LOOP: FILES/CODE → BUNDLER → PREVIEW → RESULT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/sandpack — movido desde los 115

## 19. huey
1. Nombre: huey (coleifer/huey)
2. URL visible: https://github.com/coleifer/huey
3. Micro resumen: a little task queue for python
4. LOOP: ENTRADA → huey → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/huey — descargado

## 20. cue
1. Nombre: cue (cue-lang/cue)
2. URL visible: https://github.com/cue-lang/cue
3. Micro resumen: Definición, unificación y validación de configuración/constraints.
4. LOOP: MANIFEST + CONSTRAINTS → UNIFY → VALIDATE → VALID / ERROR
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/cue — movido desde los 115

## 21. dagger
1. Nombre: dagger (dagger/dagger)
2. URL visible: https://github.com/dagger/dagger
3. Micro resumen: Motor programable para build, test, package y deploy.
4. LOOP: SOURCE → BUILD → TEST → PACKAGE → ARTIFACT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/dagger — movido desde los 115

## 22. Bayesian-Agent
1. Nombre: Bayesian-Agent (DataArcTech/Bayesian-Agent)
2. URL visible: https://github.com/DataArcTech/Bayesian-Agent
3. Micro resumen: 🥇 Not Just Another Agent Framework, But a Bayesian Evolution Layer That Can Work Across Harnesses
4. LOOP: ENTRADA → Bayesian-Agent → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/Bayesian-Agent — descargado

## 23. deepseek-harness
1. Nombre: deepseek-harness (deepseek-ai/deepseek-harness)
2. URL visible: https://github.com/deepseek-ai/deepseek-harness
3. Micro resumen: Harness modular donde modelos, tools, loops y sesiones pueden ser plugins.
4. LOOP: PROFILE → PLUGIN TREE → SERVICES/EVENTS → EXECUTION LOOP → RESULT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/deepseek-harness — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 24. haystack
1. Nombre: haystack (deepset-ai/haystack)
2. URL visible: https://github.com/deepset-ai/haystack
3. Micro resumen: Componentes y pipelines modulares; interesante para convertir pipelines completos en capacidades.
4. LOOP: COMPONENTS → PIPELINE → EXECUTE → OUTPUT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/haystack — movido desde los 115

## 25. Dexie.js
1. Nombre: Dexie.js (dexie/Dexie.js)
2. URL visible: https://github.com/dexie/Dexie.js
3. Micro resumen: Wrapper tipado/práctico de IndexedDB.
4. LOOP: OBJECT → DEXIE → INDEXEDDB → QUERY/UPDATE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/Dexie.js — movido desde los 115

## 26. ponytail
1. Nombre: ponytail (DietrichGebert/ponytail)
2. URL visible: https://github.com/DietrichGebert/ponytail
3. Micro resumen: Makes your AI agent think like the laziest senior dev in the room. The best code is the code you never wrote.
4. LOOP: ENTRADA → ponytail → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/ponytail — descargado

## 27. jsonforms
1. Nombre: jsonforms (eclipsesource/jsonforms)
2. URL visible: https://github.com/eclipsesource/jsonforms
3. Micro resumen: Genera formularios a partir de JSON Schema y UI Schema.
4. LOOP: JSON SCHEMA + UI SCHEMA → RENDERER → FORM → DATA
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/jsonforms — movido desde los 115

## 28. AutoSkill
1. Nombre: AutoSkill (ECNU-ICALK/AutoSkill)
2. URL visible: https://github.com/ECNU-ICALK/AutoSkill
3. Micro resumen: Extrae experiencia y crea/mejora skills reutilizables.
4. LOOP: TRAJECTORY → EXTRACT EXPERIENCE → CREATE/MERGE SKILL → EVALUATE → PROMOTE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/AutoSkill — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 29. gepa
1. Nombre: gepa (gepa-ai/gepa)
2. URL visible: https://github.com/gepa-ai/gepa
3. Micro resumen: Optimización evolutiva/reflexiva de prompts, código y configuraciones.
4. LOOP: CANDIDATE → EXECUTE → TRACE → REFLECT → MUTATE → EVALUATE → SELECT ↺
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/gepa — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 30. timesfm
1. Nombre: timesfm (google-research/timesfm)
2. URL visible: https://github.com/google-research/timesfm
3. Micro resumen: TimesFM (Time Series Foundation Model) is a pretrained time-series foundation model developed by Google Research for time-series forecasting.
4. LOOP: ENTRADA → timesfm → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/timesfm — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · reglas filter=lfs quitadas: .gitattributes (archivo eliminado: solo tenía reglas LFS)

## 31. artemis
1. Nombre: artemis (google/artemis)
2. URL visible: https://github.com/google/artemis
3. Micro resumen: Automatización/pruebas de Android. Puede transformarse en AndroidEngine.
4. LOOP: TASK → DEVICE STATE → ACTION → DEVICE → OBSERVE → VERIFY
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/artemis — movido desde los 115

## 32. osv-scanner
1. Nombre: osv-scanner (google/osv-scanner)
2. URL visible: https://github.com/google/osv-scanner
3. Micro resumen: Detecta vulnerabilidades conocidas en dependencias.
4. LOOP: DEPENDENCIES/SBOM → OSV MATCH → VULNERABILITIES → POLICY
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/osv-scanner — movido desde los 115

## 33. watchdog
1. Nombre: watchdog (gorakhargosh/watchdog)
2. URL visible: https://github.com/gorakhargosh/watchdog
3. Micro resumen: Python library and shell utilities to monitor filesystem events.
4. LOOP: ENTRADA → watchdog → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/watchdog — descargado

## 34. grapesjs
1. Nombre: grapesjs (GrapesJS/grapesjs)
2. URL visible: https://github.com/GrapesJS/grapesjs
3. Micro resumen: Editor visual web con componentes, estilos, commands y storage.
4. LOOP: PAGE MODEL → ADD/MOVE/STYLE → STORAGE → HTML/CSS
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/grapesjs — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 35. CLI-Anything
1. Nombre: CLI-Anything (HKUDS/CLI-Anything)
2. URL visible: https://github.com/HKUDS/CLI-Anything
3. Micro resumen: Convierte software existente en CLI/harness programático. Muy importante para transformar software en motores YAIWES.
4. LOOP: SOFTWARE → ANALIZAR OPERACIONES → CLI/HARNESS → COMMANDS → TEST → REGISTRY
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/CLI-Anything — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1) · NO TOCAR

## 36. in-toto
1. Nombre: in-toto (in-toto/in-toto)
2. URL visible: https://github.com/in-toto/in-toto
3. Micro resumen: Registra la cadena de pasos y artefactos ejecutados.
4. LOOP: INPUT → STEP → RECORD METADATA → NEXT STEP → VERIFY CHAIN
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/in-toto — movido desde los 115

## 37. capacitor
1. Nombre: capacitor (ionic-team/capacitor)
2. URL visible: https://github.com/ionic-team/capacitor
3. Micro resumen: Lleva aplicaciones web a Android/iOS y APIs nativas.
4. LOOP: WEB APP → CAPACITOR BRIDGE → NATIVE APIs → APK/IOS
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/capacitor — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 38. SCOPE
1. Nombre: SCOPE (JarvisPei/SCOPE)
2. URL visible: https://github.com/JarvisPei/SCOPE
3. Micro resumen: SCOPE: Self-evolving Context Optimization via Prompt Evolution - A framework for automatic prompt optimization
4. LOOP: ENTRADA → SCOPE → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/SCOPE — descargado

## 39. tenacity
1. Nombre: tenacity (jd/tenacity)
2. URL visible: https://github.com/jd/tenacity
3. Micro resumen: Retrying library for Python
4. LOOP: ENTRADA → tenacity → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/tenacity — descargado

## 40. dgm
1. Nombre: dgm (jennyzzt/dgm)
2. URL visible: https://github.com/jennyzzt/dgm
3. Micro resumen: Modificación iterativa de código validada mediante benchmarks.
4. LOOP: CURRENT CODE → CANDIDATE MODIFICATION → BENCHMARK → BETTER? → PROMOTE/ARCHIVE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/dgm — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · reglas filter=lfs quitadas: .gitattributes (archivo eliminado: solo tenía reglas LFS)

## 41. joern
1. Nombre: joern (joernio/joern)
2. URL visible: https://github.com/joernio/joern
3. Micro resumen: Convierte código en Code Property Graph con relaciones de control y datos.
4. LOOP: SOURCE → CPG → GRAPH QUERY → CALL/DATA/CONTROL RELATIONS
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/joern — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 42. EvolveR
1. Nombre: EvolveR (KnowledgeXLab/EvolveR)
2. URL visible: https://github.com/KnowledgeXLab/EvolveR
3. Micro resumen: Destila principios de trayectorias pasadas y los reutiliza.
4. LOOP: TRAJECTORY → DISTILL PRINCIPLE → MEMORY → RETRIEVE → NEXT RUN
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/EvolveR — movido desde los 115

## 43. langchain
1. Nombre: langchain (langchain-ai/langchain)
2. URL visible: https://github.com/langchain-ai/langchain
3. Micro resumen: Framework para modelos, tools y cadenas. Útil para estudiar wrappers/adapters.
4. LOOP: INPUT → CHAIN/MODEL → TOOL → RESULT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/langchain — movido desde los 115

## 44. langgraph
1. Nombre: langgraph (langchain-ai/langgraph)
2. URL visible: https://github.com/langchain-ai/langgraph
3. Micro resumen: Workflows/grafos con estado. Interesa su patrón, no darle autoridad sobre YAIWES.
4. LOOP: STATE → NODE → EDGE/CONDITION → NODE → CHECKPOINT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/langgraph — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 45. RouteLLM
1. Nombre: RouteLLM (lm-sys/RouteLLM)
2. URL visible: https://github.com/lm-sys/RouteLLM
3. Micro resumen: A framework for serving and evaluating LLM routers - save LLM costs without compromising quality
4. LOOP: ENTRADA → RouteLLM → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/RouteLLM — descargado

## 46. LMCache
1. Nombre: LMCache (LMCache/LMCache)
2. URL visible: https://github.com/LMCache/LMCache
3. Micro resumen: LMCache: Supercharge Your LLM with the Fastest KV Cache Layer
4. LOOP: ENTRADA → LMCache → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/LMCache — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 47. localForage
1. Nombre: localForage (localForage/localForage)
2. URL visible: https://github.com/localForage/localForage
3. Micro resumen: Almacenamiento web simple con fallback.
4. LOOP: KEY/VALUE → LOCALFORAGE → STORAGE → VALUE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/localForage — movido desde los 115

## 48. manim
1. Nombre: manim (ManimCommunity/manim)
2. URL visible: https://github.com/ManimCommunity/manim
3. Micro resumen: A community-maintained Python framework for creating mathematical animations.
4. LOOP: ENTRADA → manim → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/manim — descargado

## 49. meilisearch
1. Nombre: meilisearch (meilisearch/meilisearch)
2. URL visible: https://github.com/meilisearch/meilisearch
3. Micro resumen: Buscador ligero para fichas, componentes, errores y documentación.
4. LOOP: FICHAS → INDEX → SEARCH → FILTER/RANK → TOP RESULTS
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/meilisearch — movido desde los 115

## 50. mem0
1. Nombre: mem0 (mem0ai/mem0)
2. URL visible: https://github.com/mem0ai/mem0
3. Micro resumen: The Memory Layer for AI Agents - Drop-in memory infrastructure for AI agents and apps. Context that persists. Built for production.
4. LOOP: ENTRADA → mem0 → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/mem0 — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 51. Memento-Skills
1. Nombre: Memento-Skills (Memento-Teams/Memento-Skills)
2. URL visible: https://github.com/Memento-Teams/Memento-Skills
3. Micro resumen: Skills recuperables/persistentes con ciclos de ejecución y reflexión.
4. LOOP: READ SKILL → EXECUTE → REFLECT → CANDIDATE → TEST → PROMOTE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/Memento-Skills — movido desde los 115

## 52. MemRL
1. Nombre: MemRL (MemTensor/MemRL)
2. URL visible: https://github.com/MemTensor/MemRL
3. Micro resumen: Paper: “MEMRL: SELF-EVOLVING AGENTS VIA RUNTIME REINFORCEMENT LEARNING ON EPISODIC MEMORY” Open-Source Code
4. LOOP: ENTRADA → MemRL → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/MemRL — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 53. agent-framework
1. Nombre: agent-framework (microsoft/agent-framework)
2. URL visible: https://github.com/microsoft/agent-framework
3. Micro resumen: Framework actual de Microsoft para agents y workflows.
4. LOOP: EXECUTORS → EDGES → WORKFLOW → RUN → CHECKPOINT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/agent-framework — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · 2 punteros LFS eliminados · reglas filter=lfs quitadas: python/packages/lab/lightning/.gitattributes (archivo eliminado: solo tenía reglas LFS)
<details><summary>Rutas LFS eliminadas (2)</summary>

- `python/packages/lab/lightning/assets/train_math_agent.png`
- `python/packages/lab/lightning/assets/train_tau2_agent.png`

</details>

## 54. autogen
1. Nombre: autogen (microsoft/autogen)
2. URL visible: https://github.com/microsoft/autogen
3. Micro resumen: Framework multiagente legado para proyectos nuevos; útil como referencia.
4. LOOP: AGENT → MESSAGE → AGENT/TOOL → RESPONSE → LOOP
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/autogen — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · 51 punteros LFS eliminados · reglas filter=lfs quitadas: .gitattributes (líneas filter=lfs quitadas); dotnet/test/AutoGen.Anthropic.Tests/images/.gitattributes (archivo eliminado: solo tenía reglas LFS)
<details><summary>Rutas LFS eliminadas (51)</summary>

- `autogen-landing.jpg`
- `dotnet/nuget/icon.png`
- `dotnet/resource/images/background.png`
- `dotnet/resource/images/square.png`
- `dotnet/samples/dev-team/docs/images/github-sk-dev-team.png`
- `dotnet/samples/dev-team/docs/images/new-codespace.png`
- `dotnet/samples/dev-team/docs/images/overview.png`
- `dotnet/samples/dev-team/docs/images/solution-explorer.png`
- `dotnet/test/AutoGen.Anthropic.Tests/images/square.png`
- `dotnet/test/AutoGen.Ollama.Tests/images/image.png`
- `dotnet/test/AutoGen.Ollama.Tests/images/square.png`
- `dotnet/test/AutoGen.Tests/ApprovalTests/square.png`
- `dotnet/website/images/articles/CreateAgentWithTools/single-turn-tool-call-with-auto-invoke.png`
- `dotnet/website/images/articles/CreateAgentWithTools/single-turn-tool-call-without-auto-invoke.png`
- `dotnet/website/images/articles/CreateUserProxyAgent/image-1.png`
- `dotnet/website/images/articles/DynamicGroupChat/dynamicChat.gif`
- `dotnet/website/images/articles/PrintMessageMiddleware/printMessage.png`
- `dotnet/website/images/articles/PrintMessageMiddleware/streamingoutput.gif`
- `dotnet/website/images/articles/SequentialGroupChat/SearcherSummarizer.gif`
- `dotnet/website/images/articles/UseAutoGenAsModelinAGStudio/FinalStepsA.png`
- `dotnet/website/images/articles/UseAutoGenAsModelinAGStudio/FinalStepsB.png`
- `dotnet/website/images/articles/UseAutoGenAsModelinAGStudio/FinalStepsC.png`
- `dotnet/website/images/articles/UseAutoGenAsModelinAGStudio/Step5.2OpenAIModel.png`
- `dotnet/website/images/articles/UseAutoGenAsModelinAGStudio/Step5.3ModelNameAndURL.png`
- `dotnet/website/images/articles/UseAutoGenAsModelinAGStudio/Step6.png`
- `dotnet/website/images/articles/UseAutoGenAsModelinAGStudio/Step6b.png`
- `dotnet/website/images/articles/UseAutoGenAsModelinAGStudio/Terminal.png`
- `dotnet/website/images/articles/UseAutoGenAsModelinAGStudio/TheModelTab.png`
- `python/docs/src/_static/images/logo/favicon-16x16.png`
- `python/docs/src/_static/images/logo/favicon-32x32.png`
- `python/docs/src/_static/images/logo/favicon-512x512.png`
- `python/docs/src/images/autogen-magentic-one-agents.png`
- `python/docs/src/images/autogen-magentic-one-example.png`
- `python/docs/src/images/example-company.jpg`
- `python/docs/src/images/example-literature.jpg`
- `python/docs/src/images/example-travel.jpeg`
- `python/docs/src/images/open-ai-telemetry-example.png`
- `python/docs/src/user-guide/agentchat-user-guide/jaeger.png`
- `python/docs/src/user-guide/autogenstudio-user-guide/jsoneditor.jpg`
- `python/docs/src/user-guide/autogenstudio-user-guide/teambuilder.jpg`
- `python/packages/autogen-ext/imgs/task_centric_memory.png`
- `python/packages/autogen-ext/imgs/task_centric_memory_2.png`
- `python/packages/autogen-ext/imgs/task_centric_memory_3.png`
- `python/packages/autogen-studio/docs/ags_screen.png`
- `python/packages/autogen-studio/frontend/src/images/icon.png`
- `python/samples/core_distributed-group-chat/public/avatars/editor.png`
- `python/samples/core_distributed-group-chat/public/avatars/group_chat_manager.png`
- `python/samples/core_distributed-group-chat/public/avatars/user.png`
- `python/samples/core_distributed-group-chat/public/avatars/writer.png`
- `python/samples/core_distributed-group-chat/public/favicon.png`
- `python/samples/core_distributed-group-chat/public/logo.png`

</details>

## 55. LLMLingua
1. Nombre: LLMLingua (microsoft/LLMLingua)
2. URL visible: https://github.com/microsoft/LLMLingua
3. Micro resumen: [EMNLP'23, ACL'24] To speed up LLMs' inference and enhance LLM's perceive of key information, compress the prompt and KV-Cache, which achieves up to 20x compression with minimal performance loss.
4. LOOP: ENTRADA → LLMLingua → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/LLMLingua — ya en shark imput (enlazado, no descargado)

## 56. playwright
1. Nombre: playwright (microsoft/playwright)
2. URL visible: https://github.com/microsoft/playwright
3. Micro resumen: Browser automation y QA. Debe convertirse en BrowserEngine.
4. LOOP: TRIGGER → BROWSER ACTION → DOM/PAGE → EVIDENCE → VERIFY
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/playwright — ya en shark imput (enlazado, no descargado)

## 57. python-sdk
1. Nombre: python-sdk (modelcontextprotocol/python-sdk)
2. URL visible: https://github.com/modelcontextprotocol/python-sdk
3. Micro resumen: Protocolo para exponer capacidades fuera de YAIWES. Debe vivir en el borde, no en el Kernel.
4. LOOP: YAIWES CAPABILITY → MCP SERVER ↔ CLIENT → EXTERNAL SYSTEM
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/python-sdk — ya en shark imput (enlazado, no descargado)

## 58. AgentEvolver
1. Nombre: AgentEvolver (modelscope/AgentEvolver)
2. URL visible: https://github.com/modelscope/AgentEvolver
3. Micro resumen: Investigación de agentes que evolucionan usando experiencia acumulada.
4. LOOP: EXPERIENCE → ATTRIBUTE → GENERATE/EVOLVE → EVALUATE → UPDATE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/AgentEvolver — movido desde los 115

## 59. memanto
1. Nombre: memanto (moorcheh-ai/memanto)
2. URL visible: https://github.com/moorcheh-ai/memanto
3. Micro resumen: Memory that AI Agents Love!
4. LOOP: ENTRADA → memanto → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/memanto — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · reglas filter=lfs quitadas: .gitattributes (archivo eliminado: solo tenía reglas LFS)

## 60. rea
1. Nombre: rea (morluto/rea)
2. URL visible: https://github.com/morluto/rea
3. Micro resumen: Reverse engineer anything with agents, from app behavior down to native binaries.
4. LOOP: ENTRADA → rea → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/rea — descargado

## 61. motion-canvas
1. Nombre: motion-canvas (motion-canvas/motion-canvas)
2. URL visible: https://github.com/motion-canvas/motion-canvas
3. Micro resumen: Visualize Your Ideas With Code
4. LOOP: ENTRADA → motion-canvas → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/motion-canvas — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 62. nats-server
1. Nombre: nats-server (nats-io/nats-server)
2. URL visible: https://github.com/nats-io/nats-server
3. Micro resumen: Bus ligero de eventos/mensajes para cuando YAIWES distribuya procesos.
4. LOOP: EVENT PRODUCER → SUBJECT → NATS → SUBSCRIBER → HANDLER
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/nats-server — ya en shark imput (enlazado, no descargado)

## 63. txtai
1. Nombre: txtai (neuml/txtai)
2. URL visible: https://github.com/neuml/txtai
3. Micro resumen: 💡 All-in-one AI framework for semantic search, LLM orchestration and language model workflows
4. LOOP: ENTRADA → txtai → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/txtai — descargado

## 64. prompt-master
1. Nombre: prompt-master (nidhinjs/prompt-master)
2. URL visible: https://github.com/nidhinjs/prompt-master
3. Micro resumen: A Claude skill that writes the accurate prompts for any AI tool. Zero tokens or credits wasted. Full context and memory retention
4. LOOP: ENTRADA → prompt-master → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/prompt-master — descargado

## 65. node-red
1. Nombre: node-red (node-red/node-red)
2. URL visible: https://github.com/node-red/node-red
3. Micro resumen: Programación visual basada en eventos/nodos.
4. LOOP: EVENT → NODE → WIRE → NODE → OUTPUT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/node-red — movido desde los 115

## 66. opa
1. Nombre: opa (open-policy-agent/opa)
2. URL visible: https://github.com/open-policy-agent/opa
3. Micro resumen: Motor independiente de políticas allow/deny.
4. LOOP: REQUEST + STATE + POLICY → EVALUATE → ALLOW / DENY
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/opa — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 67. opentelemetry-collector
1. Nombre: opentelemetry-collector (open-telemetry/opentelemetry-collector)
2. URL visible: https://github.com/open-telemetry/opentelemetry-collector
3. Micro resumen: Recoge traces, logs y métricas de motores y triggers.
4. LOOP: EVENTS → COLLECT → PROCESS → EXPORT → OBSERVE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/opentelemetry-collector — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 68. openai-agents-python
1. Nombre: openai-agents-python (openai/openai-agents-python)
2. URL visible: https://github.com/openai/openai-agents-python
3. Micro resumen: Function tools, agents, handoffs, guardrails y outputs estructurados.
4. LOOP: RUNNER → AGENT → TOOL/HANDOFF → GUARDRAIL → OUTPUT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/openai-agents-python — movido desde los 115

## 69. ort
1. Nombre: ort (oss-review-toolkit/ort)
2. URL visible: https://github.com/oss-review-toolkit/ort
3. Micro resumen: Auditoría de dependencias, licencias y compliance.
4. LOOP: REPO → DEPENDENCIES → LICENSE/POLICY → REPORT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/ort — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 70. gateway
1. Nombre: gateway (Portkey-AI/gateway)
2. URL visible: https://github.com/Portkey-AI/gateway
3. Micro resumen: A blazing fast AI Gateway with integrated guardrails. Route to 1,600+ LLMs, 50+ AI Guardrails with 1 fast & friendly API.
4. LOOP: ENTRADA → gateway → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/gateway — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 71. prefect
1. Nombre: prefect (PrefectHQ/prefect)
2. URL visible: https://github.com/PrefectHQ/prefect
3. Micro resumen: Prefect is a workflow orchestration framework for building resilient data pipelines in Python.
4. LOOP: ENTRADA → prefect → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/prefect — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 72. puck
1. Nombre: puck (puckeditor/puck)
2. URL visible: https://github.com/puckeditor/puck
3. Micro resumen: Editor visual React basado en componentes configurables.
4. LOOP: REGISTER COMPONENTS → DRAG/CONFIG → JSON DATA → RENDER
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/puck — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 73. PWABuilder
1. Nombre: PWABuilder (pwa-builder/PWABuilder)
2. URL visible: https://github.com/pwa-builder/PWABuilder
3. Micro resumen: Empaquetado de PWA para plataformas instalables.
4. LOOP: WEB/PWA → MANIFEST CHECK → PACKAGE → PLATFORM ARTIFACT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/PWABuilder — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · reglas filter=lfs quitadas: apps/pwabuilder-microsoft-store/.gitattributes (archivo eliminado: solo tenía reglas LFS)

## 74. pydantic-ai
1. Nombre: pydantic-ai (pydantic/pydantic-ai)
2. URL visible: https://github.com/pydantic/pydantic-ai
3. Micro resumen: Toolsets y function tools agrupables en pools de capacidades.
4. LOOP: PYTHON FUNCTIONS → TOOLSET → FILTER/EXPOSE → CALL → VALIDATE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/pydantic-ai — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 75. pyodide
1. Nombre: pyodide (pyodide/pyodide)
2. URL visible: https://github.com/pyodide/pyodide
3. Micro resumen: Python sobre WebAssembly para navegador.
4. LOOP: PYTHON → WASM RUNTIME → EXECUTE → RESULT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/pyodide — movido desde los 115

## 76. pluggy
1. Nombre: pluggy (pytest-dev/pluggy)
2. URL visible: https://github.com/pytest-dev/pluggy
3. Micro resumen: A minimalist production ready plugin system
4. LOOP: ENTRADA → pluggy → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/pluggy — descargado

## 77. transitions
1. Nombre: transitions (pytransitions/transitions)
2. URL visible: https://github.com/pytransitions/transitions
3. Micro resumen: A lightweight, object-oriented finite state machine implementation in Python with many extensions
4. LOOP: ENTRADA → transitions → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/transitions — descargado

## 78. qdrant
1. Nombre: qdrant (qdrant/qdrant)
2. URL visible: https://github.com/qdrant/qdrant
3. Micro resumen: Qdrant - High-performance, massive-scale Vector Database and Vector Search Engine for the next generation of AI. Also available in the cloud https://cloud.qdrant.io/
4. LOOP: ENTRADA → qdrant → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/qdrant — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · 1 punteros LFS eliminados · reglas filter=lfs quitadas: .gitattributes (líneas filter=lfs quitadas)
<details><summary>Rutas LFS eliminadas (1)</summary>

- `tests/e2e_tests/test_data/storage.tar.xz`

</details>

## 79. blockly
1. Nombre: blockly (RaspberryPiFoundation/blockly)
2. URL visible: https://github.com/RaspberryPiFoundation/blockly
3. Micro resumen: Programación visual mediante bloques. Puede generar DSL/workflows.
4. LOOP: BLOCKS → CONNECTION GRAPH → GENERATED DSL/CODE → EXECUTE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/blockly — movido desde los 115

## 80. one-skill-to-rule-them-all
1. Nombre: one-skill-to-rule-them-all (rebelytics/one-skill-to-rule-them-all)
2. URL visible: https://github.com/rebelytics/one-skill-to-rule-them-all
3. Micro resumen: The meta-skill that builds and improves all your skills, including itself. Watches your work sessions (autonomous or human-led), captures patterns, corrections and judgement calls, and turns them into skill improvements and new skill candidates for your review. Practical application of the Augmented Expertise methodology. Open source: CC BY 4.0.
4. LOOP: ENTRADA → one-skill-to-rule-them-all → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/one-skill-to-rule-them-all — descargado

## 81. redis-vl-python
1. Nombre: redis-vl-python (redis/redis-vl-python)
2. URL visible: https://github.com/redis/redis-vl-python
3. Micro resumen: Redis Vector Library. The AI-native Python client for Redis.
4. LOOP: ENTRADA → redis-vl-python → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/redis-vl-python — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 82. claude-code-plugin
1. Nombre: claude-code-plugin (remotion-dev/claude-code-plugin)
2. URL visible: https://github.com/remotion-dev/claude-code-plugin
3. Micro resumen: Remotion Agent Skills for Claude Code
4. LOOP: ENTRADA → claude-code-plugin → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/claude-code-plugin — descargado

## 83. remotion
1. Nombre: remotion (remotion-dev/remotion)
2. URL visible: https://github.com/remotion-dev/remotion
3. Micro resumen: 🎥      Make videos programmatically with React
4. LOOP: ENTRADA → remotion → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/remotion — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 84. skills
1. Nombre: skills (remotion-dev/skills)
2. URL visible: https://github.com/remotion-dev/skills
3. Micro resumen: Agent Skills
4. LOOP: ENTRADA → skills → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/skills — descargado

## 85. renovate
1. Nombre: renovate (renovatebot/renovate)
2. URL visible: https://github.com/renovatebot/renovate
3. Micro resumen: Detecta y propone actualizaciones de dependencias.
4. LOOP: DEPENDENCY SCAN → NEW VERSION → PROPOSAL → TEST → APPROVE/REJECT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/renovate — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · excluido (no es LFS): docs/usage/docker.md — GitHub push protection (Google Cloud Service Account Credentials, línea 409); no es LFS · 1 symlink(s) omitidos (regla del engine)

## 86. watchfiles
1. Nombre: watchfiles (samuelcolvin/watchfiles)
2. URL visible: https://github.com/samuelcolvin/watchfiles
3. Micro resumen: Simple, modern and fast file watching and code reload for Python, written in Rust
4. LOOP: ENTRADA → watchfiles → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/watchfiles — descargado

## 87. semgrep
1. Nombre: semgrep (semgrep/semgrep)
2. URL visible: https://github.com/semgrep/semgrep
3. Micro resumen: Análisis estático multi-lenguaje mediante reglas.
4. LOOP: SOURCE → RULES → STATIC SCAN → MATCHES → FINDINGS
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/semgrep — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 88. continual-harness
1. Nombre: continual-harness (sethkarten/continual-harness)
2. URL visible: https://github.com/sethkarten/continual-harness
3. Micro resumen: Official repository of the paper: Continual Harness: Online Adaptation for Self-Improving Foundation Agents and PokeAgent Speedrun Track 2
4. LOOP: ENTRADA → continual-harness → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/continual-harness — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 89. cosign
1. Nombre: cosign (sigstore/cosign)
2. URL visible: https://github.com/sigstore/cosign
3. Micro resumen: Firma y verifica artefactos antes de activarlos.
4. LOOP: ARTIFACT → SIGN → SIGNATURE → VERIFY → ALLOW/DENY
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/cosign — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 90. zoekt
1. Nombre: zoekt (sourcegraph/zoekt)
2. URL visible: https://github.com/sourcegraph/zoekt
3. Micro resumen: Buscador especializado de código fuente.
4. LOOP: SOURCE CODE → INDEX → SYMBOL/TEXT QUERY → MATCHES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/zoekt — ya en shark imput (enlazado, no descargado)

## 91. meta-harness
1. Nombre: meta-harness (stanford-iris-lab/meta-harness)
2. URL visible: https://github.com/stanford-iris-lab/meta-harness
3. Micro resumen: Official code for Meta-Harness (2603.28052)
4. LOOP: ENTRADA → meta-harness → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/meta-harness — descargado

## 92. harness-sdk
1. Nombre: harness-sdk (strands-agents/harness-sdk)
2. URL visible: https://github.com/strands-agents/harness-sdk
3. Micro resumen: Agent harness con control de tools, sesiones, hooks, budgets y guardrails.
4. LOOP: HARNESS → MODEL → TOOL → HOOK/GUARDRAIL → RESULT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/harness-sdk — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 93. taskiq
1. Nombre: taskiq (taskiq-python/taskiq)
2. URL visible: https://github.com/taskiq-python/taskiq
3. Micro resumen: Distributed task queue with full async support
4. LOOP: ENTRADA → taskiq → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/taskiq — descargado

## 94. tauri
1. Nombre: tauri (tauri-apps/tauri)
2. URL visible: https://github.com/tauri-apps/tauri
3. Micro resumen: Empaqueta frontend web como software desktop/móvil.
4. LOOP: WEB UI → TAURI RUNTIME/IPC → NATIVE PACKAGE
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/tauri — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 95. sdk-python
1. Nombre: sdk-python (temporalio/sdk-python)
2. URL visible: https://github.com/temporalio/sdk-python
3. Micro resumen: Temporal Python SDK
4. LOOP: ENTRADA → sdk-python → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/sdk-python — descargado

## 96. temporal
1. Nombre: temporal (temporalio/temporal)
2. URL visible: https://github.com/temporalio/temporal
3. Micro resumen: Workflows durables, timers, retries, task queues y recuperación después de caídas.
4. LOOP: EVENTO → WORKFLOW STATE → ACTIVITY → CHECKPOINT → WAIT/RETRY → RESUME
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/temporal — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · reglas filter=lfs quitadas: .gitattributes (archivo eliminado: solo tenía reglas LFS) · 2 symlink(s) omitidos (regla del engine)

## 97. Life-Harness
1. Nombre: Life-Harness (Tianshi-Xu/Life-Harness)
2. URL visible: https://github.com/Tianshi-Xu/Life-Harness
3. Micro resumen: Offical implementation of "Life-Harness"
4. LOOP: ENTRADA → Life-Harness → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/Life-Harness — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 98. tree-sitter
1. Nombre: tree-sitter (tree-sitter/tree-sitter)
2. URL visible: https://github.com/tree-sitter/tree-sitter
3. Micro resumen: Parser incremental multi-lenguaje. Base fuerte para Source Analyzer.
4. LOOP: SOURCE → PARSER → SYNTAX TREE → QUERY → FUNCTIONS/CLASSES/CALLS
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/tree-sitter — ya en shark imput (enlazado, no descargado)

## 99. trigger.dev
1. Nombre: trigger.dev (triggerdotdev/trigger.dev)
2. URL visible: https://github.com/triggerdotdev/trigger.dev
3. Micro resumen: Trigger.dev – build and deploy durable AI agents and workflows
4. LOOP: ENTRADA → trigger.dev → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/trigger.dev — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 100. archify
1. Nombre: archify (tt-a1i/archify)
2. URL visible: https://github.com/tt-a1i/archify
3. Micro resumen: Turn any idea, plan, or codebase into a beautiful interactive diagram. An agent skill for Claude Code, Codex, and more.
4. LOOP: ENTRADA → archify → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/archify — descargado

## 101. strix
1. Nombre: strix (usestrix/strix)
2. URL visible: https://github.com/usestrix/strix
3. Micro resumen: Plataforma de análisis de seguridad. Interesa el patrón análisis→validación→reporte.
4. LOOP: APP → ANALYZE → FINDING → VALIDATE → REPORT/FIX
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/strix — movido desde los 115

## 102. agent-browser
1. Nombre: agent-browser (vercel-labs/agent-browser)
2. URL visible: https://github.com/vercel-labs/agent-browser
3. Micro resumen: Browser automation CLI for AI agents
4. LOOP: ENTRADA → agent-browser → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/agent-browser — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 103. vllm
1. Nombre: vllm (vllm-project/vllm)
2. URL visible: https://github.com/vllm-project/vllm
3. Micro resumen: A high-throughput and memory-efficient inference and serving engine for LLMs
4. LOOP: ENTRADA → vllm → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/vllm — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

## 104. anatomy
1. Nombre: anatomy (wheresryan22/anatomy)
2. URL visible: https://github.com/wheresryan22/anatomy
3. Micro resumen: An agent skill for creating detailed, interactive isometric illustrations of real-world machines and complex systems. Generates polished SVGs with optional WebGL shaders and 3D effects.
4. LOOP: ENTRADA → anatomy → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/anatomy — descargado

## 105. difftastic
1. Nombre: difftastic (Wilfred/difftastic)
2. URL visible: https://github.com/Wilfred/difftastic
3. Micro resumen: Diff estructural que entiende sintaxis.
4. LOOP: OLD CODE + NEW CODE → PARSE → STRUCTURAL DIFF → CHANGESET
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/difftastic — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 106. AFlow_
1. Nombre: AFlow_ (XiangJinyu/AFlow_)
2. URL visible: https://github.com/XiangJinyu/AFlow_
3. Micro resumen: Búsqueda y optimización automática de workflows agentic.
4. LOOP: WORKFLOW CANDIDATE → EXECUTE/EVAL → SEARCH → NEW WORKFLOW → SCORE ↺
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/AFlow_ — movido desde los 115

## 107. zera-agent
1. Nombre: zera-agent (younatics/zera-agent)
2. URL visible: https://github.com/younatics/zera-agent
3. Micro resumen: ZERA: Zero-init Instruction Evolving Refinement Agent - From Zero Instructions to Structured Prompts via Principle-based Optimization
4. LOOP: ENTRADA → zera-agent → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/zera-agent — descargado

## 108. z3
1. Nombre: z3 (Z3Prover/z3)
2. URL visible: https://github.com/Z3Prover/z3
3. Micro resumen: Solver SMT. Puede funcionar como Sheriff matemático de permisos, restricciones e incompatibilidades.
4. LOOP: RESTRICCIONES → SOLVER → SAT / UNSAT → PERMITIR / BLOQUEAR
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/z3 — movido desde los 115 · completo (archivos faltantes recuperados desde _archives con motor_1)

## 109. CoEvoSkills
1. Nombre: CoEvoSkills (Zhang-Henry/CoEvoSkills)
2. URL visible: https://github.com/Zhang-Henry/CoEvoSkills
3. Micro resumen: Evolución/generación y comprobación de skills.
4. LOOP: EXPERIENCE → SKILL CANDIDATE → VERIFY → EVOLVE → ACCEPT
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/CoEvoSkills — movido desde los 115

## 110. GPTCache
1. Nombre: GPTCache (zilliztech/GPTCache)
2. URL visible: https://github.com/zilliztech/GPTCache
3. Micro resumen: Semantic cache for LLMs. Fully integrated with LangChain and llama_index.
4. LOOP: ENTRADA → GPTCache → PROCESO → SALIDA VERIFICADA → CORE YAIWES
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/GPTCache — descargado · completo (archivos faltantes recuperados desde _archives con motor_1)

# Lista 2 (t130u) — percepción, agentes visuales y simulación

## 111. browser-use
1. Nombre: Browser Use (browser-use/browser-use)
2. URL visible: https://github.com/browser-use/browser-use
3. Micro resumen: Browser Use — componente de la lista 2 (t130u).
4. LOOP: Pantalla/Web → Agente visual → Detectar estado/elementos → Razonar acción → Click/Escribir/Navegar → Observar nuevo estado → Repetir tarea
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/browser-use — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos); .gitattributes eliminado (solo tenía reglas LFS)

## 112. screenshot-to-code
1. Nombre: Screenshot-to-Code (abi/screenshot-to-code)
2. URL visible: https://github.com/abi/screenshot-to-code
3. Micro resumen: Screenshot-to-Code — componente de la lista 2 (t130u).
4. LOOP: Imagen UI → Visión LLM → Descomponer componentes → Inferir layout → Generar código → Renderizar → Comparar visualmente → Corregir → Réplica
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/screenshot-to-code — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos)

## 113. OpenAdapt
1. Nombre: OpenAdapt (OpenAdaptAI/OpenAdapt)
2. URL visible: https://github.com/OpenAdaptAI/OpenAdapt
3. Micro resumen: OpenAdapt — componente de la lista 2 (t130u).
4. LOOP: Humano ejecuta tarea → Capturar pantalla+acciones → Extraer secuencia → Compilar workflow → Verificar estados → Guardar conocimiento → Ejecutar nuevamente
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/OpenAdapt — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos)

## 114. claude-skills
1. Nombre: Screenshot-to-Code Skill (OneWave-AI/claude-skills)
2. URL visible: https://github.com/OneWave-AI/claude-skills
3. Micro resumen: Screenshot-to-Code Skill — componente de la lista 2 (t130u).
4. LOOP: Screenshot → Claude Code → Screenshot-to-Code Skill → Detectar estructura visual → Generar componentes → HTML/CSS/React/Vue → Render → Comparación → Ajuste
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/claude-skills — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos); el engine no admite subcarpetas → repo completo; la skill está en `code/screenshot-to-code/`

## 115. inner-coordinates
1. Nombre: Inner Coordinates (XiaoChu-1208/inner-coordinates)
2. URL visible: https://github.com/XiaoChu-1208/inner-coordinates
3. Micro resumen: Inner Coordinates — componente de la lista 2 (t130u).
4. LOOP: Humano/Agente demuestra tarea → Capturar frames+clicks → Identificar pantallas → Pantalla=NODE → Acción=EDGE → Crear mapa del workflow → Guardarlo → Ejecutarlo desde memoria → Verificar → Auto-corregir mapa
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/inner-coordinates — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos)

## 116. android_world
1. Nombre: AndroidWorld (google-research/android_world)
2. URL visible: https://github.com/google-research/android_world
3. Micro resumen: AndroidWorld — componente de la lista 2 (t130u).
4. LOOP: Objetivo → AndroidWorld → Ver Android → Interpretar pantalla → Touch/Texto → Aplicación responde → Verificar → Continuar
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/android_world — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos)

## 117. android_env
1. Nombre: AndroidEnv (google-deepmind/android_env)
2. URL visible: https://github.com/google-deepmind/android_env
3. Micro resumen: AndroidEnv — componente de la lista 2 (t130u).
4. LOOP: Android → Pixels → Agente AI → Acción Touch → Resultado → Reward → Aprendizaje → Nueva acción
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/android_env — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos)

## 118. genesis-world
1. Nombre: Genesis World (Genesis-Embodied-AI/genesis-world)
2. URL visible: https://github.com/Genesis-Embodied-AI/genesis-world
3. Micro resumen: Genesis World — componente de la lista 2 (t130u).
4. LOOP: Descripción/escenario → Genesis → Mundo físico → Objetos + física + sensores → Agente AI → Simulación → Resultado → Aprendizaje
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/genesis-world — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos); nombre real verificado: Genesis-Embodied-AI/Genesis → redirige a Genesis-Embodied-AI/genesis-world

## 119. mujoco
1. Nombre: MuJoCo (google-deepmind/mujoco)
2. URL visible: https://github.com/google-deepmind/mujoco
3. Micro resumen: MuJoCo — componente de la lista 2 (t130u).
4. LOOP: Mundo físico → MuJoCo → Simulación → Agente AI → Acción → Física → Resultado → Reward → Aprendizaje → Repetición
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/mujoco — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos)

## 120. dm_control
1. Nombre: dm_control (complemento MuJoCo) (google-deepmind/dm_control)
2. URL visible: https://github.com/google-deepmind/dm_control
3. Micro resumen: dm_control (complemento MuJoCo) — componente de la lista 2 (t130u).
4. LOOP: Mundo físico → MuJoCo → Simulación → Agente AI → Acción → Física → Resultado → Reward → Aprendizaje → Repetición
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/dm_control — descargado con motor_2 + engine; completado con motor_1 + motor_3 (archivos ignorados por .gitignore incluidos)

## 121. IsaacSim
1. Nombre: Isaac Sim (isaac-sim/IsaacSim)
2. URL visible: https://github.com/isaac-sim/IsaacSim
3. Micro resumen: Isaac Sim — componente de la lista 2 (t130u).
4. LOOP: Escenario → Isaac Sim → Física + sensores + robot → Agente AI → Acción → Simulación → Datos/Reward → Isaac Lab → Aprendizaje → Nueva política
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/IsaacSim — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · 1099 punteros LFS eliminados · reglas filter=lfs quitadas: .gitattributes (líneas filter=lfs quitadas)
<details><summary>Rutas LFS eliminadas (1099)</summary>

- `docs/readme/hero_shot_compressed.png`
- `docs/readme/isim_6.0_base_tut_gui_vs2022_winsdk_verify.png`
- `docs/readme/vs_modify.png`
- `source/deprecated/isaacsim.core.api/data/icon.png`
- `source/deprecated/isaacsim.core.api/data/preview.png`
- `source/deprecated/isaacsim.core.api/python/tests/data/cm_asset.usd`
- `source/deprecated/isaacsim.core.prims/data/icon.png`
- `source/deprecated/isaacsim.core.prims/data/preview.png`
- `source/deprecated/isaacsim.core.utils/data/icon.png`
- `source/deprecated/isaacsim.core.utils/data/preview.png`
- `source/deprecated/isaacsim.examples.extension/data/icon.png`
- `source/deprecated/isaacsim.examples.extension/data/preview.png`
- `source/deprecated/isaacsim.examples.extension/template_source_files/common/data/icon.png`
- `source/deprecated/isaacsim.examples.extension/template_source_files/common/data/preview.png`
- `source/deprecated/isaacsim.replicator.domain_randomization/data/icon.png`
- `source/deprecated/isaacsim.replicator.domain_randomization/data/preview.png`
- `source/deprecated/isaacsim.replicator.mobility_gen/data/icon.png`
- `source/deprecated/isaacsim.replicator.mobility_gen/data/preview.png`
- `source/deprecated/isaacsim.robot.experimental.manipulators.examples/data/icon.png`
- `source/deprecated/isaacsim.robot.experimental.manipulators.examples/data/preview.png`
- `source/deprecated/isaacsim.robot.manipulators/data/icon.png`
- `source/deprecated/isaacsim.robot.manipulators/data/preview.png`
- `source/deprecated/isaacsim.robot.manipulators.examples/data/icon.png`
- `source/deprecated/isaacsim.robot.manipulators.examples/data/preview.png`
- `source/deprecated/isaacsim.robot.manipulators.ui/data/icon.png`
- `source/deprecated/isaacsim.robot.manipulators.ui/data/preview.png`
- `source/deprecated/isaacsim.robot.wheeled_robots/data/icon.png`
- `source/deprecated/isaacsim.robot.wheeled_robots/data/preview.png`
- `source/deprecated/isaacsim.robot_motion.lula/data/icon.png`
- `source/deprecated/isaacsim.robot_motion.lula/data/preview.png`
- `source/deprecated/isaacsim.robot_motion.lula_test_widget/data/icon.png`
- `source/deprecated/isaacsim.robot_motion.lula_test_widget/data/preview.png`
- `source/deprecated/isaacsim.robot_motion.motion_generation/data/icon.png`
- `source/deprecated/isaacsim.robot_motion.motion_generation/data/preview.png`
- `source/deprecated/isaacsim.robot_motion.motion_generation.examples/data/icon.png`
- `source/deprecated/isaacsim.robot_motion.motion_generation.examples/data/preview.png`
- `source/deprecated/isaacsim.robot_setup.wizard/data/icon.png`
- `source/deprecated/isaacsim.robot_setup.wizard/data/preview.png`
- `source/deprecated/isaacsim.robot_setup.wizard/icons/add_robot.png`
- `source/deprecated/isaacsim.robot_setup.wizard/icons/define_robot.png`
- `source/deprecated/isaacsim.robot_setup.wizard/icons/drag_and_drop.png`
- `source/deprecated/isaacsim.robot_setup.wizard/icons/import_robot.png`
- `source/deprecated/isaacsim.sensors.camera/data/icon.png`
- `source/deprecated/isaacsim.sensors.camera/data/preview.png`
- `source/deprecated/isaacsim.sensors.camera/data/tests/nested_semantics.usd`
- `source/deprecated/isaacsim.sensors.camera/data/tests/test_rename_node_type.usda`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_pointcloud/debug_imgs/pointcloud_camera_frame_res_211_99_rgb.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_pointcloud/debug_imgs/pointcloud_camera_frame_res_4_4_rgb.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_pointcloud/debug_imgs/pointcloud_camera_frame_res_64_64_rgb.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_pointcloud/debug_imgs/pointcloud_camera_frame_res_67_137_rgb.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_pointcloud/debug_imgs/pointcloud_world_frame_res_211_99_rgb.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_pointcloud/debug_imgs/pointcloud_world_frame_res_4_4_rgb.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_pointcloud/debug_imgs/pointcloud_world_frame_res_64_64_rgb.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_pointcloud/debug_imgs/pointcloud_world_frame_res_67_137_rgb.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/batched_depth/camera_view_depth_batched_0.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/batched_depth/camera_view_depth_batched_1.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/batched_depth/camera_view_depth_batched_2.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/batched_depth/camera_view_depth_batched_3.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/batched_rgb/camera_view_rgb_batched_0.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/batched_rgb/camera_view_rgb_batched_1.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/batched_rgb/camera_view_rgb_batched_2.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/batched_rgb/camera_view_rgb_batched_3.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/tiled_depth/camera_view_depth_tiled.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/camera_view/tiled_rgb/camera_view_rgb_tiled.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/single_view_depth_sensor/depth_sensor_distance_annotator.png`
- `source/deprecated/isaacsim.sensors.camera/isaacsim/sensors/camera/tests/data/golden/single_view_depth_sensor/depth_sensor_distance_annotator_windows.png`
- `source/deprecated/isaacsim.sensors.physics/data/icon.png`
- `source/deprecated/isaacsim.sensors.physics/data/preview.png`
- `source/deprecated/isaacsim.sensors.physx/data/icon.png`
- `source/deprecated/isaacsim.sensors.physx/data/preview.png`
- `source/deprecated/isaacsim.sensors.physx.examples/data/icon.png`
- `source/deprecated/isaacsim.sensors.physx.examples/data/preview.png`
- `source/deprecated/isaacsim.sensors.physx.ui/data/icon.png`
- `source/deprecated/isaacsim.sensors.physx.ui/data/preview.png`
- `source/deprecated/isaacsim.sensors.rtx/data/icon.png`
- `source/deprecated/isaacsim.sensors.rtx/data/preview.png`
- `source/deprecated/isaacsim.util.merge_mesh/data/icon.png`
- `source/deprecated/isaacsim.util.merge_mesh/data/preview.png`
- `source/deprecated/omni.isaac.ml_archive/data/icon.png`
- `source/deprecated/omni.isaac.ml_archive/data/preview.png`
- `source/extensions/isaacsim.app.about/data/icon.png`
- `source/extensions/isaacsim.app.about/data/preview.png`
- `source/extensions/isaacsim.app.about/data/tests/golden_img/test_about_ui.png`
- `source/extensions/isaacsim.app.setup/data/icon.png`
- `source/extensions/isaacsim.app.setup/data/nvidia-omniverse-isaacsim.ico`
- `source/extensions/isaacsim.app.setup/data/omni.isaac.sim.png`
- `source/extensions/isaacsim.app.setup/data/preview.png`
- `source/extensions/isaacsim.asset.exporter.urdf/data/icon.png`
- `source/extensions/isaacsim.asset.exporter.urdf/data/preview.png`
- `source/extensions/isaacsim.asset.exporter.urdf.ui/data/icon.png`
- `source/extensions/isaacsim.asset.exporter.urdf.ui/data/preview.png`
- `source/extensions/isaacsim.asset.gen.conveyor/data/icon.png`
- `source/extensions/isaacsim.asset.gen.conveyor/data/preview.png`
- `source/extensions/isaacsim.asset.gen.conveyor.ui/data/icon.png`
- `source/extensions/isaacsim.asset.gen.conveyor.ui/data/preview.png`
- `source/extensions/isaacsim.asset.gen.omap/data/icon.png`
- `source/extensions/isaacsim.asset.gen.omap/data/preview.png`
- `source/extensions/isaacsim.asset.gen.omap.ui/data/icon.png`
- `source/extensions/isaacsim.asset.gen.omap.ui/data/preview.png`
- `source/extensions/isaacsim.asset.importer.heightmap/data/icon.png`
- `source/extensions/isaacsim.asset.importer.heightmap/data/preview.png`
- `source/extensions/isaacsim.asset.importer.heightmap/data/test/test_image.png`
- `source/extensions/isaacsim.asset.importer.mjcf/data/icon.png`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/F1.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/F2.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/F3.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/TH1_z.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/TH2_z.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/TH3_z.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/forearm_electric.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/forearm_electric_cvx.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/knuckle.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/lfmetacarpal.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/palm.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/stls/hand/wrist.stl`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/textures/block.png`
- `source/extensions/isaacsim.asset.importer.mjcf/data/mjcf/open_ai_assets/textures/block_hidden.png`
- `source/extensions/isaacsim.asset.importer.mjcf/data/preview.png`
- `source/extensions/isaacsim.asset.importer.mjcf.ui/data/icon.png`
- `source/extensions/isaacsim.asset.importer.mjcf.ui/data/preview.png`
- `source/extensions/isaacsim.asset.importer.mjcf.ui/icons/icoFileMJCF.png`
- `source/extensions/isaacsim.asset.importer.urdf/data/icon.png`
- `source/extensions/isaacsim.asset.importer.urdf/data/preview.png`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/carter/meshes/caster_wheel.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/carter/meshes/chassis.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/carter/meshes/pivot.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/carter/meshes/side_wheel.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/collision/J1.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/collision/J2.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/collision/J3.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/collision/J4.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/collision/J5.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/collision/J6.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/collision/base_link.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/visual/J1.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/visual/J2.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/visual/J3.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/visual/J4.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/visual/J5.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/visual/J6.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/cobotta_pro_900_visualization/meshes/visual/base_link.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/images/collision.png`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/images/visual.png`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/meshes/collision/base_link.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/meshes/collision/inner_finger.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/meshes/collision/inner_knuckle.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/meshes/collision/outer_knuckle.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/meshes/visual/base_link.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/meshes/visual/inner_finger.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/meshes/visual/inner_knuckle.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/cobotta_pro_900/onrobot_rg6_visualization/meshes/visual/outer_knuckle.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/finger.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/hand.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/link0.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/link1.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/link2.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/link3.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/link4.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/link5.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/link6.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/collision/link7.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/finger.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/hand.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/link0.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/link1.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/link2.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/link3.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/link4.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/link5.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/link6.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/franka_description/meshes/visual/link7.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/assembly_battery.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/axle.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/base.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/base_collision.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/mx12w.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/nano_chassis_base.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/nano_chassis_bridge.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/nano_chassis_rs_mount.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/pusher.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/realsense.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/shock_mount.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/kaya/meshes/wheel_and_rollers.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/ur10/meshes/ur10_base.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/ur10/meshes/ur10_forearm.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/ur10/meshes/ur10_shoulder.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/ur10/meshes/ur10_upper_arm.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/ur10/meshes/ur10_wrist_1.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/ur10/meshes/ur10_wrist_2.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/robots/ur10/meshes/ur10_wrist_3.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/tests/test_mtl/test_mtl.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/tests/test_mtl_stl/cube.stl`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/tests/test_textures_urdf/meshes/tex_cube.dae`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/tests/test_textures_urdf/meshes/tex_cube.obj`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/tests/test_textures_urdf/meshes/textures/base_color.png`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/tests/test_textures_urdf/meshes/textures/emission_map.png`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/tests/test_textures_urdf/meshes/textures/metallic_map.png`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/tests/test_textures_urdf/meshes/textures/normal_map.png`
- `source/extensions/isaacsim.asset.importer.urdf/data/urdf/tests/test_textures_urdf/meshes/textures/roughness_map.png`
- `source/extensions/isaacsim.asset.importer.urdf.ui/data/icon.png`
- `source/extensions/isaacsim.asset.importer.urdf.ui/data/preview.png`
- `source/extensions/isaacsim.asset.importer.urdf.ui/icons/icoFileURDF.png`
- `source/extensions/isaacsim.asset.importer.utils/data/icon.png`
- `source/extensions/isaacsim.asset.importer.utils/data/preview.png`
- `source/extensions/isaacsim.asset.transformer/data/icon.png`
- `source/extensions/isaacsim.asset.transformer/data/preview.png`
- `source/extensions/isaacsim.asset.transformer.rules/data/icon.png`
- `source/extensions/isaacsim.asset.transformer.rules/data/preview.png`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/Materials/Materials.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/backpack/configuration/g1_29dof_NVBP_base.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/backpack/configuration/g1_29dof_NVBP_physics.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/backpack/configuration/g1_29dof_NVBP_robot.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/backpack/configuration/g1_29dof_NVBP_sensor.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/backpack/g1_29dof_NVBP.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_29dof_with_hand_rev_1_0_base.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_29dof_with_hand_rev_1_0_physics.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_29dof_with_hand_rev_1_0_physics_simplified.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_29dof_with_hand_rev_1_0_robot.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_29dof_with_hand_rev_1_0_sensor.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_Gripper_three_finger_hand_physics_right.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_left_hand_inspire_left_physics.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_left_hand_three_finger_hand_physics_left.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_right_hand_inspire_right_physics.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/g1_right_hand_three_finger_hand_physics_right.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/inspire_hand/g1_29dof_rev_1_0_with_inspire_hand_retarget_inspire_white_physics.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/inspire_hand/inspire_left_base.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/inspire_hand/inspire_left_hand.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/inspire_hand/inspire_left_physics.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/inspire_hand/inspire_left_robot.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/inspire_hand/inspire_right_base.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/inspire_hand/inspire_right_hand.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/inspire_hand/inspire_right_physics.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/inspire_hand/inspire_right_robot.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/three_finger_hand/three_finger_hand_base_left.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/three_finger_hand/three_finger_hand_base_right.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/three_finger_hand/three_finger_hand_physics_left.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/three_finger_hand/three_finger_hand_physics_right.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/three_finger_hand/three_fingers_left_hand.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/three_finger_hand/three_fingers_left_hand_robot.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/three_finger_hand/three_fingers_right_hand.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/configuration/three_finger_hand/three_fingers_right_hand_robot.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/G1/g1.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/inspire_hand/Plastics/Rubber_Smooth/Rubber_Smooth_BaseColor.png`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/inspire_hand/Plastics/Rubber_Smooth/Rubber_Smooth_Normal.png`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/inspire_hand/Plastics/Rubber_Smooth/Rubber_Smooth_ORM.png`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/inspire_hand/inspire_hand_materials.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/test_advanced/usdex/test_advanced.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/test_collision_from_visuals/test_collision_from_visuals.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/test_prims/base.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/Robotiq_2F_140_base.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/Robotiq_2F_140_physics_edit.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/configuration/Robotiq_2F_140_robot.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/materials/materials.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/parts/Finger1_JFT.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/parts/Finger2_JFP.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/parts/Finger3_JFH.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/parts/Finger4_JFL.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/parts/Fingertip_JFD.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-140/parts/_F_Body_JFX.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/Robotiq_2F_85.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/payloads/Physics/None.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/payloads/Physics/Physics.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/payloads/Physics/Physx_Loop.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/payloads/Physics/Physx_Mimic.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/payloads/base.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/payloads/geometries.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/payloads/instances.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/payloads/materials.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/Robotiq/2F-85/payloads/robot.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/configuration/ur10e_Gripper_Robotiq_2F_140.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/configuration/ur10e_Gripper_Robotiq_2f_85.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/configuration/ur10e_base.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/configuration/ur10e_physics.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/configuration/ur10e_robot.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/configuration/ur10e_sensor.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e/ur10e.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/Gripper/None.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/Gripper/Robotiq_2F_140.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/Gripper/Robotiq_2F_85.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/Physics/None.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/Physics/physics.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/Physics/physx.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/Sensor/None.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/Sensor/Sensors.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/base.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/geometries.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/instances.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/materials.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_interface/payloads/robot.usda`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_shoulder/configuration/ur10e_base_defeatured.usd`
- `source/extensions/isaacsim.asset.transformer.rules/data/tests/ur10e_shoulder/ur10e.usda`
- `source/extensions/isaacsim.asset.transformer.ui/data/icon.png`
- `source/extensions/isaacsim.asset.transformer.ui/data/preview.png`
- `source/extensions/isaacsim.asset.validation/data/icon.png`
- `source/extensions/isaacsim.asset.validation/data/preview.png`
- `source/extensions/isaacsim.asset.validation.ui/data/icon.png`
- `source/extensions/isaacsim.asset.validation.ui/data/preview.png`
- `source/extensions/isaacsim.benchmark.services/data/icon.png`
- `source/extensions/isaacsim.benchmark.services/data/preview.png`
- `source/extensions/isaacsim.code_editor.jupyter/data/icon.png`
- `source/extensions/isaacsim.code_editor.jupyter/data/kernels/embedded_omniverse_python3_socket/logo-32x32.png`
- `source/extensions/isaacsim.code_editor.jupyter/data/kernels/embedded_omniverse_python3_socket/logo-64x64.png`
- `source/extensions/isaacsim.code_editor.jupyter/data/preview.png`
- `source/extensions/isaacsim.code_editor.python_server/data/icon.png`
- `source/extensions/isaacsim.code_editor.python_server/data/preview.png`
- `source/extensions/isaacsim.code_editor.python_server.ui/data/icon.png`
- `source/extensions/isaacsim.code_editor.python_server.ui/data/preview.png`
- `source/extensions/isaacsim.code_editor.vscode/data/icon.png`
- `source/extensions/isaacsim.code_editor.vscode/data/preview.png`
- `source/extensions/isaacsim.common/data/icon.png`
- `source/extensions/isaacsim.common/data/preview.png`
- `source/extensions/isaacsim.core.cloner/data/icon.png`
- `source/extensions/isaacsim.core.cloner/data/preview.png`
- `source/extensions/isaacsim.core.cloner/python/tests/data/quatf_d.usda`
- `source/extensions/isaacsim.core.deprecation_manager/data/icon.png`
- `source/extensions/isaacsim.core.deprecation_manager/data/preview.png`
- `source/extensions/isaacsim.core.experimental.actuators/data/icon.png`
- `source/extensions/isaacsim.core.experimental.actuators/data/preview.png`
- `source/extensions/isaacsim.core.experimental.materials/data/icon.png`
- `source/extensions/isaacsim.core.experimental.materials/data/preview.png`
- `source/extensions/isaacsim.core.experimental.objects/data/icon.png`
- `source/extensions/isaacsim.core.experimental.objects/data/preview.png`
- `source/extensions/isaacsim.core.experimental.objects/data/templates/wireframe-blue.png`
- `source/extensions/isaacsim.core.experimental.primdata/data/icon.png`
- `source/extensions/isaacsim.core.experimental.primdata/data/preview.png`
- `source/extensions/isaacsim.core.experimental.prims/data/icon.png`
- `source/extensions/isaacsim.core.experimental.prims/data/preview.png`
- `source/extensions/isaacsim.core.experimental.utils/data/icon.png`
- `source/extensions/isaacsim.core.experimental.utils/data/preview.png`
- `source/extensions/isaacsim.core.includes/data/icon.png`
- `source/extensions/isaacsim.core.includes/data/preview.png`
- `source/extensions/isaacsim.core.nodes/data/icon.png`
- `source/extensions/isaacsim.core.nodes/data/preview.png`
- `source/extensions/isaacsim.core.nodes/python/tests/data/golden/attach_hydra_texture/rgb/attach_hydra_texture_rgb.png`
- `source/extensions/isaacsim.core.rendering_manager/data/icon.png`
- `source/extensions/isaacsim.core.rendering_manager/data/preview.png`
- `source/extensions/isaacsim.core.simulation_manager/data/icon.png`
- `source/extensions/isaacsim.core.simulation_manager/data/preview.png`
- `source/extensions/isaacsim.core.throttling/data/icon.png`
- `source/extensions/isaacsim.core.throttling/data/preview.png`
- `source/extensions/isaacsim.core.version/data/icon.png`
- `source/extensions/isaacsim.core.version/data/preview.png`
- `source/extensions/isaacsim.examples.base/data/icon.png`
- `source/extensions/isaacsim.examples.base/data/preview.png`
- `source/extensions/isaacsim.examples.browser/data/icon.png`
- `source/extensions/isaacsim.examples.browser/data/preview.png`
- `source/extensions/isaacsim.examples.interactive/data/SurfaceGripper_gantry.usda`
- `source/extensions/isaacsim.examples.interactive/data/icon.png`
- `source/extensions/isaacsim.examples.interactive/data/preview.png`
- `source/extensions/isaacsim.examples.ipc/data/icon.png`
- `source/extensions/isaacsim.examples.ipc/data/preview.png`
- `source/extensions/isaacsim.examples.ui/data/icon.png`
- `source/extensions/isaacsim.examples.ui/data/preview.png`
- `source/extensions/isaacsim.gui.components/data/icon.png`
- `source/extensions/isaacsim.gui.components/data/preview.png`
- `source/extensions/isaacsim.gui.content_browser/data/icon.png`
- `source/extensions/isaacsim.gui.content_browser/data/preview.png`
- `source/extensions/isaacsim.gui.menu/data/icon.png`
- `source/extensions/isaacsim.gui.menu/data/preview.png`
- `source/extensions/isaacsim.gui.property/data/icon.png`
- `source/extensions/isaacsim.gui.property/data/preview.png`
- `source/extensions/isaacsim.gui.sensors.icon/data/icon.png`
- `source/extensions/isaacsim.gui.sensors.icon/data/preview.png`
- `source/extensions/isaacsim.gui.sensors.icon/data/tests/golden_img/legacy/prim_icon.png`
- `source/extensions/isaacsim.gui.sensors.icon/data/tests/golden_img/prim_icon.png`
- `source/extensions/isaacsim.gui.sensors.icon/data/tests/primicon.png`
- `source/extensions/isaacsim.hsb.bridge/data/icon.png`
- `source/extensions/isaacsim.hsb.bridge/data/preview.png`
- `source/extensions/isaacsim.hsb.core/data/icon.png`
- `source/extensions/isaacsim.hsb.core/data/preview.png`
- `source/extensions/isaacsim.hsb.nodes/data/icon.png`
- `source/extensions/isaacsim.hsb.nodes/data/preview.png`
- `source/extensions/isaacsim.physics.newton/data/icon.png`
- `source/extensions/isaacsim.physics.newton/data/preview.png`
- `source/extensions/isaacsim.physics.newton.tensors/data/icon.png`
- `source/extensions/isaacsim.physics.newton.tensors/data/usd/Ant.usda`
- `source/extensions/isaacsim.physics.newton.tensors/data/usd/CartPole.usda`
- `source/extensions/isaacsim.physics.newton.tensors/data/usd/Franka.usda`
- `source/extensions/isaacsim.physics.newton.tensors/data/usd/Humanoid.usda`
- `source/extensions/isaacsim.physics.newton.ui/data/icon.png`
- `source/extensions/isaacsim.physics.newton.ui/data/preview.png`
- `source/extensions/isaacsim.pip.newton/data/icon.png`
- `source/extensions/isaacsim.pip.newton/data/preview.png`
- `source/extensions/isaacsim.pip.nv/data/icon.png`
- `source/extensions/isaacsim.pip.nv/data/preview.png`
- `source/extensions/isaacsim.pip.onnx/data/icon.png`
- `source/extensions/isaacsim.pip.onnx/data/preview.png`
- `source/extensions/isaacsim.replicator.behavior/data/icon.png`
- `source/extensions/isaacsim.replicator.behavior/data/preview.png`
- `source/extensions/isaacsim.replicator.behavior/isaacsim/replicator/behavior/tests/data/golden/_out_behaviors_sdg/distance_to_image_plane_0000.png`
- `source/extensions/isaacsim.replicator.behavior/isaacsim/replicator/behavior/tests/data/golden/_out_behaviors_sdg/distance_to_image_plane_0001.png`
- `source/extensions/isaacsim.replicator.behavior/isaacsim/replicator/behavior/tests/data/golden/_out_behaviors_sdg/distance_to_image_plane_0002.png`
- `source/extensions/isaacsim.replicator.behavior/isaacsim/replicator/behavior/tests/data/golden/_out_behaviors_sdg/distance_to_image_plane_0003.png`
- `source/extensions/isaacsim.replicator.behavior/isaacsim/replicator/behavior/tests/data/golden/_out_behaviors_sdg/rgb_0000.png`
- `source/extensions/isaacsim.replicator.behavior/isaacsim/replicator/behavior/tests/data/golden/_out_behaviors_sdg/rgb_0001.png`
- `source/extensions/isaacsim.replicator.behavior/isaacsim/replicator/behavior/tests/data/golden/_out_behaviors_sdg/rgb_0002.png`
- `source/extensions/isaacsim.replicator.behavior/isaacsim/replicator/behavior/tests/data/golden/_out_behaviors_sdg/rgb_0003.png`
- `source/extensions/isaacsim.replicator.behavior.ui/data/icon.png`
- `source/extensions/isaacsim.replicator.behavior.ui/data/preview.png`
- `source/extensions/isaacsim.replicator.episode_recorder/data/icon.png`
- `source/extensions/isaacsim.replicator.episode_recorder/data/preview.png`
- `source/extensions/isaacsim.replicator.episode_recorder.ui/data/icon.png`
- `source/extensions/isaacsim.replicator.episode_recorder.ui/data/preview.png`
- `source/extensions/isaacsim.replicator.examples/data/icon.png`
- `source/extensions/isaacsim.replicator.examples/data/preview.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_numpy/annot_depth_1_0.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_numpy/annot_depth_1_1.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_numpy/annot_depth_2_0.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_numpy/annot_depth_2_1.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_numpy/annot_rgb_0.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_numpy/annot_rgb_1.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_warp/annot_depth_1_0.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_warp/annot_depth_1_1.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_warp/annot_depth_2_0.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_warp/annot_depth_2_1.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_warp/annot_rgb_0.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_annot_warp/annot_rgb_1.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_writer_numpy/distance_to_camera_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_writer_numpy/distance_to_camera_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_writer_numpy/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_writer_numpy/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_writer_warp/distance_to_camera_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_writer_warp/distance_to_camera_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_writer_warp/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_augm_writer_warp/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_box_stacking_env_none/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_box_stacking_env_warehouse/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/depth/depth_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/depth/depth_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/depth/depth_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/edges/edges_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/edges/edges_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/edges/edges_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/segmentation/segmentation_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/segmentation/segmentation_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/segmentation/segmentation_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/shaded_seg/shaded_seg_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/shaded_seg/shaded_seg_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_simple/clip_0000/shaded_seg/shaded_seg_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0000/depth/depth_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0000/depth/depth_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0000/depth/depth_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0000/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0000/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0000/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0001/depth/depth_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0001/depth/depth_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0001/depth/depth_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0001/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0001/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_cosmos_warehouse/clip_0001/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_deformable_drop/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_deformable_drop/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_deformable_drop/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_deformable_drop/rgb_0003.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_0.0042_pt_subsamples_4_spp_32/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_0.0042_pt_subsamples_4_spp_32/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_0.0042_pt_subsamples_4_spp_32/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_0.0042_rt/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_0.0042_rt/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_0.0042_rt/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_None_pt_subsamples_4_spp_32/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_None_pt_subsamples_4_spp_32/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_None_pt_subsamples_4_spp_32/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_None_rt/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_None_rt/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_motion_blur/_out_motion_blur_func_dt_None_rt/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_nav_sdg_demo/left_sensor/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_nav_sdg_demo/left_sensor/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_nav_sdg_demo/right_sensor/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_nav_sdg_demo/right_sensor/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_obj_based_sdg_pose_writer/cam_0/000000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_obj_based_sdg_pose_writer/cam_0/000001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_obj_based_sdg_pose_writer/cam_0/000002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_obj_based_sdg_pose_writer/cam_0/000003.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_obj_based_sdg_pose_writer/cam_1/000000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_obj_based_sdg_pose_writer/cam_1/000001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_obj_based_sdg_pose_writer/cam_1/000002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_obj_based_sdg_pose_writer/cam_1/000003.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/distance_to_camera_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/distance_to_camera_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/distance_to_camera_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/distance_to_camera_0003.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/rgb_0003.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/semantic_segmentation_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/semantic_segmentation_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/semantic_segmentation_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_object_reconstruction_assets_drop/semantic_segmentation_0003.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_lights/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_lights/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_lights/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_sphere_scan/PerspView/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_sphere_scan/PerspView/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_sphere_scan/PerspView/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_sphere_scan/SphereView/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_sphere_scan/SphereView/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_sphere_scan/SphereView/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_textures/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_textures/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_rand_textures/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/DriverView/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/DriverView/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/DriverView/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/DriverView/rgb/rgb_0003.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/PalletView/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/PalletView/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/PalletView/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/PalletView/rgb/rgb_0003.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/TopView/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/TopView/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/TopView/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_scene_based_sdg/TopView/rgb/rgb_0003.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_simready_assets/rgb_0000.png`
- `source/extensions/isaacsim.replicator.examples/python/tests/data/golden/_out_simready_assets/rgb_0001.png`
- `source/extensions/isaacsim.replicator.experimental.domain_randomization/data/icon.png`
- `source/extensions/isaacsim.replicator.experimental.domain_randomization/data/preview.png`
- `source/extensions/isaacsim.replicator.experimental.mobility_gen/data/icon.png`
- `source/extensions/isaacsim.replicator.experimental.mobility_gen/data/preview.png`
- `source/extensions/isaacsim.replicator.grasping/data/icon.png`
- `source/extensions/isaacsim.replicator.grasping/data/preview.png`
- `source/extensions/isaacsim.replicator.grasping.ui/data/icon.png`
- `source/extensions/isaacsim.replicator.grasping.ui/data/preview.png`
- `source/extensions/isaacsim.replicator.mobility_gen.examples/data/icon.png`
- `source/extensions/isaacsim.replicator.mobility_gen.examples/data/preview.png`
- `source/extensions/isaacsim.replicator.mobility_gen.ui/data/docs_images/startup_preview.png`
- `source/extensions/isaacsim.replicator.mobility_gen.ui/data/icon.png`
- `source/extensions/isaacsim.replicator.mobility_gen.ui/data/preview.png`
- `source/extensions/isaacsim.replicator.nurec_utils/data/icon.png`
- `source/extensions/isaacsim.replicator.nurec_utils/data/preview.png`
- `source/extensions/isaacsim.replicator.synthetic_recorder/data/icon.png`
- `source/extensions/isaacsim.replicator.synthetic_recorder/data/preview.png`
- `source/extensions/isaacsim.replicator.teleop/data/icon.png`
- `source/extensions/isaacsim.replicator.teleop/data/preview.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm/rgb_0000.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm/rgb_0001.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm/rgb_0002.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm/rgb_0003.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm/rgb_0004.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0003.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0004.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0003.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_floating_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0004.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0003.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_dex3_view_cam/rgb/rgb_0004.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0000.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0001.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0002.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0003.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_dual_ur3_xarm_dex3/rp_xarm_view_cam/rgb/rgb_0004.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_solo_ur3_xarm/rgb_0000.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_solo_ur3_xarm/rgb_0001.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_solo_ur3_xarm/rgb_0002.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_solo_ur3_xarm/rgb_0003.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_ik_solo_ur3_xarm/rgb_0004.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/Right_right_hand_palm_link_TCPCameraSide/rgb_after_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/Right_right_hand_palm_link_TCPCameraSide/rgb_after_lift.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/Right_right_hand_palm_link_TCPCameraSide/rgb_after_place.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/Right_right_hand_palm_link_TCPCameraSide/rgb_before_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/Right_right_hand_palm_link_TCPCameraTop/rgb_after_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/Right_right_hand_palm_link_TCPCameraTop/rgb_after_lift.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/Right_right_hand_palm_link_TCPCameraTop/rgb_after_place.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/Right_right_hand_palm_link_TCPCameraTop/rgb_before_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/scene_top/rgb_after_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/scene_top/rgb_after_lift.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/scene_top/rgb_after_place.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_dex3/scene_top/rgb_before_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/Right_xarm_gripper_base_link_TCPCameraSide/rgb_after_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/Right_xarm_gripper_base_link_TCPCameraSide/rgb_after_lift.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/Right_xarm_gripper_base_link_TCPCameraSide/rgb_after_place.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/Right_xarm_gripper_base_link_TCPCameraSide/rgb_before_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/Right_xarm_gripper_base_link_TCPCameraTop/rgb_after_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/Right_xarm_gripper_base_link_TCPCameraTop/rgb_after_lift.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/Right_xarm_gripper_base_link_TCPCameraTop/rgb_after_place.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/Right_xarm_gripper_base_link_TCPCameraTop/rgb_before_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/scene_top/rgb_after_grasp.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/scene_top/rgb_after_lift.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/scene_top/rgb_after_place.png`
- `source/extensions/isaacsim.replicator.teleop/isaacsim/replicator/teleop/tests/data/_out_teleop_script_editor_xarm/scene_top/rgb_before_grasp.png`
- `source/extensions/isaacsim.replicator.teleop.ui/data/icon.png`
- `source/extensions/isaacsim.replicator.teleop.ui/data/preview.png`
- `source/extensions/isaacsim.replicator.writers/data/icon.png`
- `source/extensions/isaacsim.replicator.writers/data/preview.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_fisheyePolynomial/rp1/000000.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_fisheyePolynomial/rp1/000000_overlay.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_fisheyePolynomial/rp2/000000.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_fisheyePolynomial/rp2/000000_overlay.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_generalizedProjection/rp1/000000.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_generalizedProjection/rp1/000000_overlay.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_generalizedProjection/rp2/000000.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_generalizedProjection/rp2/000000_overlay.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_pinhole/rp1/000000.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_pinhole/rp1/000000_overlay.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_pinhole/rp2/000000.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_pinhole/rp2/000000_overlay.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_pinholeOpenCV/rp1/000000.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_pinholeOpenCV/rp1/000000_overlay.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_pinholeOpenCV/rp2/000000.png`
- `source/extensions/isaacsim.replicator.writers/python/tests/data/golden/_out_test_pose_writer_pinholeOpenCV/rp2/000000_overlay.png`
- `source/extensions/isaacsim.robot.experimental.wheeled_robots/data/icon.png`
- `source/extensions/isaacsim.robot.experimental.wheeled_robots/data/preview.png`
- `source/extensions/isaacsim.robot.policy.examples/data/icon.png`
- `source/extensions/isaacsim.robot.policy.examples/data/preview.png`
- `source/extensions/isaacsim.robot.poser/data/icon.png`
- `source/extensions/isaacsim.robot.poser/data/preview.png`
- `source/extensions/isaacsim.robot.poser.ui/data/icon.png`
- `source/extensions/isaacsim.robot.poser.ui/data/preview.png`
- `source/extensions/isaacsim.robot.schema/data/icon.png`
- `source/extensions/isaacsim.robot.schema/data/preview.png`
- `source/extensions/isaacsim.robot.schema.ui/data/icon.png`
- `source/extensions/isaacsim.robot.schema.ui/data/preview.png`
- `source/extensions/isaacsim.robot.surface_gripper/data/SurfaceGripper_gantry.usda`
- `source/extensions/isaacsim.robot.surface_gripper/data/icon.png`
- `source/extensions/isaacsim.robot.surface_gripper/data/preview.png`
- `source/extensions/isaacsim.robot.surface_gripper.ui/data/icon.png`
- `source/extensions/isaacsim.robot.surface_gripper.ui/data/preview.png`
- `source/extensions/isaacsim.robot.wheeled_robots.nodes/data/icon.png`
- `source/extensions/isaacsim.robot.wheeled_robots.nodes/data/preview.png`
- `source/extensions/isaacsim.robot.wheeled_robots.ui/data/icon.png`
- `source/extensions/isaacsim.robot.wheeled_robots.ui/data/preview.png`
- `source/extensions/isaacsim.robot_motion.controllers/data/icon.png`
- `source/extensions/isaacsim.robot_motion.controllers/data/preview.png`
- `source/extensions/isaacsim.robot_motion.cumotion/data/icon.png`
- `source/extensions/isaacsim.robot_motion.cumotion/data/preview.png`
- `source/extensions/isaacsim.robot_motion.cumotion.examples/data/icon.png`
- `source/extensions/isaacsim.robot_motion.cumotion.examples/data/preview.png`
- `source/extensions/isaacsim.robot_motion.examples/data/icon.png`
- `source/extensions/isaacsim.robot_motion.examples/data/preview.png`
- `source/extensions/isaacsim.robot_motion.experimental.motion_generation/data/icon.png`
- `source/extensions/isaacsim.robot_motion.experimental.motion_generation/data/preview.png`
- `source/extensions/isaacsim.robot_motion.pink/data/icon.png`
- `source/extensions/isaacsim.robot_motion.pink/data/preview.png`
- `source/extensions/isaacsim.robot_motion.pink.examples/data/icon.png`
- `source/extensions/isaacsim.robot_motion.pink.examples/data/preview.png`
- `source/extensions/isaacsim.robot_motion.schema/data/icon.png`
- `source/extensions/isaacsim.robot_motion.schema/data/preview.png`
- `source/extensions/isaacsim.robot_setup.assembler/data/icon.png`
- `source/extensions/isaacsim.robot_setup.assembler/data/preview.png`
- `source/extensions/isaacsim.robot_setup.collision_detector/data/icon.png`
- `source/extensions/isaacsim.robot_setup.collision_detector/data/preview.png`
- `source/extensions/isaacsim.robot_setup.gain_tuner/data/icon.png`
- `source/extensions/isaacsim.robot_setup.gain_tuner/data/preview.png`
- `source/extensions/isaacsim.robot_setup.gain_tuner.ui/data/icon.png`
- `source/extensions/isaacsim.robot_setup.gain_tuner.ui/data/preview.png`
- `source/extensions/isaacsim.robot_setup.grasp_editor/data/icon.png`
- `source/extensions/isaacsim.robot_setup.grasp_editor/data/preview.png`
- `source/extensions/isaacsim.robot_setup.sysid/data/icon.png`
- `source/extensions/isaacsim.robot_setup.sysid/data/preview.png`
- `source/extensions/isaacsim.robot_setup.sysid/data/scenes/benchtop_force.usda`
- `source/extensions/isaacsim.robot_setup.sysid/data/scenes/contact_probing.usda`
- `source/extensions/isaacsim.robot_setup.sysid/data/scenes/free_space.usda`
- `source/extensions/isaacsim.robot_setup.sysid/data/scenes/gravity_comp.usda`
- `source/extensions/isaacsim.robot_setup.sysid.ui/data/icon.png`
- `source/extensions/isaacsim.robot_setup.sysid.ui/data/preview.png`
- `source/extensions/isaacsim.robot_setup.virtual_gantry/data/icon.png`
- `source/extensions/isaacsim.robot_setup.virtual_gantry/data/preview.png`
- `source/extensions/isaacsim.robot_setup.virtual_gantry.ui/data/icon.png`
- `source/extensions/isaacsim.robot_setup.virtual_gantry.ui/data/preview.png`
- `source/extensions/isaacsim.robot_setup.virtual_gantry_schema/data/icon.png`
- `source/extensions/isaacsim.robot_setup.virtual_gantry_schema/data/preview.png`
- `source/extensions/isaacsim.robot_setup.xrdf_editor/data/icon.png`
- `source/extensions/isaacsim.robot_setup.xrdf_editor/data/preview.png`
- `source/extensions/isaacsim.ros2.bridge/data/icon.png`
- `source/extensions/isaacsim.ros2.bridge/data/preview.png`
- `source/extensions/isaacsim.ros2.control/data/icon.png`
- `source/extensions/isaacsim.ros2.control/data/preview.png`
- `source/extensions/isaacsim.ros2.core/data/icon.png`
- `source/extensions/isaacsim.ros2.core/data/preview.png`
- `source/extensions/isaacsim.ros2.examples/data/icon.png`
- `source/extensions/isaacsim.ros2.examples/data/preview.png`
- `source/extensions/isaacsim.ros2.nodes/data/icon.png`
- `source/extensions/isaacsim.ros2.nodes/data/preview.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/nova_carter_warehouse_front_stereo_left_rgb.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_0_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_0_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_120_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_120_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_150_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_150_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_180_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_180_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_210_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_210_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_240_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_240_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_270_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_270_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_300_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_300_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_30_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_30_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_330_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_330_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_60_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_60_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_90_camera_1.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/angle_90_camera_2.png`
- `source/extensions/isaacsim.ros2.nodes/python/tests/data/golden/spinning_camera/spinning_camera_scene.usda`
- `source/extensions/isaacsim.ros2.sim_control/data/icon.png`
- `source/extensions/isaacsim.ros2.sim_control/data/preview.png`
- `source/extensions/isaacsim.ros2.tf_viewer/data/icon.png`
- `source/extensions/isaacsim.ros2.tf_viewer/data/preview.png`
- `source/extensions/isaacsim.ros2.ui/data/icon.png`
- `source/extensions/isaacsim.ros2.ui/data/preview.png`
- `source/extensions/isaacsim.ros2.urdf/data/icon.png`
- `source/extensions/isaacsim.ros2.urdf/data/preview.png`
- `source/extensions/isaacsim.sensors.camera.ui/data/icon.png`
- `source/extensions/isaacsim.sensors.camera.ui/data/preview.png`
- `source/extensions/isaacsim.sensors.experimental.physics/data/icon.png`
- `source/extensions/isaacsim.sensors.experimental.physics/data/preview.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/data/icon.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/data/preview.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/data/spg/golden/grayscale.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/data/spg/golden/grayscale_invert.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/data/spg/scene/cornell_box.usda`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output/oak_d_tof__camera_pseudo_depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output/oak_d_tof__camera_pseudo_depth_tof_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/oak4_d__camera_pseudo_depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/oak4_d_wide__camera_pseudo_depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/oak_d_pro_poe__camera_pseudo_depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/oak_d_pro_w_poe__camera_pseudo_depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/oak_d_tof__camera_pseudo_depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/oak_d_tof__camera_pseudo_depth_tof_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/orbbec_femtomega_v1_0__camera_tof_wfov_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/orbbec_gemini2_v1_0__stream_depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/orbbec_gemini_335__stream_ir_left_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/orbbec_gemini_335l__camera_depth_left_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/rsd455__camera_pseudo_depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/rsd457__depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/rsd555__depth_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/sick_safevisionary2__depthcamera_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/sick_visionary_t_mini__depthcamera_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/golden/depth_sensor_output_zero_sigma/zed_x__cameraleft_rp.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_00.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_01.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_02.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_03.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_04.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_05.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_06.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_07.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_08.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_09.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_10.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_11.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_12.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_13.png`
- `source/extensions/isaacsim.sensors.experimental.rtx/python/tests/data/structured_light_camera/patterns/image_14.png`
- `source/extensions/isaacsim.sensors.physics.examples/data/icon.png`
- `source/extensions/isaacsim.sensors.physics.examples/data/preview.png`
- `source/extensions/isaacsim.sensors.physics.nodes/data/icon.png`
- `source/extensions/isaacsim.sensors.physics.nodes/data/preview.png`
- `source/extensions/isaacsim.sensors.physics.ui/data/icon.png`
- `source/extensions/isaacsim.sensors.physics.ui/data/preview.png`
- `source/extensions/isaacsim.sensors.rtx.nodes/data/icon.png`
- `source/extensions/isaacsim.sensors.rtx.nodes/data/preview.png`
- `source/extensions/isaacsim.sensors.rtx.ui/data/icon.png`
- `source/extensions/isaacsim.sensors.rtx.ui/data/preview.png`
- `source/extensions/isaacsim.simulation_app/data/icon.png`
- `source/extensions/isaacsim.simulation_app/data/omni.isaac.sim.png`
- `source/extensions/isaacsim.simulation_app/data/preview.png`
- `source/extensions/isaacsim.storage.native/data/icon.png`
- `source/extensions/isaacsim.storage.native/data/preview.png`
- `source/extensions/isaacsim.streaming.rtsp/data/icon.png`
- `source/extensions/isaacsim.streaming.rtsp/data/preview.png`
- `source/extensions/isaacsim.test.action_event_sdg/data/icon.png`
- `source/extensions/isaacsim.test.action_event_sdg/data/preview.png`
- `source/extensions/isaacsim.test.collection/data/icon.png`
- `source/extensions/isaacsim.test.collection/data/preview.png`
- `source/extensions/isaacsim.test.collection/data/tests/articulation_drives_opposite.usd`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Black Grid.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Curved Grid.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Flat Grid.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Full Warehouse.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Hospital.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Jetracer Track.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Office.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Simple Room.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Small Warehouse Digital Twin.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Small Warehouse With Forklifts.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Small Warehouse With Multiple Shelves.png`
- `source/extensions/isaacsim.test.collection/data/tests/golden_img/Small Warehouse.png`
- `source/extensions/isaacsim.test.collection/data/tests/test_mtl/test_mtl.obj`
- `source/extensions/isaacsim.test.docstring/data/icon.png`
- `source/extensions/isaacsim.test.docstring/data/preview.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_capture/distance_to_camera_auto_scaled_8bit.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_capture/distance_to_camera_manual_scaled_8bit.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_capture/rgb_data.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/different_extension_rgb_2.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/different_resolution_rgb_1.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/different_resolution_rgb_2.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_depth_8bit_1.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_depth_8bit_2.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_forklift_rt1.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_forklift_rt16.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_forklift_rt2.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_forklift_rt4.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_forklift_rt64.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_forklift_rt8.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_rotated_drill_1.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_rotated_drill_2.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_semantic_segmentation_1.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_semantic_segmentation_2.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_shifted_warehouse_1.png`
- `source/extensions/isaacsim.test.utils/data/golden/image_comparison/similar_rgb_shifted_warehouse_2.png`
- `source/extensions/isaacsim.test.utils/data/icon.png`
- `source/extensions/isaacsim.test.utils/data/preview.png`
- `source/extensions/isaacsim.ucx.bridge/data/icon.png`
- `source/extensions/isaacsim.ucx.bridge/data/preview.png`
- `source/extensions/isaacsim.ucx.core/data/icon.png`
- `source/extensions/isaacsim.ucx.core/data/preview.png`
- `source/extensions/isaacsim.ucx.nodes/data/icon.png`
- `source/extensions/isaacsim.ucx.nodes/data/preview.png`
- `source/extensions/isaacsim.util.camera_inspector/data/icon.png`
- `source/extensions/isaacsim.util.camera_inspector/data/preview.png`
- `source/extensions/isaacsim.util.physics/data/icon.png`
- `source/extensions/isaacsim.util.physics/data/preview.png`
- `source/extensions/isaacsim.zmq.bridge/data/icon.png`
- `source/extensions/isaacsim.zmq.bridge/data/preview.png`
- `source/extensions/isaacsim.zmq.core/data/icon.png`
- `source/extensions/isaacsim.zmq.core/data/preview.png`
- `source/extensions/isaacsim.zmq.protos/data/icon.png`
- `source/extensions/isaacsim.zmq.protos/data/preview.png`
- `source/extensions/omni.isaac.core_archive/data/icon.png`
- `source/extensions/omni.isaac.core_archive/data/preview.png`
- `source/extensions/omni.kit.loop-isaac/data/icon.png`
- `source/extensions/omni.kit.loop-isaac/data/preview.png`
- `source/extensions/omni.pip.cloud/data/icon.png`
- `source/extensions/omni.pip.cloud/data/preview.png`
- `source/extensions/omni.pip.compute/data/icon.png`
- `source/extensions/omni.pip.compute/data/preview.png`
- `source/extensions/omni.usd.schema.mujoco/data/icon.png`
- `source/extensions/omni.usd.schema.mujoco/data/preview.png`
- `source/extensions/omni.usd.schema.newton/data/icon.png`
- `source/extensions/omni.usd.schema.newton/data/preview.png`
- `source/libraries/isaacsim/foundation/objects/resources/tests/isaacsim.foundation.objects/attributes.usda`
- `source/libraries/isaacsim/foundation/objects/resources/tests/isaacsim.foundation.objects/scene.usda`
- `source/libraries/isaacsim/foundation/objects/resources/tests/isaacsim.foundation.objects/variant.usda`
- `source/libraries/isaacsim/foundation/ovsim/resources/tests/isaacsim.foundation.ovsim/variant.usda`
- `source/libraries/isaacsim/foundation/prims/resources/tests/isaacsim.foundation.prims/ant.usda`
- `source/libraries/isaacsim/foundation/usd/openusd/resources/tests/isaacsim.foundation.usd.openusd/attributes.usda`
- `source/libraries/isaacsim/foundation/usd/openusd/resources/tests/isaacsim.foundation.usd.openusd/scene.usda`
- `source/libraries/isaacsim/foundation/usd/openusd/resources/tests/isaacsim.foundation.usd.openusd/variant.usda`
- `source/libraries/isaacsim/foundation/usd/ovstage/resources/tests/isaacsim.foundation.usd.ovstage/attributes.usda`
- `source/libraries/isaacsim/foundation/usd/ovstage/resources/tests/isaacsim.foundation.usd.ovstage/scene.usda`
- `source/libraries/isaacsim/foundation/usd/ovstage/resources/tests/isaacsim.foundation.usd.ovstage/variant.usda`
- `source/libraries/isaacsim/ovsim/api/resources/tests/isaacsim.ovsim.api/variant.usda`
- `source/libraries/isaacsim/ovsim/clients/local/resources/tests/isaacsim.ovsim.clients.local/variant.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/Ant.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/CartPole.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/CartPoleNoRail.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/CartRailNoPole.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/FixedTendonTest.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/Humanoid.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/MultipleSpatialTendonsTest.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/ShadowHand.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/SpatialTendonTest.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/SurfaceDeformable.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/VolumeDeformable.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/cabinet.usda`
- `source/libraries/isaacsim/physics/manager/resources/tests/franka.usda`
- `source/libraries/isaacsim/physics/ovsim/resources/tests/isaacsim.physics.ovsim/variant.usda`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/camera_link.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_hand.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_leftfinger.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_link0.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_link1.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_link2.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_link3.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_link4.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_link5.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_link6.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_link7.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/franka/meshes/panda_rightfinger.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/collision/base.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/collision/forearm.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/collision/shoulder.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/collision/upperarm.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/collision/wrist1.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/collision/wrist2.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/collision/wrist3.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/visual/base.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/visual/forearm.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/visual/shoulder.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/visual/upperarm.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/visual/wrist1.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/visual/wrist2.stl`
- `source/libraries/isaacsim/robot_motion/cumotion/python/robot_configurations/ur10/meshes/visual/wrist3.stl`
- `source/scripts/python/linux-aarch64/icon/omni.isaac.sim.png`
- `source/scripts/python/linux-x86_64/icon/omni.isaac.sim.png`
- `source/standalone_examples/benchmarks/data/mobility_gen/warehouse_multiple_shelves/map.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.066667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.083333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.100000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.116667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.133333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.150000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.166667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.183333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.200000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.216667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.233333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.250000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.266667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.283333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.300000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.316667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.333333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.350000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.366667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/OmniverseKit_Persp/rgb/rgb_0.383333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.066667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.083333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.100000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.116667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.133333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.150000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.166667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.183333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.200000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.216667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.233333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.250000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.266667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.283333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.300000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.316667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.333333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.350000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.366667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/left/camera_left/rgb/rgb_0.383333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.066667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.083333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.100000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.116667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.133333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.150000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.166667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.183333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.200000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.216667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.233333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.250000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.266667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.283333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.300000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.316667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.333333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.350000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.366667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/back_hawk/right/camera_right/rgb/rgb_0.383333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.066667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.083333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.100000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.116667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.133333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.150000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.166667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.183333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.200000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.216667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.233333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.250000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.266667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.283333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.300000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.316667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.333333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.350000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.366667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/left/camera_left/rgb/rgb_0.383333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.066667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.083333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.100000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.116667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.133333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.150000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.166667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.183333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.200000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.216667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.233333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.250000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.266667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.283333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.300000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.316667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.333333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.350000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.366667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/front_hawk/right/camera_right/rgb/rgb_0.383333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.066667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.083333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.100000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.116667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.133333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.150000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.166667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.183333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.200000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.216667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.233333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.250000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.266667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.283333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.300000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.316667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.333333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.350000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.366667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/left/camera_left/rgb/rgb_0.383333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.066667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.083333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.100000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.116667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.133333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.150000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.166667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.183333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.200000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.216667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.233333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.250000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.266667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.283333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.300000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.316667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.333333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.350000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.366667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/left_hawk/right/camera_right/rgb/rgb_0.383333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.066667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.083333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.100000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.116667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.133333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.150000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.166667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.183333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.200000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.216667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.233333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.250000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.266667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.283333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.300000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.316667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.333333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.350000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.366667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/left/camera_left/rgb/rgb_0.383333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.066667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.083333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.100000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.116667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.133333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.150000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.166667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.183333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.200000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.216667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.233333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.250000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.266667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.283333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.300000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.316667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.333333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.350000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.366667.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_robots_nova_carter_ros2/Robots/Robot_0/chassis_link/sensors/right_hawk/right/camera_right/rgb/rgb_0.383333.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_sdg/OmniverseKit_Persp/rgb/rgb_0000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_sdg/Replicator/cam_0_Xform/cam_0/rgb/rgb_0000.png`
- `source/standalone_examples/benchmarks/validation/golden_data/benchmark_sdg/Replicator/cam_1_Xform/cam_1/rgb/rgb_0000.png`
- `source/standalone_examples/data/torus/torus.obj`
- `source/standalone_examples/data/torus/torus.stl`
- `source/standalone_examples/testing/isaacsim.core.api/data/orientation_bug.usd`
- `templates/isaacsim-cpp-extension/data/icon.png`
- `templates/isaacsim-cpp-extension/data/preview.png`
- `templates/isaacsim-omnigraph-extension/data/icon.png`
- `templates/isaacsim-omnigraph-extension/data/preview.png`
- `templates/isaacsim-python-extension/data/icon.png`
- `templates/isaacsim-python-extension/data/preview.png`
- `templates/isaacsim-ui-extension/data/icon.png`
- `templates/isaacsim-ui-extension/data/preview.png`

</details>

## 122. IsaacLab
1. Nombre: Isaac Lab (isaac-sim/IsaacLab)
2. URL visible: https://github.com/isaac-sim/IsaacLab
3. Micro resumen: Isaac Lab — componente de la lista 2 (t130u).
4. LOOP: Escenario → Isaac Sim → Física + sensores + robot → Agente AI → Acción → Simulación → Datos/Reward → Isaac Lab → Aprendizaje → Nueva política
- Ubicación: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/IsaacLab — re-adquirido sin LFS por motores (ZIP local → motor_1 → motor_3) · 372 punteros LFS eliminados · reglas filter=lfs quitadas: .gitattributes (líneas filter=lfs quitadas); tools/template/templates/external/.gitattributes (líneas filter=lfs quitadas) · 25 symlink(s) omitidos (regla del engine)
<details><summary>Rutas LFS eliminadas (372)</summary>

- `docs/source/_static/actuators/delay-clip.webp`
- `source/isaaclab_newton/test/assets/data/articulation_ordering_branching.usda`
- `source/isaaclab_newton/test/assets/data/fixed_cartpole.usda`
- `source/isaaclab_newton/test/assets/data/fixed_spatial_chain.usda`
- `source/isaaclab_newton/test/assets/data/fixed_tendon_hand.usda`
- `source/isaaclab_newton/test/assets/data/floating_two_leg.usda`
- `source/isaaclab_newton/test/assets/data/floating_two_link.usda`
- `source/isaaclab_newton/test/assets/data/revolute_pendulum.usda`
- `source/isaaclab_newton/test/assets/data/rigid_body_with_articulation_root.usda`
- `source/isaaclab_ov/test/assets/data/articulation_ordering_branching.usda`
- `source/isaaclab_physx/test/assets/data/articulation_ordering_branching.usda`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-ovrtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/newton-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-motion_vectors.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-simple_shading_constant_diffuse.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-simple_shading_diffuse_mdl.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/ovphysx-ovrtx_renderer-simple_shading_full_mdl.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-motion_vectors.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-simple_shading_constant_diffuse.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-simple_shading_diffuse_mdl.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-isaacsim_rtx_renderer-simple_shading_full_mdl.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/cartpole/physx-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/franka_cable/newton-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-motion_vectors.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-ovrtx_renderer-motion_vectors.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/newton-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/physx-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/physx-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/physx-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/physx-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/physx-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/physx-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/physx-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/franka_cloth/physx-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-ovrtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/franka_soft/newton-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/kuka_visual_material_randomization/newton-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/kuka_visual_material_randomization/newton-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/kuka_visual_material_randomization/physx-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-ovrtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/newton-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-motion_vectors.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_hetero/physx-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-ovrtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/newton-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-motion_vectors.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/ovphysx-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-motion_vectors.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/lift_kuka_homo/physx-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/mpm_particles/newton-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/registered_tasks/Isaac-Cartpole-Camera-Direct/default_physics-default_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/registered_tasks/Isaac-Cartpole-Camera-Direct/default_physics-default_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/registered_tasks/Isaac-Cartpole-Camera-Direct/default_physics-default_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/registered_tasks/Isaac-Cartpole-Camera-Direct/default_physics-default_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/registered_tasks/Isaac-Reorient-Cube-Shadow-Camera-Direct/default_physics-default_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/registered_tasks/Isaac-Reorient-Cube-Shadow-Camera-Direct/default_physics-default_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/registered_tasks/Isaac-Reorient-Cube-Shadow-Camera-Direct/default_physics-default_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/registered_tasks/Isaac-Reorient-Cube-Shadow-Camera-Direct/default_physics-default_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-ovrtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/newton-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-motion_vectors.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-simple_shading_constant_diffuse.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-simple_shading_diffuse_mdl.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/ovphysx-ovrtx_renderer-simple_shading_full_mdl.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-albedo.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-instance_id_segmentation_fast.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-motion_vectors.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-simple_shading_constant_diffuse.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-simple_shading_diffuse_mdl.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-isaacsim_rtx_renderer-simple_shading_full_mdl.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-newton_renderer-depth.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-newton_renderer-distance_to_camera.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-newton_renderer-distance_to_image_plane.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-newton_renderer-instance_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-newton_renderer-normals.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand/physx-newton_renderer-semantic_segmentation.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand_yellow_bg/newton-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand_yellow_bg/newton-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand_yellow_bg/physx-isaacsim_rtx_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand_yellow_bg/physx-isaacsim_rtx_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand_yellow_bg/physx-newton_renderer-rgb.png`
- `source/isaaclab_tasks/test/golden_images/shadow_hand_yellow_bg/physx-newton_renderer-rgba.png`
- `source/isaaclab_tasks/test/golden_stages/cartpole/newton-isaacsim_rtx_renderer-rgb.usda`
- `source/isaaclab_tasks/test/golden_stages/cartpole/physx-isaacsim_rtx_renderer-rgb.usda`
- `source/isaaclab_tasks/test/golden_stages/cartpole/physx-newton_renderer-rgb.usda`
- `source/isaaclab_tasks/test/golden_stages/registered_tasks_Isaac-Cartpole-Camera-Direct/default_physics-default_renderer-stage.usda`
- `source/isaaclab_tasks/test/golden_stages/registered_tasks_Isaac-Reorient-Cube-Shadow-Camera-Direct/default_physics-default_renderer-stage.usda`

</details>

## Notas (sin repo)
- Gemini Computer Use (Gemini 3.x): servicio cerrado, sin repo open source → solo nota.
- Pesos HF de TimesFM: NO descargados (regla sin HF).
- Ya estaban en core (no se duplican): vercel-labs/agent-browser, google-research/timesfm.

## No-repo (solo referencia)
- MOSS paper: https://arxiv.org/abs/2605.22794
- Strix web: https://www.strix.ai/
- Video: https://youtu.be/ytlfkXZKB9A
- NotebookLM como buscador adicional vía imput shark (diseño pendiente)

## Pendientes de diseño (del mensaje t126u)
- Micro-Kernel de integración: URL → motores → QUARANTINE → analyzer → COMPONENT-IR.json → planner → compilers → contract gate → sandbox/test → capsule → registry.
- Action Registry para botones del chat.
- agente.md / constitución YAIWES (15 puntos).
- Autoevolución: motor de descarga/extracción como schema-contrato + workflow (sin GitHub Actions).


## Estado final (2026-10-15, America/Bogota)
- Esta carpeta: 122 entradas listadas; lista 1: 103 repos aquí + 7 enlazados en shark imput; lista 2: 12 repos nuevos.
- Sin LFS en todo Yaiwes: 0 punteros LFS y 0 líneas filter=lfs (escaneo completo del repo).
- Sin `_archives` en todo Yaiwes (también shark imput y memoria, tras extraer y verificar con motor_1).
- Forense blob a blob contra upstream: idéntico salvo lo anotado por repo (punteros LFS y reglas filter=lfs eliminados, renovate docs/usage/docker.md, symlinks, MoDr con upstream vacío).
