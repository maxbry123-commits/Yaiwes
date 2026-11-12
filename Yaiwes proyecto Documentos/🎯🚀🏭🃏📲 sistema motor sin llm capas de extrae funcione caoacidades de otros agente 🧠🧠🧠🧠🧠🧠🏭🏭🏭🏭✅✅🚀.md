Sistema de extracción de componentes 

Procesó durante 15s

Sí. Yo crearía un Capability Discovery Engine totalmente separado del agente y sin LLM. Su trabajo sería descubrir automáticamente todo lo que Hermes, OpenClaw, Claude Code, Codex, etc. realmente pueden hacer, convertirlo a capacidades pequeñas y registrarlas para que el Task-OS pueda usarlas.

Hermes es un buen ejemplo: actualmente expone un registro amplio de tools —web, browser, terminal, archivos, memoria, delegación, tareas programadas, etc.— y además plugins que pueden registrar tools, hooks y comandos.  OpenClaw también separa tools, skills, plugins, automations, sub-agents y Code Mode, por lo que esas superficies pueden descubrirse programáticamente. 

Motor propuesto: Capability Discovery Engine

No le preguntas al agente:

> “¿Qué sabes hacer?”



Porque podría olvidar capacidades o inventarlas.

El motor inspecciona directamente:

CÓDIGO → REGISTROS → SCHEMAS → PLUGINS → SKILLS → COMANDOS → WORKFLOWS → DEPENDENCIAS → PRUEBAS

y construye:

AGENT CAPABILITY MAP

El flujo sería:

AGENTE/REPO → STATIC SCAN → REGISTRY SCAN → PLUGIN SCAN → SKILL SCAN → WORKFLOW SCAN → DEPENDENCY CHECK → SANDBOX TEST → CAPABILITY GRAPH → INDEX

1. Static Scanner

Escanea el código sin ejecutarlo.

Busca automáticamente patrones Python como:

register_tool(...)
register_command(...)
register_hook(...)
register_skill(...)

también:

def browser_open(...)
def send_email(...)
def read_file(...)

y decoradores:

@tool
@command
@workflow

Lo haría con ast, no con regex.

import ast

def discover_functions(path):
    tree = ast.parse(open(path).read())

    return [
        node.name
        for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    ]

Después clasifica:

send_email()
   ↓
CATEGORY=email
ACTION=send
INPUT=recipient, body
OUTPUT=message_id


---

2. Registry Scanner

Este es aún más importante.

Si Hermes ya posee:

TOOL_REGISTRY

el motor lo lee directamente.

Hermes actualmente organiza sus herramientas en toolsets y su documentación de referencia describe cerca de un centenar de tools registrados. 

Obtendrías algo como:

{
  "name": "web_search",
  "source": "hermes",
  "type": "tool",
  "inputs": ["query"],
  "status": "declared"
}

No tienes que comprender manualmente todo Hermes.


---

3. Plugin Scanner

Busca:

plugins/**
plugin.yaml
manifest.json
pyproject.toml

En Hermes esto es especialmente fácil porque un plugin puede declarar plugin.yaml y registrar herramientas, hooks y comandos mediante su API de plugins. 

El motor extraería:

PLUGIN
 ├─ tools
 ├─ commands
 ├─ hooks
 ├─ skills
 ├─ dependencies
 └─ required_credentials

Hermes incluso descubre plugins desde varias ubicaciones —bundled, usuario, proyecto y entry points de Python—, patrón que puedes reutilizar. 


---

4. Skill / Workflow Scanner

Aquí descubres no solamente herramientas individuales, sino cosas completas que el sistema sabe hacer.

Ejemplo:

SKILL:
"investigar un repositorio"

puede requerir:

search
↓
read files
↓
inspect commits
↓
compare
↓
produce report

El motor lo transforma en:

{
  "capability_id": "CAP_REPO_RESEARCH",
  "type": "workflow",
  "operations": [
    "search_repo",
    "read_file",
    "compare",
    "report"
  ]
}

OpenClaw distingue precisamente herramientas, skills, plugins, automation y Code Mode, por lo que conviene escanear cada superficie independientemente. 


---

5. Dependency Detector

Una capacidad declarada no significa que pueda ejecutarse.

Por ejemplo:

Spotify tool

puede existir pero faltar credenciales.

Así que cada capacidad tendría cuatro estados:

DECLARED
DISCOVERED
AVAILABLE
VERIFIED

Ejemplo:

{
  "capability": "EMAIL_SEND",
  "declared": true,
  "dependencies_ok": true,
  "credentials_ok": false,
  "verified": false
}

Esto evita que YAIWES crea que posee algo que en realidad no está operativo.


---

6. Dynamic Probe

Después viene una prueba controlada.

No probaría operaciones destructivas.

Usaría tests pequeños:

read_file
→ archivo temporal

browser_open
→ página local

write_file
→ sandbox temporal

search
→ consulta controlada

Resultado:

CAP_BROWSER_OPEN
DECLARED ✅
IMPORTABLE ✅
DEPENDENCIES ✅
EXECUTION ✅
OUTPUT_SCHEMA ✅

STATUS = VERIFIED


---

7. Capability Fingerprint

A cada capacidad le daría una huella.

Por ejemplo:

{
  "capability_id": "HERMES_BROWSER_OPEN_V1",

  "provider": "hermes",

  "category": "browser",
  "action": "open",

  "input_schema": {
    "url": "string"
  },

  "output_schema": {
    "page_id": "string"
  },

  "permissions": [
    "network"
  ],

  "dependencies": [
    "browser_runtime"
  ],

  "cost": {
    "llm_required": false
  },

  "status": "VERIFIED",

  "source": {
    "module": "tools.browser",
    "function": "browser_open"
  }
}

Ese fingerprint es muchísimo más útil que almacenar documentación completa.


---

8. Fragmentar grandes capacidades

Esto es fundamental para tu arquitectura.

Hermes puede tener una capacidad enorme:

BROWSER

YAIWES no debería registrar simplemente:

Hermes sabe navegador.

Debe romperla:

browser.open
browser.read
browser.click
browser.type
browser.download
browser.screenshot
browser.inspect

Igual:

EMAIL

se fragmenta:

email.search
email.read
email.draft
email.send
email.reply

Esto permite al Task-OS solicitar exactamente una función.


---

9. Capability Graph

Después construiría un grafo.

HERMES
 ├── browser
 │    ├── open
 │    ├── click
 │    └── screenshot
 │
 ├── files
 │    ├── read
 │    └── write
 │
 └── terminal
      ├── execute
      └── process_manage

OpenClaw:

OPENCLAW
 ├── tools
 ├── skills
 ├── plugins
 ├── automation
 ├── code_mode
 └── ...

Y luego unificas conceptos:

Hermes.browser_open ─┐
OpenClaw.browser     ├→ CAPABILITY:BROWSER_OPEN
Codex.browser_X      ┘

Eso permite sustituir un sistema por otro.


---

10. Registry universal de YAIWES

El resultado final no debería ser:

Hermes capabilities
OpenClaw capabilities
Codex capabilities

sino:

YAIWES CAPABILITY REGISTRY

Por ejemplo:

{
  "BROWSER_OPEN": {
    "providers": [
      "hermes",
      "openclaw"
    ]
  },

  "FILE_READ": {
    "providers": [
      "hermes",
      "openclaw",
      "codex"
    ]
  },

  "CODE_REFACTOR": {
    "providers": [
      "codex",
      "claude_code"
    ]
  }
}

Entonces el Task-OS simplemente dice:

REQUIRES:
BROWSER_OPEN
SCREENSHOT
FILE_READ

No dice necesariamente:

usa Hermes

El Dispatcher puede seleccionar quién proporciona esas capacidades.


---

Estructura del motor

Yo lo haría pequeño:

capability_engine/
├── static_scanner.py
├── registry_scanner.py
├── plugin_scanner.py
├── skill_scanner.py
├── workflow_scanner.py
├── dependency_checker.py
├── probe_runner.py
├── normalizer.py
├── graph_builder.py
└── registry.db

Y la regla más importante sería:

NO confiar en documentación solamente.

Cada capacidad pasa por:

DESCUBRIR → EXTRAER → NORMALIZAR → COMPROBAR DEPENDENCIAS → PROBAR → REGISTRAR

Cómo se conecta con tu Microkernel

Aquí es donde se vuelve muy útil:

TAREA
 ↓
MICROKERNEL
 ↓
"necesito:
 browser.open
 screenshot
 visual.verify"
 ↓
CAPABILITY SEARCH ENGINE
 ↓
Registry
 ↓
encuentra:
 Hermes.browser_open
 OpenClaw.screenshot
 YAIWES.visual_verify
 ↓
compone Task-OS

Así el Microkernel no necesita conocer Hermes ni OpenClaw internamente.

Solo conoce capacidades normalizadas.

Microflujo completo

HERMES / OPENCLAW / CODEX → CAPABILITY DISCOVERY → TOOLS + SKILLS + PLUGINS + WORKFLOWS → FRAGMENTAR → PROBAR → FINGERPRINT → CAPABILITY GRAPH → YAIWES REGISTRY → TASK-OS BUSCA CAPACIDAD → SELECCIONA PROVEEDOR → TRIGGER

Y añadiría una propiedad especialmente importante:

LLM_REQUIRED = true/false

porque muchas capacidades internas de esos sistemas pueden ejecutarse directamente como código/tool sin encender la LLM. El buscador de YAIWES debería preferir:

CODE DIRECTO → TOOL DIRECTO → WORKFLOW DETERMINISTA → y solo finalmente LLM.

[Referencia actual de tools de Hermes](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/reference/tools-reference.md?utm_source=chatgpt.com)
[Sistema de plugins de Hermes](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/user-guide/features/plugins.md?utm_source=chatgpt.com)
[Mapa de tools, skills y plugins de OpenClaw](https://github.com/openclaw/openclaw/blob/main/docs/tools/index.md?utm_source=chatgpt.com)


Sí. Se puede convertir en un motor universal sin LLM que descubra, fragmente, relacione y registre automáticamente prácticamente todas las capacidades visibles de Hermes, OpenClaw u otro sistema.

La condición importante es esta: “sin code” debe significar sin escribir código específico para cada agente. El motor universal sí necesita programarse una vez. Después debería poder conectarse a repositorios/sistemas nuevos y descubrirlos automáticamente mediante introspección.

Motor: Universal Capability Harvester

Su objetivo sería:

SISTEMA DESCONOCIDO → DESCUBRIR → EXTRAER → CLASIFICAR → RELACIONAR → COMPONER WORKFLOWS → VERIFICAR → REGISTRAR

Sin preguntar nada a una LLM.

1. Descubrimiento de superficies

Primero no intenta entender el significado profundo. Localiza automáticamente todas las superficies ejecutables:

Python modules
CLI commands
functions
classes
decorators
entry_points
OpenAPI
JSON Schema
MCP tools
plugins
skills
hooks
workflows
YAML
JSON
TOML
package metadata
routes HTTP
event handlers
schedulers

Por ejemplo:

Hermes/
├─ tools/
├─ plugins/
├─ skills/
├─ commands/
└─ workflows/

No necesitas decirle manualmente dónde está cada capacidad.


---

2. Introspección sin ejecutar LLM

Para Python utilizaría principalmente ast.

No importa cómo se llame la función.

El scanner descubre:

def send_email(...)
def browser_open(...)
def execute_shell(...)

pero también:

@tool(...)
@plugin(...)
@command(...)

y llamadas:

registry.register(...)
tools.add(...)
router.mount(...)

Produce:

{
  "symbol": "send_email",
  "type": "function",
  "inputs": ["recipient", "subject", "body"],
  "module": "email/tools.py"
}


---

3. Scanner de contratos

El motor busca contratos ya existentes antes de analizar código.

Prioridad:

MCP schema
OpenAPI
JSON Schema
plugin manifest
skill manifest
CLI metadata
Python signature
AST

Porque si encuentra:

{
  "name": "send_email",
  "inputSchema": {
    "to": "string",
    "body": "string"
  }
}

ya tiene una capacidad estructurada.

No necesita interpretarla con IA.


---

4. Unificación automática

Hermes podría llamarla:

send_message

OpenClaw:

email_send

otro sistema:

gmail.dispatch

El motor necesita convertirlas al namespace YAIWES:

communication.email.send

Esto puede hacerse determinísticamente con:

nombres;

rutas;

firmas;

schemas;

dependencias;

tags;

diccionario de sinónimos;

patrones Aho-Corasick;

BM25;

reglas.


Ejemplo:

send + recipient + subject + body
            ↓
communication.email.send

No necesariamente requiere embeddings ni LLM.


---

5. Descubrir workflows automáticamente

Aquí está la parte más interesante.

No basta descubrir:

browser.open
browser.click
browser.download

Hay que descubrir que existe:

LOGIN_TO_SITE

compuesto por:

browser.open
→ browser.type
→ browser.click
→ browser.wait
→ browser.read

Para eso el motor construye un Call Graph.

Analiza quién llama a quién:

workflow_login()
    │
    ├→ browser_open()
    ├→ type_text()
    ├→ click()
    └→ wait()

Y produce:

{
  "capability": "browser.login",
  "type": "workflow",
  "requires": [
    "browser.open",
    "browser.type",
    "browser.click",
    "browser.wait"
  ]
}


---

6. Descubrimiento recursivo

Tiene que hacerlo recursivamente.

Supongamos:

WORKFLOW A
   ↓
SKILL B
   ↓
PLUGIN C
   ↓
TOOL D
   ↓
API E

El Harvester genera:

CAPABILITY A
│
├─ requires B
│   └─ requires C
│       └─ requires D
│           └─ requires E

Esto permite saber no solo:

> puede ejecutar A



sino:

> qué necesita exactamente para ejecutar A.




---

7. Dependency Graph

Cada capacidad queda representada como un grafo.

Ejemplo:

SEND_REPORT
│
├── search.web
├── file.read
├── document.generate
└── email.send
      ├── smtp
      └── credential.email

Entonces YAIWES puede determinar:

search.web          ✅
file.read           ✅
document.generate   ✅
email.send          ❌ credencial

Resultado:

SEND_REPORT = BLOCKED
reason = missing email credential

Sin probar a ciegas.


---

8. Capability Fingerprint automático

Cada capacidad descubierta termina normalizada:

{
  "id": "CAP-000428",

  "canonical": "browser.screenshot",

  "provider": "openclaw",

  "type": "tool",

  "inputs": {
    "page": "page_reference"
  },

  "outputs": {
    "image": "file"
  },

  "requires": [
    "browser.runtime"
  ],

  "permissions": [
    "network",
    "filesystem.write"
  ],

  "llm_required": false,

  "source": {
    "file": "tools/browser.ts",
    "symbol": "screenshot"
  },

  "status": "DISCOVERED"
}


---

9. Muy importante: detectar si realmente necesita LLM

El motor debería clasificar:

CODE_ONLY
TOOL_ONLY
WORKFLOW_ONLY
LLM_REQUIRED
OPTIONAL_LLM
UNKNOWN

Ejemplo:

browser.screenshot
→ CODE_ONLY

files.copy
→ CODE_ONLY

search.web
→ TOOL_ONLY

workflow.download_extract
→ WORKFLOW_ONLY

summarize_ambiguous_document
→ posiblemente LLM_REQUIRED

Esto conecta perfectamente con tu idea de reducir llamadas.

YAIWES siempre escogería:

CODE → WORKFLOW → TOOL → LLM

en ese orden cuando las capacidades sean equivalentes.


---

10. Dynamic Probe

Descubrir no significa confiar.

El motor crea automáticamente una prueba pequeña para capacidades seguras:

file.read
→ archivo temporal

file.write
→ sandbox

browser.open
→ localhost

calculator
→ 2+2

archive.extract
→ zip temporal

Después cambia:

DISCOVERED
↓
LOADABLE
↓
TESTED
↓
VERIFIED

Las capacidades destructivas no se ejecutan automáticamente.


---

11. Dedupe

Probablemente descubrirás cientos de duplicados:

Hermes.file_read
OpenClaw.read_file
Codex.fs_read
YAIWES.file.read

El motor los agrupa:

CANONICAL CAPABILITY:
filesystem.read

y conserva proveedores:

filesystem.read
├─ Hermes
├─ OpenClaw
├─ Codex
└─ YAIWES-native


---

12. Descubrir capacidades nuevas por composición

Aquí puede volverse muy poderoso sin LLM.

Supongamos que no existe:

DOWNLOAD_AND_EXTRACT

pero existen:

http.download
archive.detect
archive.extract
file.move

Las firmas encajan:

URL
 ↓
download
 ↓ FILE
detect
 ↓ ARCHIVE_TYPE
extract
 ↓ FILES

El motor puede detectar que las salidas y entradas son compatibles.

Entonces crea un candidato:

COMPOSITE-CAPABILITY-91

http.download
→ archive.detect
→ archive.extract

Esto es composición automática de workflow sin LLM.


---

13. Cómo hacerlo sin código específico por sistema

La clave sería construir extractores genéricos:

harvester/
├── python_ast.py
├── javascript_ast.py
├── openapi.py
├── mcp.py
├── jsonschema.py
├── cli.py
├── manifest.py
├── package_metadata.py
├── filesystem.py
└── generic_graph.py

No:

hermes_scanner.py
openclaw_scanner.py
codex_scanner.py

Eso sería volver al problema manual.


---

14. El motor completo

UNIVERSAL CAPABILITY HARVESTER
                            │
                            ▼
                 DISCOVERY SCANNER
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
      CODE              MANIFESTS            APIs
   AST / imports       YAML/JSON/TOML     MCP/OpenAPI/CLI
        └───────────────────┼───────────────────┘
                            ▼
                    SYMBOL EXTRACTOR
                            ▼
                      CALL GRAPH
                            ▼
                    DEPENDENCY GRAPH
                            ▼
                 CAPABILITY CLASSIFIER
                            ▼
                     NORMALIZER
                            ▼
                        DEDUPE
                            ▼
                   WORKFLOW DETECTOR
                            ▼
                 COMPOSITION ENGINE
                            ▼
                    SAFE PROBE ENGINE
                            ▼
                 CAPABILITY REGISTRY


---

15. Cómo se conecta después con el Microkernel

Esto elimina otro trabajo cognitivo.

El Microkernel recibe:

TAREA:
descargar ZIP y extraerlo

Su clasificador produce:

#download
#archive
#extract

Consulta:

Capability Registry

y encuentra:

CAP-91 = download_and_extract

requires:
http.download
archive.extract

LLM_REQUIRED = false
VERIFIED = true

Entonces:

TAREA
→ TEMPLATE TASK-OS
→ insertar CAP-91
→ ejecutar

0 llamadas LLM.


---

La mejora que yo añadiría

Además del Capability Registry, crearía un:

Capability Genome

Una representación extremadamente pequeña:

filesystem.read:
 IN=file_ref
 OUT=bytes
 COST=1
 RISK=1

archive.extract:
 IN=bytes/archive
 OUT=files[]
 COST=2
 RISK=2

Eso permite que algoritmos como:

A*;

Dijkstra;

CP-SAT;

Z3;


calculen automáticamente qué combinación de capacidades puede transformar INPUT → OUTPUT esperado.

Entonces el sistema no solo descubriría capacidades.

Podría también descubrir:

> qué puede lograr combinándolas.



Microflujo final

SISTEMA NUEVO → HARVEST → EXTRAER CAPACIDADES → CALL GRAPH → DEPENDENCIAS → NORMALIZAR → DEDUPE → VERIFICAR → REGISTRY → COMBINAR INPUT/OUTPUT → DESCUBRIR WORKFLOWS POSIBLES → TASK-OS PUEDE UTILIZARLOS

Eso convertiría Hermes/OpenClaw/etc. prácticamente en bibliotecas de capacidades que YAIWES desarma, clasifica y reutiliza, en lugar de tratarlos como agentes monolíticos.



Sí. Ese mismo motor puede extraer no solo tools y skills, sino también workflows completos y sistemas LOOP de un agente, siempre que esos flujos estén representados de alguna forma observable en su código, configuración o ejecución.




La idea sería crear un Workflow/Loop Extractor encima del Capability Discovery Engine.

Qué puede extraer



Puede detectar cosas como:

secuencias de funciones,

ciclos while/for,

retries,

condiciones if/else,

state machines,

DAGs,

callbacks,

hooks,

timers,

watchdogs,

colas,

eventos,

chains,

pipelines,

subworkflows,

patrones PLAN → EXECUTE → VERIFY → RETRY,

y dependencias entre tools/plugins/skills.


Por ejemplo, si Hermes internamente hace:

while not done:
    research()
    analyze()
    execute_tool()
    verify()

    if failed:
        retry()

el extractor puede convertirlo en algo así:

LOOP-17

START
 ↓
RESEARCH
 ↓
ANALYZE
 ↓
EXECUTE
 ↓
VERIFY
 ├─ PASS → CLOSE
 └─ FAIL → RETRY ↺

Y después guardarlo como un workflow reutilizable:

{
  "workflow_id": "WF-17",
  "type": "loop",
  "steps": [
    "research",
    "analyze",
    "execute",
    "verify"
  ],
  "transitions": {
    "verify.pass": "close",
    "verify.fail": "research"
  }
}

Cómo lo descubre

Usaría cuatro capas.

1. AST / código estático. Busca while, for, if, try/retry, llamadas entre funciones, decorators, callbacks y state enums.

2. Call Graph. Reconstruye:

main()
 → plan()
 → tool()
 → verify()
 → retry()

3. Control Flow Graph. Aquí descubre el orden real:

A → B → C
        ↓
       FAIL
        ↓
        B

Esto permite identificar LOOPs automáticamente.

4. Runtime Trace opcional. Si el flujo se construye dinámicamente, ejecutas el sistema en sandbox y registras:

EVENT 01 call search
EVENT 02 call analyze
EVENT 03 call tool
EVENT 04 verify FAIL
EVENT 05 call analyze

Entonces el motor infiere:

ANALYZE → TOOL → VERIFY → ANALYZE

como ciclo.

Lo más útil para YAIWES

No guardaría el workflow extraído como código original.

Lo normalizaría a un DSL universal YAIWES.

Ejemplo:

{
  "id": "WF-HERMES-023",
  "entry": "SEARCH",

  "states": {
    "SEARCH": {
      "op": "web.search",
      "next": "ANALYZE"
    },

    "ANALYZE": {
      "op": "reason",
      "next": "EXECUTE"
    },

    "EXECUTE": {
      "op": "tool.call",
      "next": "VERIFY"
    },

    "VERIFY": {
      "PASS": "CLOSE",
      "FAIL": "ANALYZE"
    }
  }
}

Entonces ese workflow deja de pertenecer a Hermes.

Pasa a ser:

YAIWES.WF-023

y el Task-OS puede reutilizarlo con otro proveedor.

Incluso puede separar la LLM del LOOP

Esto encaja perfectamente con tu arquitectura.

Supongamos que el workflow original es:

LLM
→ buscar
→ LLM
→ ejecutar
→ LLM
→ verificar
→ LLM
→ repetir

El extractor puede descubrir que realmente la estructura es:

SEARCH
→ ANALYZE
→ EXECUTE
→ VERIFY
↺

Y YAIWES puede reconstruirlo así:

SEARCH = motor code
ANALYZE = LLM solo si es necesaria
EXECUTE = tool/code
VERIFY = motor determinista
LOOP = Python

Resultado:

la LLM deja de controlar el LOOP.

El LOOP pasa a ser software.

También puede descubrir workflows ocultos por composición

Ejemplo:

function A
 → skill B
 → plugin C
 → tool D

el motor podría producir:

WF-A
 ├─ CAP-B
 ├─ CAP-C
 └─ CAP-D

y además:

INPUT
→ B
→ C
→ D
→ OUTPUT

Limitación importante

No siempre puedes recuperar el workflow exacto al 100%.

Si el sistema construye dinámicamente decisiones en runtime o deja que una LLM improvise la próxima acción, solo puedes extraer:

partes deterministas,

patrones observados,

trazas,

límites,

tools usados,

ciclos frecuentes.


En esos casos marcaría:

STATIC_CONFIDENCE = 100%
DYNAMIC_CONFIDENCE = 82%
LLM_DEFINED_BRANCH = UNKNOWN

y no inventaría la parte que no existe en código.

Motor completo

AGENTE → AST → CALL GRAPH → CONTROL FLOW GRAPH → LOOP DETECTOR → STATE/DAG EXTRACTOR → TOOL/SKILL DEPENDENCIES → RUNTIME TRACE → NORMALIZER → YAIWES DSL → REGISTRY

Y eso te permitiría hacer algo muy potente:

> desmontar Hermes/OpenClaw en capacidades + workflows + LOOPs reutilizables y convertirlos en piezas del sistema operativo YAIWES, sin depender del agente completo.
 Sí. La diferencia importante es el parser del lenguaje, no el diseño del motor.

A día de hoy, Hermes Agent es principalmente Python y OpenClaw está construido principalmente sobre TypeScript/JavaScript con Node.js. Hermes se instala y usa como librería Python; OpenClaw tiene tsconfig.json, módulos .ts/.mts/.mjs y runtime Node.  

1. No haría dos motores distintos

Haría:

UNIVERSAL CAPABILITY HARVESTER
              │
      detectar lenguaje
              │
     ┌────────┴────────┐
     ↓                 ↓
 Python Parser    TS/JS Parser
     │                 │
     └────────┬────────┘
              ↓
       MISMO IR YAIWES
              ↓
     Capability Registry

Es decir: cambia solamente cómo extraes el código.

Después todo se transforma al mismo formato interno.


---

2. Hermes → parser Python

Para Hermes:

.py
pyproject.toml
plugins
skills
registries
decorators
imports

Usaría el módulo estándar:

ast

El AST permite descubrir:

FunctionDef
ClassDef
Call
Import
If
For
While
Try
Return
decorators

Por ejemplo:

while not complete:
    search()
    execute()
    verify()

se puede convertir automáticamente en:

LOOP
├─ search
├─ execute
└─ verify
     ├─ PASS → CLOSE
     └─ FAIL → LOOP

Hermes además tiene una arquitectura extensible mediante plugins y skills, así que estos registros también deben escanearse aparte del AST. 


---

3. OpenClaw → parser TypeScript/JavaScript

OpenClaw requiere otra puerta porque trabaja principalmente con el ecosistema Node y TypeScript. Su configuración TypeScript usa módulos NodeNext, target ES2023 y rutas hacia numerosos paquetes internos. 

Aquí no usarías ast de Python.

Usaría un parser TypeScript como:

TypeScript Compiler API

o:

tree-sitter-typescript

Debe reconocer:

FunctionDeclaration
ArrowFunction
ClassDeclaration
CallExpression
ImportDeclaration
AwaitExpression
IfStatement
ForStatement
WhileStatement
SwitchStatement
Promise
Event handlers

Por ejemplo:

async function workflow() {
   await browser.open();
   const r = await inspect();

   if (!r.ok) {
      await repair();
   }

   await verify();
}

se normaliza a:

OPEN
 ↓
INSPECT
 ↓
PASS?
 ├─ NO → REPAIR
 └─ YES
 ↓
VERIFY

OpenClaw además posee un Gateway que centraliza sesiones, tools, eventos y conexiones, así que esos registros son otra fuente para descubrir capacidades sin depender solamente de analizar texto fuente. 


---

4. El truco: convertir ambos a un IR universal

Esta es la pieza realmente importante.

No deberías guardar:

Python AST Hermes
TypeScript AST OpenClaw

como representación final.

Ambos parsers deben producir:

YAIWES INTERMEDIATE REPRESENTATION

Por ejemplo:

{
  "id": "WF-182",
  "type": "workflow",

  "nodes": [
    {"id":"N1","op":"browser.open"},
    {"id":"N2","op":"browser.inspect"},
    {"id":"N3","op":"repair"},
    {"id":"N4","op":"verify"}
  ],

  "edges": [
    {"from":"N1","to":"N2"},
    {"from":"N2","condition":"FAIL","to":"N3"},
    {"from":"N2","condition":"PASS","to":"N4"},
    {"from":"N3","to":"N4"}
  ]
}

Da igual si originalmente vino de:

Python
TypeScript
JavaScript
Go
Rust
Java

YAIWES solo ve ese IR.


---

5. Harvester por adaptadores de lenguaje

Yo lo estructuraría así:

capability_harvester/
│
├── language_detector.py
│
├── parsers/
│   ├── python_parser.py
│   ├── typescript_parser.py
│   ├── javascript_parser.py
│   ├── go_parser.py
│   ├── rust_parser.py
│   └── generic_parser.py
│
├── extractors/
│   ├── function_extractor.py
│   ├── tool_extractor.py
│   ├── workflow_extractor.py
│   ├── loop_extractor.py
│   └── dependency_extractor.py
│
├── normalizer/
│   └── yaiwes_ir.py
│
└── registry/
    └── capabilities.db

Pero incluso esto se puede simplificar bastante.


---

6. Mejor opción: Tree-sitter

Para tu objetivo yo estudiaría seriamente Tree-sitter, porque evita construir manualmente un parser completamente distinto para cada lenguaje.

URL visible:

https://github.com/tree-sitter/tree-sitter

Tree-sitter tiene gramáticas para muchos lenguajes.

Entonces:

Hermes .py
      ↓
Tree-sitter Python

OpenClaw .ts
      ↓
Tree-sitter TypeScript

otro proyecto .go
      ↓
Tree-sitter Go

Todos producen árboles sintácticos navegables.

Después YAIWES busca conceptos universales:

FUNCTION
CALL
LOOP
CONDITION
RETURN
IMPORT
CLASS
ASYNC CALL


---

7. Dos niveles de extracción

No dependería solamente del lenguaje.

NIVEL A — código

AST
CFG
Call Graph
Loops
Functions
Classes
Imports

NIVEL B — contratos del framework

Busca directamente:

MCP definitions
OpenAPI
JSON Schema
plugin manifests
package.json
pyproject.toml
CLI definitions
skills
workflow YAML
registries
hooks

Nivel B normalmente es más fiable porque ya declara qué es una herramienta.


---

8. Ejemplo Hermes

Archivo Python:

def research():
    search()
    download()
    summarize()

Scanner:

FUNCTION research
 CALL search
 CALL download
 CALL summarize

IR:

CAPABILITY research

search
 ↓
download
 ↓
summarize


---

9. Ejemplo OpenClaw

TypeScript:

export async function research() {
   await search();
   await download();
   return summarize();
}

Scanner:

FUNCTION research
 CALL search
 CALL download
 CALL summarize

IR final:

CAPABILITY research

search
 ↓
download
 ↓
summarize

Exactamente el mismo resultado.

La procedencia deja de importar.


---

10. Lo mismo para LOOP

Hermes:

while not passed:
    test()
    repair()

OpenClaw:

while (!passed) {
   await test();
   await repair();
}

Ambos terminan en:

{
  "type": "LOOP",
  "condition": "NOT_PASS",
  "body": [
    "test",
    "repair"
  ]
}

Y ese LOOP ya puede pasar al Registry YAIWES.


---

11. Luego puedes llegar a cualquier lenguaje

El motor crecería así:

PYTHON ───────┐
TYPESCRIPT ───┤
JAVASCRIPT ───┤
GO ───────────┤
RUST ─────────┤
JAVA ─────────┤
C/C++ ────────┤
              ↓
          YAIWES IR
              ↓
 CAPABILITY / WORKFLOW / LOOP
              ↓
       COMPONENT REGISTRY

Por eso no conviene que el Capability Engine sea Python-céntrico ni OpenClaw-céntrico.

Debe ser:

> multi-language in → canonical YAIWES IR out.



Lo que recomiendo

Para el MVP:

Python: AST nativo de Python.
TypeScript/JavaScript: Tree-sitter o TypeScript Compiler API.
Todos los demás: Tree-sitter progresivamente.

Y después una única cadena:

SOURCE → AST → CALL GRAPH → CONTROL FLOW → LOOP/WORKFLOW DETECTOR → YAIWES IR → CAPABILITY REGISTRY

Eso permitiría desmontar Hermes y OpenClaw aunque estén escritos en lenguajes distintos y terminar con el mismo catálogo universal de capabilities, tools, skills, workflows y LOOPs.




