# HANDOFF — Yaiwes core / componentes integrar (T4)

Índice: [INDICE Yaiwes core componentes para integrar al core Yaiwes.md](./INDICE%20Yaiwes%20core%20componentes%20para%20integrar%20al%20core%20Yaiwes.md) · Índice maestro: [README-INDICE.md](./README-INDICE.md)

Carpeta destino: https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes

## 1. core componentes (T4) — reanudar / auditar

Descarga + extracción de **115** repos hacia `Yaiwes/Yaiwes core/componentes para integrar al core Yaiwes/`.

| Ítem | Valor |
|---|---|
| Lista | `/workspace/descarga-115/lista.txt` (115 líneas; sitios web ya resueltos a owner/repo) |
| Destino | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes |
| Motores | **motor_2** (descarga ZIP) + **engine** + **motor_1** (extracción); partida en **4 motores** |
| Estado | **en planificación** |
| STATE_FILE sugeridos | `/workspace/descarga-115/state/M1.json` … `M4.json` (fuera del árbol Git) |

Sitios → GitHub (9): vespa-engine/vespa, opensearch-project/OpenSearch, apache/solr, elastic/elasticsearch, qdrant/qdrant, milvus-io/milvus, weaviate/weaviate, typesense/typesense, apache/lucene.

### Reanudar

1. Leer `lista.txt` y el STATE_FILE del motor (M1–M4).
2. Relanzar el **mismo** motor_2/engine/motor_1 con las **mismas** rutas absolutas y el mismo STATE_FILE.
3. Un agente (o proceso) por motor; no mezclar lotes.
4. Tras cada push a Yaiwes: `git fetch origin main` + `git rebase origin/main` (nunca force).
5. Evidencias y STATE_FILE fuera del árbol final.

### Auditar (antes de PASS)

1. Cada repo de la lista existe bajo `Yaiwes core/componentes para integrar al core Yaiwes/<nombre>/` (o convención acordada).
2. Verdict motor_1: extracción limpia (CRC / tree hash según skill); sin `.partial` / `.tmp`.
3. Recuento destino vs lista (115); read-back de main.
4. Actualizar este handoff y el índice §6 cuando pase a **en curso** / **hecho**.
5. Checklist GUIA §§1–10 (sin HF/LFS/Actions; sin secretos en markdown).

Índice vivo: [INDICE Yaiwes core componentes para integrar al core Yaiwes.md](./INDICE%20Yaiwes%20core%20componentes%20para%20integrar%20al%20core%20Yaiwes.md).


---

## 2. Plan de motores (copia de PLAN.md del box)

### PLAN descarga+extracción 115 repos → Yaiwes/`Yaiwes core/componentes para integrar al core Yaiwes/` (SOLO PLAN, nada ejecutado)

## Cómo aterriza
Motor 2 → engine: por ítem `Yaiwes core/componentes para integrar al core Yaiwes/<slug>/code/` (repo extraído HEAD, depth=1, sin symlinks/LFS) + `<slug>/_archives/<slug>.bundle.zip.part-NNNN` (12 MiB) + `DOWNLOAD_EXTRACT_MANIFEST.json`. Un push por ítem (no por lote) → límite 2 GB aplica por repo. `_archives` SÍ se sube (≈ duplica peso). Si `<slug>/` existe → ALREADY_PRESENT (no compara). Motor 1 no hace falta (motor 2 ya extrae); solo si se quisiera re-extraer `_archives`.

## Comando por motor (k=1..4)
```
R='<clon>/Motores descarga extracción búsquedas/➡️📂motores de descarga extracción copiado movimiento archivos router-universal-router-inteligente-/📂Motor descarga de componentes y extracción de zip'
QUEUE_FILE=/workspace/descarga-115/queue_motorK.json STATE_FILE=/workspace/descarga-115/state/m2-K.json INDEX_PATH=/workspace/descarga-115/state/index-K.md \
 ENGINE_PATH="$R/hf_download_extract_engine.py" DEST_REPO=maxbry123-commits/Yaiwes DEST_BRANCH=main DEST_ROOT='Yaiwes core/componentes para integrar al core Yaiwes' MAX_RETRIES=3 python3 "$R/motor_2_queue_download_extract.py"
```
4 motores empujan al mismo main: el engine hace rebase sin force; conflictos → NON_FAST_FORWARD_CONFLICT → reintento.

## Hallazgos
- 115/115 existen; ninguno renombrado. Webs resueltas: vespa-engine/vespa, opensearch-project/OpenSearch, apache/solr, elastic/elasticsearch, qdrant/qdrant, milvus-io/milvus, weaviate/weaviate, typesense/typesense, apache/lucene.
- Archivado: SamsungSAILMontreal/TinyRecursiveModels (solo lectura, se descarga igual).
- Ningún archivo >95 MB en HEAD (máx CoEvoSkills 86 MB). elasticsearch: árbol truncado por API, estimado ~0,9 GB.
- Duplicados ya en `Yaiwes/shark imput/componentes por integrar/`: ast-grep, nats-server, playwright, pydantic, python-sdk, spaCy, tree-sitter, zoekt → EXCLUIDOS de las colas (pendiente OK).
- Antes descartados como agentes en la migración anterior y ahora pedidos: hermes-agent, pydantic-ai (y systemd en 'otros'). Se incluyen porque el usuario los pide explícitamente.

## Gigantes (HEAD, push≈code+zip)
- elastic/elasticsearch: 900 MB, 38116 archivos, branch main
- openclaw/openclaw: 670 MB, 55974 archivos, branch main
- Zhang-Henry/CoEvoSkills: 599 MB, 1680 archivos, branch main
- semgrep/semgrep: 561 MB, 12348 archivos, branch develop
- apache/incubator-kie: 344 MB, 25820 archivos, branch main
- pydantic/pydantic-ai: 301 MB, 4343 archivos, branch main
- kubernetes/kubernetes: 277 MB, 31449 archivos, branch master
- vespa-engine/vespa: 273 MB, 22470 archivos, branch master
- bazelbuild/bazel: 242 MB, 14439 archivos, branch master
- NousResearch/hermes-agent: 222 MB, 19727 archivos, branch main
- ctn-archive/spaun1.0: 213 MB, 1386 archivos, branch master
- dagger/dagger: 182 MB, 16689 archivos, branch main
Plan: todos <1,5 GB por push estimado; vigilar CoEvoSkills (binarios, ~1,2 GB push) y elasticsearch (~1,3 GB push). Si falla por tamaño → bajar ese ítem solo, publicar code y _archives en 2 commits (requiere cambio de engine = preguntar).

## Lotes
### Motor 1: 26 repos, 2.17 GB HEAD (~3.2 GB subidos con _archives)
elastic/elasticsearch (900MB), vespa-engine/vespa (273MB), apache/solr (151MB), PaddlePaddle/PaddleOCR (136MB), sqlite/sqlite (113MB), deepset-ai/haystack (111MB), RaspberryPiFoundation/blockly (67MB), zhangxjohn/MoDr (63MB), weaviate/weaviate (57MB), strands-agents/harness-sdk (52MB), ggml-org/whisper.cpp (40MB), apache/uima-uimaj (38MB), DreamLM/Dream (35MB), renovatebot/renovate (34MB), SoarGroup/SoarGroup.github.io (23MB), SWI-Prolog/swipl-devel (18MB), langchain-ai/langgraph (14MB), usestrix/strix (10MB), celery/celery (7MB), GrapesJS/grapesjs (7MB), bellard/quickjs (6MB), BehaviorTree/BehaviorTree.CPP (4MB), jruizgit/rules (3MB), trueagi-io/hyperon-experimental (2MB), opennars/opennars (1MB), in-toto/in-toto (1MB)
### Motor 2: 27 repos, 2.17 GB HEAD (~3.2 GB subidos con _archives)
openclaw/openclaw (670MB), kubernetes/kubernetes (277MB), ctn-archive/spaun1.0 (213MB), opensearch-project/OpenSearch (161MB), milvus-io/milvus (136MB), ECNU-ICALK/AutoSkill (120MB), systemd/systemd (105MB), open-policy-agent/opa (74MB), rabbitmq/rabbitmq-server (63MB), souffle-lang/souffle (56MB), gepa-ai/gepa (46MB), opendilab/LightZero (43MB), Z3Prover/z3 (37MB), apache/calcite (36MB), meilisearch/meilisearch (33MB), tauri-apps/tauri (22MB), SakanaAI/continuous-thought-machines (20MB), SamsungSAILMontreal/TinyRecursiveModels (12MB), apache/pouchdb (10MB), egraphs-good/egglog (10MB), codesandbox/sandpack (6MB), eclipsesource/jsonforms (4MB), pyodide/pyodide (4MB), ajv-validator/ajv (3MB), XiangJinyu/AFlow_ (2MB), seal-rg/recurrent-pretraining (1MB), WojciechMula/pyahocorasick (0MB)
### Motor 3: 27 repos, 2.17 GB HEAD (~3.2 GB subidos con _archives)
Zhang-Henry/CoEvoSkills (599MB), pydantic/pydantic-ai (301MB), bazelbuild/bazel (242MB), asmaloney/ACT-R (170MB), apache/lucene (138MB), google/or-tools (133MB), oss-review-toolkit/ort (82MB), bytecodealliance/wasmtime (79MB), HKUDS/CLI-Anything (63MB), microsoft/agent-framework (61MB), google/osv-scanner (53MB), temporalio/temporal (42MB), qdrant/qdrant (37MB), node-red/node-red (36MB), facebookresearch/coconut (33MB), openai/openai-agents-python (27MB), KnowledgeXLab/EvolveR (15MB), typesense/typesense (13MB), networkx/networkx (10MB), algorithmicsuperintelligence/openevolve (8MB), Memento-Teams/Memento-Skills (6MB), facebookresearch/vjepa2 (6MB), china-qijizhifeng/agentic-harness-engineering (4MB), ionic-team/capacitor (3MB), nengo/nengo (2MB), facebookresearch/large_concept_model (2MB), sapientinc/HRM (0MB)
### Motor 4: 27 repos, 2.17 GB HEAD (~3.2 GB subidos con _archives)
semgrep/semgrep (561MB), apache/incubator-kie (344MB), NousResearch/hermes-agent (222MB), dagger/dagger (182MB), pwa-builder/PWABuilder (141MB), deepseek-ai/deepseek-harness (132MB), Wilfred/difftastic (97MB), joernio/joern (77MB), affaan-m/ECC (62MB), jennyzzt/dgm (53MB), microsoft/autogen (48MB), langchain-ai/langchain (44MB), google/artemis (37MB), anchore/syft (35MB), modelscope/AgentEvolver (34MB), ML-GSAI/LLaDA (26MB), cue-lang/cue (17MB), open-telemetry/opentelemetry-collector (12MB), cel-expr/cel-go (10MB), TimelyDataflow/differential-dataflow (8MB), danijar/dreamerv3 (7MB), dexie/Dexie.js (4MB), sigstore/cosign (4MB), python-jsonschema/jsonschema (4MB), puckeditor/puck (3MB), localForage/localForage (1MB), facebookresearch/blt (1MB)

## Tabla completa
|#|repo|branch|MB HEAD|archivos|max MB|archivado|dup|
|-|-|-|-|-|-|-|-|
|1|SoarGroup/SoarGroup.github.io|main|22.9|388|2.3|false||
|2|opennars/opennars|master|1.3|419|0.0|false||
|3|trueagi-io/hyperon-experimental|main|2.3|296|0.2|false||
|4|apache/incubator-kie|main|344.5|25820|51.7|false||
|5|jruizgit/rules|master|2.9|73|0.4|false||
|6|souffle-lang/souffle|master|56.3|4080|16.2|false||
|7|egraphs-good/egglog|main|9.5|581|1.3|false||
|8|SWI-Prolog/swipl-devel|master|17.7|1957|0.8|false||
|9|Z3Prover/z3|master|36.6|3092|0.4|false||
|10|google/or-tools|stable|132.9|4842|28.8|false||
|11|apache/calcite|main|36.2|3305|1.0|false||
|12|BehaviorTree/BehaviorTree.CPP|master|3.8|337|0.9|false||
|13|networkx/networkx|main|10.3|976|1.3|false||
|14|kubernetes/kubernetes|master|276.8|31449|5.4|false||
|15|temporalio/temporal|main|42.5|3994|0.6|false||
|16|sqlite/sqlite|master|113.2|2292|17.0|false||
|17|nats-io/nats-server|main|14.9|599|0.8|false|SÍ|
|18|rabbitmq/rabbitmq-server|main|62.5|3719|2.2|false||
|19|celery/celery|main|7.0|852|0.2|false||
|20|systemd/systemd|main|105.3|7617|6.6|false||
|21|bazelbuild/bazel|master|241.9|14439|6.0|false||
|22|TimelyDataflow/differential-dataflow|master|7.7|360|1.8|false||
|23|WojciechMula/pyahocorasick|master|0.4|124|0.0|false||
|24|open-policy-agent/opa|main|74.2|7917|5.1|false||
|25|cel-expr/cel-go|master|10.0|862|0.2|false||
|26|cue-lang/cue|master|16.7|3915|0.5|false||
|27|pydantic/pydantic|main|11.6|851|0.7|false|SÍ|
|28|python-jsonschema/jsonschema|main|3.6|627|0.2|false||
|29|explosion/spaCy|master|20.6|1776|1.2|false|SÍ|
|30|apache/uima-uimaj|main|38.1|5755|1.2|false||
|31|PaddlePaddle/PaddleOCR|main|135.6|2455|10.6|false||
|32|vespa-engine/vespa|master|272.6|22470|38.1|false||
|33|opensearch-project/OpenSearch|main|160.7|19334|2.5|false||
|34|apache/solr|main|150.8|8817|4.9|false||
|35|elastic/elasticsearch|main|900.0|38116|19.8|false||
|36|qdrant/qdrant|master|37.2|2446|0.8|false||
|37|milvus-io/milvus|master|135.6|6832|8.6|false||
|38|weaviate/weaviate|main|56.8|5870|1.0|false||
|39|typesense/typesense|v31|12.6|508|0.9|false||
|40|apache/lucene|main|137.8|7627|11.2|false||
|41|meilisearch/meilisearch|main|33.5|1750|7.5|false||
|42|sourcegraph/zoekt|main|3.7|346|0.1|false|SÍ|
|43|HKUDS/CLI-Anything|main|63.0|1872|4.9|false||
|44|affaan-m/ECC|main|61.8|4615|5.7|false||
|45|deepseek-ai/deepseek-harness|master|131.8|16083|1.4|false||
|46|NousResearch/hermes-agent|main|221.9|19727|3.9|false||
|47|openclaw/openclaw|main|670.4|55974|5.1|false||
|48|langchain-ai/langchain|master|44.2|3190|4.7|false||
|49|langchain-ai/langgraph|main|14.3|691|0.7|false||
|50|openai/openai-agents-python|main|27.2|1696|1.5|false||
|51|deepset-ai/haystack|main|111.5|12744|1.1|false||
|52|pydantic/pydantic-ai|main|301.2|4343|15.0|false||
|53|microsoft/agent-framework|main|60.7|5532|1.6|false||
|54|strands-agents/harness-sdk|main|52.5|3284|11.5|false||
|55|microsoft/autogen|main|48.3|1837|31.5|false||
|56|modelcontextprotocol/python-sdk|main|15.5|1726|0.4|false|SÍ|
|57|google/artemis|main|36.6|817|7.1|false||
|58|usestrix/strix|main|9.9|544|1.7|false||
|59|tree-sitter/tree-sitter|master|4.5|628|0.2|false|SÍ|
|60|joernio/joern|master|76.6|2216|5.8|false||
|61|ast-grep/ast-grep|main|3.0|325|0.2|false|SÍ|
|62|semgrep/semgrep|develop|561.3|12348|62.4|false||
|63|oss-review-toolkit/ort|main|82.4|3675|15.8|false||
|64|anchore/syft|main|34.8|3087|6.0|false||
|65|google/osv-scanner|main|52.9|1134|16.6|false||
|66|Wilfred/difftastic|master|97.4|483|38.2|false||
|67|ajv-validator/ajv|master|3.4|486|0.5|false||
|68|bytecodealliance/wasmtime|main|78.6|7587|14.2|false||
|69|dagger/dagger|main|182.4|16689|11.7|false||
|70|open-telemetry/opentelemetry-collector|main|11.8|2867|0.3|false||
|71|in-toto/in-toto|develop|0.7|183|0.1|false||
|72|sigstore/cosign|main|4.1|483|1.3|false||
|73|renovatebot/renovate|main|33.8|3968|3.5|false||
|74|microsoft/playwright|main|69.2|3127|1.2|false|SÍ|
|75|GrapesJS/grapesjs|dev|6.8|735|1.2|false||
|76|puckeditor/puck|main|2.7|810|0.7|false||
|77|eclipsesource/jsonforms|master|4.2|843|1.1|false||
|78|node-red/node-red|main|36.4|1550|7.0|false||
|79|RaspberryPiFoundation/blockly|main|67.3|2565|12.4|false||
|80|bellard/quickjs|master|6.1|109|2.1|false||
|81|pyodide/pyodide|main|4.0|545|0.3|false||
|82|codesandbox/sandpack|main|6.1|579|0.9|false||
|83|dexie/Dexie.js|master|4.5|816|0.5|false||
|84|localForage/localForage|master|1.0|98|0.1|false||
|85|apache/pouchdb|master|10.0|865|0.9|false||
|86|tauri-apps/tauri|dev|22.5|1098|5.2|false||
|87|ionic-team/capacitor|main|3.1|510|0.2|false||
|88|pwa-builder/PWABuilder|main|141.4|1687|16.1|false||
|89|ggml-org/whisper.cpp|master|40.0|2039|4.1|false||
|90|china-qijizhifeng/agentic-harness-engineering|main|4.0|224|1.3|false||
|91|ECNU-ICALK/AutoSkill|main|120.0|10048|18.4|false||
|92|Zhang-Henry/CoEvoSkills|main|599.5|1680|86.3|false||
|93|Memento-Teams/Memento-Skills|main|6.3|641|0.9|false||
|94|algorithmicsuperintelligence/openevolve|main|8.0|520|0.9|false||
|95|jennyzzt/dgm|main|53.2|1650|2.2|false||
|96|gepa-ai/gepa|main|45.8|608|4.9|false||
|97|XiangJinyu/AFlow_|main|1.9|43|0.9|false||
|98|modelscope/AgentEvolver|main|33.8|379|7.0|false||
|99|KnowledgeXLab/EvolveR|main|14.6|665|1.6|false||
|100|opendilab/LightZero|main|43.3|899|3.3|false||
|101|danijar/dreamerv3|main|6.6|95|0.9|false||
|102|sapientinc/HRM|main|0.2|26|0.1|false||
|103|SamsungSAILMontreal/TinyRecursiveModels|main|11.5|40|4.0|true||
|104|seal-rg/recurrent-pretraining|main|1.5|82|0.1|false||
|105|zhangxjohn/MoDr|main|62.9|95|25.1|false||
|106|SakanaAI/continuous-thought-machines|main|20.1|107|6.6|false||
|107|facebookresearch/coconut|main|32.8|23|30.9|false||
|108|facebookresearch/large_concept_model|main|1.8|171|0.6|false||
|109|ML-GSAI/LLaDA|main|26.3|1760|9.1|false||
|110|DreamLM/Dream|main|35.1|594|19.0|false||
|111|facebookresearch/blt|main|0.9|112|0.2|false||
|112|facebookresearch/vjepa2|main|5.5|173|3.7|false||
|113|asmaloney/ACT-R|main|170.2|448|63.1|false||
|114|nengo/nengo|main|2.1|281|0.2|false||
|115|ctn-archive/spaun1.0|master|213.3|1386|62.7|false||


---

## 3. Enlaces directos por componente (115)

| # | Repo origen | Ubicación |
|---|---|---|
| 1 | https://github.com/SoarGroup/SoarGroup.github.io | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/SoarGroup.github.io (pendiente) |
| 2 | https://github.com/opennars/opennars | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/opennars (pendiente) |
| 3 | https://github.com/trueagi-io/hyperon-experimental | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/hyperon-experimental (pendiente) |
| 4 | https://github.com/apache/incubator-kie | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/incubator-kie (pendiente) |
| 5 | https://github.com/jruizgit/rules | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/rules (pendiente) |
| 6 | https://github.com/souffle-lang/souffle | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/souffle (pendiente) |
| 7 | https://github.com/egraphs-good/egglog | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/egglog (pendiente) |
| 8 | https://github.com/SWI-Prolog/swipl-devel | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/swipl-devel (pendiente) |
| 9 | https://github.com/Z3Prover/z3 | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/z3 (pendiente) |
| 10 | https://github.com/google/or-tools | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/or-tools (pendiente) |
| 11 | https://github.com/apache/calcite | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/calcite (pendiente) |
| 12 | https://github.com/BehaviorTree/BehaviorTree.CPP | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/BehaviorTree.CPP (pendiente) |
| 13 | https://github.com/networkx/networkx | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/networkx (pendiente) |
| 14 | https://github.com/kubernetes/kubernetes | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/kubernetes (pendiente) |
| 15 | https://github.com/temporalio/temporal | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/temporal (pendiente) |
| 16 | https://github.com/sqlite/sqlite | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/sqlite (pendiente) |
| 17 | https://github.com/nats-io/nats-server | https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/nats-server (ya en shark) |
| 18 | https://github.com/rabbitmq/rabbitmq-server | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/rabbitmq-server (pendiente) |
| 19 | https://github.com/celery/celery | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/celery (pendiente) |
| 20 | https://github.com/systemd/systemd | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/systemd (pendiente) |
| 21 | https://github.com/bazelbuild/bazel | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/bazel (pendiente) |
| 22 | https://github.com/TimelyDataflow/differential-dataflow | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/differential-dataflow (pendiente) |
| 23 | https://github.com/WojciechMula/pyahocorasick | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/pyahocorasick (pendiente) |
| 24 | https://github.com/open-policy-agent/opa | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/opa (pendiente) |
| 25 | https://github.com/cel-expr/cel-go | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/cel-go (pendiente) |
| 26 | https://github.com/cue-lang/cue | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/cue (pendiente) |
| 27 | https://github.com/pydantic/pydantic | https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/pydantic (ya en shark) |
| 28 | https://github.com/python-jsonschema/jsonschema | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/jsonschema (pendiente) |
| 29 | https://github.com/explosion/spaCy | https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/spaCy (ya en shark) |
| 30 | https://github.com/apache/uima-uimaj | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/uima-uimaj (pendiente) |
| 31 | https://github.com/PaddlePaddle/PaddleOCR | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/PaddleOCR (pendiente) |
| 32 | https://github.com/vespa-engine/vespa | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/vespa (pendiente) |
| 33 | https://github.com/opensearch-project/OpenSearch | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/OpenSearch (pendiente) |
| 34 | https://github.com/apache/solr | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/solr (pendiente) |
| 35 | https://github.com/elastic/elasticsearch | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/elasticsearch (pendiente) |
| 36 | https://github.com/qdrant/qdrant | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/qdrant (pendiente) |
| 37 | https://github.com/milvus-io/milvus | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/milvus (pendiente) |
| 38 | https://github.com/weaviate/weaviate | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/weaviate (pendiente) |
| 39 | https://github.com/typesense/typesense | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/typesense (pendiente) |
| 40 | https://github.com/apache/lucene | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/lucene (pendiente) |
| 41 | https://github.com/meilisearch/meilisearch | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/meilisearch (pendiente) |
| 42 | https://github.com/sourcegraph/zoekt | https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/zoekt (ya en shark) |
| 43 | https://github.com/HKUDS/CLI-Anything | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/CLI-Anything (pendiente) |
| 44 | https://github.com/affaan-m/ECC | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/ECC (pendiente) |
| 45 | https://github.com/deepseek-ai/deepseek-harness | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/deepseek-harness (pendiente) |
| 46 | https://github.com/NousResearch/hermes-agent | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/hermes-agent (pendiente) |
| 47 | https://github.com/openclaw/openclaw | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/openclaw (pendiente) |
| 48 | https://github.com/langchain-ai/langchain | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/langchain (pendiente) |
| 49 | https://github.com/langchain-ai/langgraph | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/langgraph (pendiente) |
| 50 | https://github.com/openai/openai-agents-python | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/openai-agents-python (pendiente) |
| 51 | https://github.com/deepset-ai/haystack | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/haystack (pendiente) |
| 52 | https://github.com/pydantic/pydantic-ai | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/pydantic-ai (pendiente) |
| 53 | https://github.com/microsoft/agent-framework | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/agent-framework (pendiente) |
| 54 | https://github.com/strands-agents/harness-sdk | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/harness-sdk (pendiente) |
| 55 | https://github.com/microsoft/autogen | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/autogen (pendiente) |
| 56 | https://github.com/modelcontextprotocol/python-sdk | https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/python-sdk (ya en shark) |
| 57 | https://github.com/google/artemis | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/artemis (pendiente) |
| 58 | https://github.com/usestrix/strix | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/strix (pendiente) |
| 59 | https://github.com/tree-sitter/tree-sitter | https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/tree-sitter (ya en shark) |
| 60 | https://github.com/joernio/joern | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/joern (pendiente) |
| 61 | https://github.com/ast-grep/ast-grep | https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/ast-grep (ya en shark) |
| 62 | https://github.com/semgrep/semgrep | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/semgrep (pendiente) |
| 63 | https://github.com/oss-review-toolkit/ort | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/ort (pendiente) |
| 64 | https://github.com/anchore/syft | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/syft (pendiente) |
| 65 | https://github.com/google/osv-scanner | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/osv-scanner (pendiente) |
| 66 | https://github.com/Wilfred/difftastic | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/difftastic (pendiente) |
| 67 | https://github.com/ajv-validator/ajv | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/ajv (pendiente) |
| 68 | https://github.com/bytecodealliance/wasmtime | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/wasmtime (pendiente) |
| 69 | https://github.com/dagger/dagger | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/dagger (pendiente) |
| 70 | https://github.com/open-telemetry/opentelemetry-collector | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/opentelemetry-collector (pendiente) |
| 71 | https://github.com/in-toto/in-toto | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/in-toto (pendiente) |
| 72 | https://github.com/sigstore/cosign | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/cosign (pendiente) |
| 73 | https://github.com/renovatebot/renovate | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/renovate (pendiente) |
| 74 | https://github.com/microsoft/playwright | https://github.com/maxbry123-commits/Yaiwes/tree/main/shark%20imput/componentes%20por%20integrar/playwright (ya en shark) |
| 75 | https://github.com/GrapesJS/grapesjs | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/grapesjs (pendiente) |
| 76 | https://github.com/puckeditor/puck | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/puck (pendiente) |
| 77 | https://github.com/eclipsesource/jsonforms | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/jsonforms (pendiente) |
| 78 | https://github.com/node-red/node-red | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/node-red (pendiente) |
| 79 | https://github.com/RaspberryPiFoundation/blockly | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/blockly (pendiente) |
| 80 | https://github.com/bellard/quickjs | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/quickjs (pendiente) |
| 81 | https://github.com/pyodide/pyodide | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/pyodide (pendiente) |
| 82 | https://github.com/codesandbox/sandpack | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/sandpack (pendiente) |
| 83 | https://github.com/dexie/Dexie.js | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/Dexie.js (pendiente) |
| 84 | https://github.com/localForage/localForage | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/localForage (pendiente) |
| 85 | https://github.com/apache/pouchdb | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/pouchdb (pendiente) |
| 86 | https://github.com/tauri-apps/tauri | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/tauri (pendiente) |
| 87 | https://github.com/ionic-team/capacitor | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/capacitor (pendiente) |
| 88 | https://github.com/pwa-builder/PWABuilder | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/PWABuilder (pendiente) |
| 89 | https://github.com/ggml-org/whisper.cpp | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/whisper.cpp (pendiente) |
| 90 | https://github.com/china-qijizhifeng/agentic-harness-engineering | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/agentic-harness-engineering (pendiente) |
| 91 | https://github.com/ECNU-ICALK/AutoSkill | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/AutoSkill (pendiente) |
| 92 | https://github.com/Zhang-Henry/CoEvoSkills | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/CoEvoSkills (pendiente) |
| 93 | https://github.com/Memento-Teams/Memento-Skills | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/Memento-Skills (pendiente) |
| 94 | https://github.com/algorithmicsuperintelligence/openevolve | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/openevolve (pendiente) |
| 95 | https://github.com/jennyzzt/dgm | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/dgm (pendiente) |
| 96 | https://github.com/gepa-ai/gepa | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/gepa (pendiente) |
| 97 | https://github.com/XiangJinyu/AFlow_ | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/AFlow_ (pendiente) |
| 98 | https://github.com/modelscope/AgentEvolver | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/AgentEvolver (pendiente) |
| 99 | https://github.com/KnowledgeXLab/EvolveR | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/EvolveR (pendiente) |
| 100 | https://github.com/opendilab/LightZero | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/LightZero (pendiente) |
| 101 | https://github.com/danijar/dreamerv3 | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/dreamerv3 (pendiente) |
| 102 | https://github.com/sapientinc/HRM | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/HRM (pendiente) |
| 103 | https://github.com/SamsungSAILMontreal/TinyRecursiveModels | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/TinyRecursiveModels (pendiente) |
| 104 | https://github.com/seal-rg/recurrent-pretraining | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/recurrent-pretraining (pendiente) |
| 105 | https://github.com/zhangxjohn/MoDr | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/MoDr (pendiente) |
| 106 | https://github.com/SakanaAI/continuous-thought-machines | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/continuous-thought-machines (pendiente) |
| 107 | https://github.com/facebookresearch/coconut | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/coconut (pendiente) |
| 108 | https://github.com/facebookresearch/large_concept_model | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/large_concept_model (pendiente) |
| 109 | https://github.com/ML-GSAI/LLaDA | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/LLaDA (pendiente) |
| 110 | https://github.com/DreamLM/Dream | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/Dream (pendiente) |
| 111 | https://github.com/facebookresearch/blt | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/blt (pendiente) |
| 112 | https://github.com/facebookresearch/vjepa2 | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/vjepa2 (pendiente) |
| 113 | https://github.com/asmaloney/ACT-R | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/ACT-R (pendiente) |
| 114 | https://github.com/nengo/nengo | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/nengo (pendiente) |
| 115 | https://github.com/ctn-archive/spaun1.0 | https://github.com/maxbry123-commits/Yaiwes/tree/main/Yaiwes%20core/componentes%20para%20integrar%20al%20core%20Yaiwes/spaun1.0 (pendiente) |


---
## Actualización 2026-10-15 (America/Bogota)
- Carpeta renombrada `componentes integrar` → `componentes para integrar al core Yaiwes`.
- 53 componentes de la lista core kernel se movieron a `core kernel Yaiwes principal` (sus enlaces arriba ya apuntan allí); pouchdb duplicado eliminado (queda en core kernel).
- `_archives/` borrado donde el árbol `code/` cuadra con el manifiesto; conservado donde no (árbol≠manifiesto).
- Fallidos de los 115 (qdrant, autogen, agent-framework, renovate): resueltos en el cierre final (ver abajo).
- Core kernel: https://github.com/maxbry123-commits/Yaiwes/blob/main/Yaiwes%20core/core%20kernel%20Yaiwes%20principal/README.md


---
## Cierre final 2026-10-15 (America/Bogota)
- 65 repos con árbol≠manifiesto: 3227 archivos faltantes recuperados desde `_archives` con motor_1 (CRC + tree hash = manifiesto) y `_archives` borrado. Causa: archivos ignorados por el `.gitignore` del propio repo al hacer `git add`.
- qdrant, autogen, agent-framework: importados sin LFS (punteros LFS quedan como punteros: 1, 51, 2). renovate: importado excluyendo solo `docs/usage/docker.md` (push protection).
- Forense upstream↔destino blob a blob en 152 repos: idénticos (198 archivos alineados con el blob upstream por normalización EOL). Excepciones: renovate (1 excluido) y MoDr (upstream vacío hoy).
- Sin `_archives`, sin duplicados, sin sueltos en `Yaiwes core/`.
