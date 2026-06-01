# Unit Test Mapping

## 1. Objetivo

Este documento identifica y clasifica las pruebas unitarias existentes en el proyecto Baby Buddy. Su propósito es proporcionar una línea base para actividades de auditoría, análisis de cobertura y mejora de calidad.

## 2. Alcance

Se incluyen únicamente pruebas unitarias automatizadas. No se consideran pruebas de integración, funcionales, de interfaz de usuario ni pruebas manuales.


## 3. Estructura del Directorio de Pruebas

Durante el proceso de auditoría se identificó la siguiente estructura dentro del directorio de pruebas del módulo analizado:

```text
tests/
├── import/
├── tests_forms.py
├── tests_import_export.py
├── tests_models.py
├── tests_templatetags.py
├── tests_utils.py
└── tests_views.py
```

### Archivos analizados

| Archivo                  | Descripción general                                                                                 |
| ------------------------ | --------------------------------------------------------------------------------------------------- |
| `tests_forms.py`         | Pruebas relacionadas con formularios y operaciones de creación, edición y eliminación de registros. |
| `tests_import_export.py` | Pruebas relacionadas con funcionalidades de importación y exportación de datos.                     |
| `tests_models.py`        | Pruebas relacionadas con modelos y lógica asociada.                                                 |
| `tests_templatetags.py`  | Pruebas relacionadas con etiquetas y filtros personalizados de plantillas.                          |
| `tests_utils.py`         | Pruebas relacionadas con funciones utilitarias.                                                     |
| `tests_views.py`         | Pruebas relacionadas con vistas y rutas de la aplicación.                                           |

La subcarpeta `import/` fue identificada como parte de la estructura del directorio de pruebas, pero no forma parte del presente análisis debido a que el alcance se limita a los archivos principales de prueba ubicados en la raíz del directorio `tests`.


## 3.1 Archivo: `test_forms.py`

### Resultado del análisis

Se realizó la revisión de las 46 pruebas automatizadas contenidas en el archivo `test_forms.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

Tras el análisis de su implementación y comportamiento, se determinó que el archivo no contiene pruebas unitarias puras. En consecuencia, ninguna de las pruebas definidas en este archivo forma parte del alcance del presente documento.

### Justificación de la clasificación

Las pruebas analizadas ejercen simultáneamente múltiples componentes de la aplicación, por lo que no aíslan una única unidad de código. Entre las características observadas se encuentran:

* Uso del cliente HTTP de Django (`django.test.Client`) para realizar solicitudes GET y POST.
* Creación, modificación y eliminación de registros en la base de datos de prueba.
* Verificación de respuestas HTTP completas, incluyendo códigos de estado y contenido generado.
* Interacción conjunta entre vistas, formularios, modelos y mecanismos de persistencia.

Debido a estas características, las pruebas se clasifican principalmente como pruebas de integración y pruebas funcionales, en lugar de pruebas unitarias.

### Clasificación identificada

| Tipo de prueba                      | Cantidad aproximada | Observaciones                                                                          |
| ----------------------------------- | ------------------- | -------------------------------------------------------------------------------------- |
| Pruebas de integración              | ~40                 | Operaciones de creación, edición y eliminación de entidades mediante solicitudes HTTP. |
| Pruebas funcionales de formularios  | ~6                  | Verificación de comportamiento y precarga de valores en formularios.                   |
| Pruebas de validación (integración) | ~4                  | Validación de reglas de negocio a través del flujo completo de la aplicación.          |
| Pruebas unitarias puras             | 0                   | No se identificaron pruebas que aíslen una unidad individual de código.                |

### Observación

Para ser consideradas pruebas unitarias puras, las pruebas deberían ejercitar directamente métodos o funciones específicas de formularios, modelos o utilidades, aislando dependencias externas y evitando el uso del cliente HTTP o de flujos completos de persistencia. No se identificaron pruebas con estas características en el archivo analizado.

### Resultado

**Archivo excluido del inventario de pruebas unitarias.**
