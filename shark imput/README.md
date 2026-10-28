# Imput Sharck — Sistema de Búsqueda y Control de Input para Modelos

Repositorio unificado que consolida el código activo y los componentes integrables relacionados con la gestión de input, búsqueda de contexto y control de flujo para modelos de lenguaje.

## Estructura Actual

```
shark imput/
├── imput shark core/               # Código cableado y operativo (Code_imput_sharck)
│   ├── ➡️📂 shart imput code Run/  # Runtime y ejecución
│   ├── 📂 component acquisition/   # Adquisición de componentes
│   ├── 📂 root-only-runtime/       # Runtime mínimo
│   └── 📂 sharck-v3-parallel-candidate/ # Candidatos paralelos v3
└── componentes por integrar/       # Componentes desacoplados (Componentes_imput_sharck_para_integrar)
    ├── FlagEmbedding/, LLMLingua/, bm25s/, fastembed/  # Embeddings y búsqueda semántica
    ├── Perplexica/, searxng/, khoj/                    # Motores de búsqueda externos
    ├── anthropic-skills/, openai-skills/, huggingface-skills/ # Skills de proveedores
    ├── phoenix/, guardrails/, ragas/                   # Evaluación y seguridad
    ├── playwright/, crawl4ai/, trafilatura/            # Web scraping y extracción
    ├── spaCy/, tesseract/, whisperX/                   # NLP y procesamiento multimodal
    ├── duckdb/, datasketch/, ranx/                     # Bases de datos y ranking
    └── ... (ver lista completa en carpeta)
```

## Clasificación Aplicada

- **imput shark core**: Todo lo relacionado con búsqueda, control de input, evidencia y motores operativos. Incluye runtime, adquisición de componentes y candidatos paralelos.
- **componentes por integrar**: Librerías y herramientas externas no cableadas al MVP actual. Son candidatos para integrar como backend de contexto, búsqueda o persistencia.

## Handoff e Integración

### Para imput shark core
El núcleo contiene:
- Runtime de ejecución (`➡️📂 shart imput code Run/`)
- Adquisición de componentes (`📂 component acquisition/`)
- Candidatos para paralelización v3 (`📂 sharck-v3-parallel-candidate/`)

**Próximos pasos**: 
1. Integrar motores de `router-universal-router-inteligente-/chat-router/motores/` aquí.
2. Exponer vía MCP y Harness del MVP.
3. Validar compatibilidad con runtime existente.

### Para componentes por integrar
Ya contiene 37+ librerías clasificadas. Para integrar:
1. Definir contrato de integración (API de guardar/buscar contexto).
2. Priorizar: embeddings (FlagEmbedding, fastembed), búsqueda (Perplexica, searxng), evaluación (ragas, guardrails).
3. Conectar con `puente_chat` o nuevo loader de memoria.

## Índice de Archivos Clave (Pendiente de Actualizar)

| Categoría | Ejemplos | Estado |
|-----------|----------|--------|
| Embeddings | FlagEmbedding, fastembed, bm25s | Por integrar |
| Búsqueda | Perplexica, searxng, khoj | Por integrar |
| Skills | anthropic-skills, openai-skills | Por integrar |
| Evaluación | ragas, guardrails, phoenix | Por integrar |
| Extracción | crawl4ai, trafilatura, playwright | Por integrar |
| NLP | spaCy, tesseract, whisperX | Por integrar |

## Notas de Migración

- Este repo se está consolidando desde `router-universal-router-inteligente-/chat-router/`.
- Los motores de búsqueda/evidencia/fabrica deben copiarse a `imput shark core/`.
- Los sistemas de memoria (`memoria-yaiwes`, `hf_datasets`) deben evaluarse contra componentes existentes.
- Para desarrollo futuro, trabajar sobre esta estructura unificada.

---
*Generado durante reorganización. Mejorar con detalles específicos de integración tras completar transferencia.*
