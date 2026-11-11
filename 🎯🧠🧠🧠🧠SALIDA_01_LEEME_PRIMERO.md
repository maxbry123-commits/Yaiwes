# Entrega 01/12 — MEMORY OS

Esta entrega contiene código real de **software determinista de memoria**. No contiene agentes ni bucles LLM.

Ruta de instalación: `chat-router/memoria/memory_os/` de `maxbry123-commits/router-universal-router-inteligente-`.

Documentación principal:

- `chat-router/memoria/memory_os/README.md`: instalación, ejemplos y límites.
- `chat-router/memoria/memory_os/docs/SALIDA_01_AUDITORIA_FUENTES.md`: auditoría del código YAIWES real, con rutas, líneas y SHA de origen.
- `chat-router/memoria/memory_os/docs/SALIDA_01_PODA_ADAPTACION.md`: instrucciones exactas de poda y adaptación.
- `chat-router/memoria/memory_os/docs/SALIDA_01_INTEGRACION.md`: cableado interno, planes de conexión y restauración.
- `chat-router/memoria/memory_os/docs/SALIDA_01_ARCHITECTURE_MATRIX.md`: cobertura de la arquitectura obligatoria.
- `chat-router/memoria/memory_os/docs/SOURCE_LEDGER_20_MD.md`: 20 documentos adjuntos con hashes y salidas correspondientes.
- `chat-router/memoria/memory_os/docs/SALIDA_01_RESULTADOS.md`: pruebas y funciones pendientes.

Para instalar en un clon local del repositorio, desde la raíz extraída de este ZIP:

```bash
python install_salida_01.py /ruta/al/repositorio
python install_salida_01.py /ruta/al/repositorio --apply
```

Por defecto el instalador no escribe. Rechaza sobrescrituras. NO modifica ningún archivo de código existente.

**Resultado local:** 17 tests aprobados, 1 prueba contra proveedor real omitida por no disponer del clon completo en el contenedor. No se ha desplegado.
