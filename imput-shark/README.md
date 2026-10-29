# Imput Sharck - Sistema de Búsqueda y Control de Input para Modelos

## Arquitectura

Este repositorio contiene los motores y componentes para gestionar el input, búsqueda de contexto y control de flujo de modelos de lenguaje. Reorganizado desde `router-universal-router-inteligente-/chat-router/motores/`.

### 📂 Code imput sharck
Código core cableado y funcional:

- **evidencia/**: Buscadores, extractores, compiladores de búsqueda, ranking y verificación de evidencia. ✅ Transferido
- **fabrica-motores/**: Motores de canvas, layout, QA, flujo de acciones, capacidades y sandbox. ✅ Transferido (8 archivos + tests)
- **motores-descarga/**: Descarga y extracción de archivos desde HuggingFace y otras fuentes. ✅ Transferido (3 archivos)
- **archivos/**: Motor de archivos en cola (descarga, extracción, copia, movimiento, listado y búsqueda). ✅ Transferido (3 archivos)

### 📂 Componentes imput sharck para integrar
Componentes desacoplados candidatos a integración:

- **busqueda-contexto/**: Búsqueda de contexto para enriquecimiento de prompts. ✅ Transferido (6 archivos)
- **descarga-copia/**: Utilidades de descarga y copia de recursos. ⚠️ Placeholders creados; contenido real pendiente de completar
- **motores-caso/**: Motores específicos por caso de uso. ✅ Transferido (motor_openclaw_deref_symlinks.py)

### ❌ Excluido (sistema de memoria/almacenamiento)
- `memoria/` y subcarpetas pertenecen al sistema de almacenamiento y memoria del router, NO a imput sharck. Se mantienen en `chat-router/memoria/` del repo origen.

## Handoff

### Estado Final
| Módulo | Estado | Archivos |
|--------|--------|----------|
| evidencia/ | ✅ Completo | 9 + tests |
| fabrica-motores/ | ✅ Completo | 8 + tests |
| motores-descarga/ | ✅ Completo | 3 |
| archivos/ | ✅ Completo | 3 |
| busqueda-contexto/ | ✅ Completo | 6 |
| descarga-copia/ | ⚠️ Placeholders | 3 (pendiente contenido real) |
| motores-caso/ | ✅ Completo | 1 |
| memoria/ | ❌ Excluido | N/A |

### Próximos Pasos
1. Completar contenido real de `descarga-copia/` (leer origen y reescribir).
2. Integrar componentes de `Componentes imput sharck para integrar/` en el flujo principal según necesidad.
3. Documentar APIs y contratos de cada motor.
4. Establecer pruebas de integración entre motores.
5. Migrar referencias de `plugins/puente_chat/` para usar estos motores centralizados.

### Notas de Integración
- Los motores en `Code imput sharck/` están cableados y son funcionales.
- Los componentes en `Componentes imput sharck para integrar/` requieren adaptación antes de su uso.
- El sistema de memoria/almacenamiento se mantiene separado en `chat-router/memoria/` del repo origen.
- La transferencia se realizó vía `github_leer` + `github_escribir` debido a bloqueo del motor de archivos en colas largas.

## Índice de Contenidos

### Code imput sharck
| Módulo | Descripción | Estado |
|--------|-------------|--------|
| evidencia/ | Buscadores, extractores, ranking | ✅ Transferido |
| fabrica-motores/ | Canvas, layout, QA, action flow, capability, sandbox | ✅ Transferido |
| motores-descarga/ | Descarga HF y extracción | ✅ Transferido |
| archivos/ | Motor de archivos en cola | ✅ Transferido |

### Componentes imput sharck para integrar
| Componente | Descripción | Estado |
|------------|-------------|--------|
| busqueda-contexto/ | Enriquecimiento de contexto (web, github, hf) | ✅ Transferido |
| descarga-copia/ | Copia y movimiento por lotes | ⚠️ Placeholders |
| motores-caso/ | Motores por caso de uso (openclaw) | ✅ Transferido |

---
*Generado automáticamente durante reorganización desde router-universal-router-inteligente-*
*Fecha: 2025-01-28*
*Modelo: qwen3.8-max*
