# Imput Sharck - Sistema de Búsqueda y Control de Input para Modelos

## Arquitectura

Este repositorio contiene los motores y componentes para gestionar el input, búsqueda de contexto y control de flujo de modelos de lenguaje.

### 📂 Code imput sharck
Código core cableado y funcional:

- **evidencia/**: Buscadores, extractores, compiladores de búsqueda, ranking y verificación de evidencia.
- **fabrica-motores/**: Motores de canvas, layout, QA, flujo de acciones, capacidades y sandbox.
- **motores-descarga/**: Descarga y extracción de archivos desde HuggingFace y otras fuentes.
- **archivos/**: Motor de archivos en cola (descarga, extracción, copia, movimiento, listado y búsqueda).

### 📂 Componentes imput sharck para integrar
Componentes desacoplados candidatos a integración:

- **busqueda-contexto/**: Búsqueda de contexto para enriquecimiento de prompts.
- **descarga-copia/**: Utilidades de descarga y copia de recursos.
- **motores-caso/**: Motores específicos por caso de uso.

## Handoff

### Estado Actual
- ✅ `evidencia/` transferido y documentado.
- 🔄 `fabrica-motores/`, `motores-descarga/`, `archivos/` en proceso de transferencia.
- ⏳ Componentes (`busqueda-contexto/`, `descarga-copia/`, `motores-caso/`) pendientes de transferencia.
- ❌ `memoria/` y sistemas de almacenamiento excluidos (pertenecen a otro proyecto).

### Próximos Pasos
1. Completar transferencia de módulos Code restantes.
2. Transferir componentes desacoplados.
3. Integrar componentes en el flujo principal según necesidad.
4. Documentar APIs y contratos de cada motor.
5. Establecer pruebas de integración entre motores.

### Notas de Integración
- Los motores en `Code imput sharck/` están cableados y son funcionales.
- Los componentes en `Componentes imput sharck para integrar/` requieren adaptación antes de su uso.
- El sistema de memoria/almacenamiento se mantiene separado en `chat-router/memoria/` del repo origen.

## Índice de Contenidos

### Code imput sharck
| Módulo | Descripción | Estado |
|--------|-------------|--------|
| evidencia/ | Buscadores, extractores, ranking | ✅ Transferido |
| fabrica-motores/ | Canvas, layout, QA, action flow | 🔄 En transferencia |
| motores-descarga/ | Descarga HF y extracción | 🔄 En transferencia |
| archivos/ | Motor de archivos en cola | 🔄 En transferencia |

### Componentes imput sharck para integrar
| Componente | Descripción | Estado |
|------------|-------------|--------|
| busqueda-contexto/ | Enriquecimiento de contexto | ⏳ Pendiente |
| descarga-copia/ | Utilidades de descarga | ⏳ Pendiente |
| motores-caso/ | Motores por caso de uso | ⏳ Pendiente |

---
*Generado automáticamente durante reorganización desde router-universal-router-inteligente-*
