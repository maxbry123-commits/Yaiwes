# Imput Sharck — Sistema de Búsqueda y Control de Input para Modelos

Repositorio unificado que consolida el código activo y los componentes integrables relacionados con la gestión de input, búsqueda de contexto y control de flujo para modelos de lenguaje.

## Estructura Actual

```
shark imput/
├── imput shark core/               # Código cableado y operativo (Code_imput_sharck)
│   ├── motores/                    # ✅ TRANSFERIDO: Motores de búsqueda y evidencia
│   │   └── evidencia/              # ✅ COMPLETO: buscadores, parser, ranking, puerta, verificador
│   │       ├── buscadores.py       # Fan-out multi-fuente (GitHub, URL, local, simulado)
│   │       ├── compilador_busquedas.py  # Compilación determinista de queries
│   │       ├── evidence_pack.py    # Empaquetado de evidencia con tope de tokens
│   │       ├── extractor.py        # Extracción de fragmentos por términos
│   │       ├── goals.py            # 12 Goals del Director (G01-G12)
│   │       ├── parser.py           # Parser determinista sin LLM
│   │       ├── puerta.py           # Puerta de Evidencia T07 (antes/despues)
│   │       ├── ranking.py          # BM25 + RRF + autoridad + recencia
│   │       ├── verificador.py      # Verificación independiente de claims
│   │       └── tests/              # Tests SIMULADO completos
│   ├── ➡️📂 shart imput code Run/  # Runtime y ejecución (existente)
│   ├── 📂 component acquisition/   # Adquisición de componentes (existente)
│   ├── 📂 root-only-runtime/       # Runtime mínimo (existente)
│   └── 📂 sharck-v3-parallel-candidate/ # Candidatos paralelos v3 (existente)
└── componentes por integrar/       # Componentes desacoplados (Componentes_imput_sharck_para_integrar)
    ├── FlagEmbedding/, LLMLingua/, bm25s/, fastembed/  # Embeddings y búsqueda semántica
    ├── Perplexica/, searxng/, khoj/                    # Motores de búsqueda externos
    ├── anthropic-skills/, openai-skills/, huggingface-skills/ # Skills de proveedores
    ├── phoenix/, guardrails/, ragas/                   # Evaluación y seguridad
    ├── playwright/, crawl4ai/, trafilatura/            # Web scraping y extracción
    ├── spaCy/, tesseract/, whisperX/                   # NLP y procesamiento multimodal
    ├── duckdb/, datasketch/, ranx/                     # Bases de datos y ranking
    └── ... (37+ librerías clasificadas)
```

## Estado de Transferencia

### ✅ Completado
- **evidencia/**: Módulo completo de búsqueda y verificación (9 archivos + tests)
- **README.md**: Documentación arquitectónica actualizada

### ⏳ Pendiente de Transferir
- **motores/fabrica-motores/**: Engines modulares (canvas, layout, QA, action_flow, capability, sandbox)
- **motores/motores-descarga/**: HF download/extract engines
- **motores/archivos/**: Tool `archivos` especificación
- **memoria/**: Sistemas de memoria no cableados (memoria-yaiwes, hf_datasets, arquitectura)

> Nota: El motor de archivos (`archivos` tool) presentó bloqueo persistente durante transferencia. Se usó escritura directa vía API para evidencia/. Los módulos restantes requieren reintentar cuando el motor esté disponible o continuar con escritura directa.

## Handoff e Integración

### Para imput shark core / motores / evidencia
El módulo `evidencia/` es **autocontenido y operativo**:
- **Entrada**: Texto en lenguaje natural → `parser.parse()` → estructura determinista
- **Búsqueda**: `compilador_busquedas.compilar()` → `buscadores.fanout()` → resultados normalizados
- **Ranking**: `ranking.rankear()` → BM25 + autoridad + recencia + RRF
- **Verificación**: `puerta.despues()` → PASS | INCOMPLETE | CONTRADICTION | FAIL
- **Tests**: Ejecutar con `SIMULADO=1 pytest -q` (cero red)

**Próximos pasos**:
1. Integrar `fabrica-motores/` para construir motores personalizados sobre esta base
2. Exponer vía MCP y Harness del MVP (Fase 6 según MAPA.md original)
3. Conectar con runtime existente en `➡️📂 shart imput code Run/`

### Para componentes por integrar
Ya contiene 37+ librerías clasificadas. Prioridades de integración:
1. **Embeddings**: FlagEmbedding, fastembed, bm25s → complementar `ranking.py`
2. **Búsqueda externa**: Perplexica, searxng → extender `buscadores.fanout()`
3. **Evaluación**: ragas, guardrails → validar calidad de evidencia
4. **Extracción**: crawl4ai, trafilatura → mejorar `extractor.py`

**Contrato de integración propuesto**:
```python
# Interfaz mínima para nuevos componentes
class SearchBackend:
    def search(self, query: str, top_k: int = 5) -> list[dict]:
        """Devuelve resultados normalizados: {url, title, snippet, source_type, date}"""
        ...

class MemoryBackend:
    def save(self, key: str, value: dict) -> None: ...
    def search(self, query: str, top_k: int = 5) -> list[dict]: ...
```

## Índice de Archivos Clave

| Módulo | Archivo | Función | Estado |
|--------|---------|---------|--------|
| evidencia | `buscadores.py` | Fan-out multi-fuente | ✅ Operativo |
| evidencia | `parser.py` | Parsing determinista | ✅ Operativo |
| evidencia | `ranking.py` | BM25 + RRF | ✅ Operativo |
| evidencia | `puerta.py` | Gate T07 antes/despues | ✅ Operativo |
| evidencia | `verificador.py` | Verificación independiente | ✅ Operativo |
| fabrica-motores | `engine.py` | Base motores custom | ⏳ Pendiente |
| motores-descarga | `hf_download_extract_engine.py` | HF download | ⏳ Pendiente |
| archivos | `tool.json` | Spec tool archivos | ⏳ Pendiente |

## Notas de Migración

- Este repo se consolidó desde `router-universal-router-inteligente-/chat-router/`.
- Los enlaces simbólicos originales NO se preservan; usar rutas directas.
- El código cableado en `chat/backend/mvp/` del repo original NO se movió.
- Para desarrollo futuro, trabajar sobre esta estructura unificada.
- **Modelo activo**: qwen3.8-max (Qwen/Alibaba) ejecutó esta transferencia.

---
*Última actualización: Transferencia evidencia/ completada. Módulos restantes pendientes de transferencia.*
