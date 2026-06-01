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


## 4. Archivo: `test_forms.py`

### 4.1. Resultado del análisis

Se realizó la revisión de las 46 pruebas automatizadas contenidas en el archivo `test_forms.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

Tras el análisis de su implementación y comportamiento, se determinó que el archivo no contiene pruebas unitarias puras. En consecuencia, ninguna de las pruebas definidas en este archivo forma parte del alcance del presente documento.

### 4.2. Justificación de la clasificación

Las pruebas analizadas ejercen simultáneamente múltiples componentes de la aplicación, por lo que no aíslan una única unidad de código. Entre las características observadas se encuentran:

* Uso del cliente HTTP de Django (`django.test.Client`) para realizar solicitudes GET y POST.
* Creación, modificación y eliminación de registros en la base de datos de prueba.
* Verificación de respuestas HTTP completas, incluyendo códigos de estado y contenido generado.
* Interacción conjunta entre vistas, formularios, modelos y mecanismos de persistencia.

Debido a estas características, las pruebas se clasifican principalmente como pruebas de integración y pruebas funcionales, en lugar de pruebas unitarias.

### 4.3 Clasificación identificada

| Tipo de prueba                      | Cantidad | Observaciones                                                                          |
| ----------------------------------- | ------------------- | -------------------------------------------------------------------------------------- |
| Pruebas de integración              | 40                 | Operaciones de creación, edición y eliminación de entidades mediante solicitudes HTTP. |
| Pruebas funcionales de formularios  | 6                  | Verificación de comportamiento y precarga de valores en formularios.                   |
| Pruebas de validación (integración) | 4                  | Validación de reglas de negocio a través del flujo completo de la aplicación.          |
| Pruebas unitarias puras             | 0                   | No se identificaron pruebas que aíslen una unidad individual de código.                |

### 4.4. Observación

Para ser consideradas pruebas unitarias puras, las pruebas deberían ejercitar directamente métodos o funciones específicas de formularios, modelos o utilidades, aislando dependencias externas y evitando el uso del cliente HTTP o de flujos completos de persistencia. No se identificaron pruebas con estas características en el archivo analizado.

### 4.5. Resultado

**Archivo excluido del inventario de pruebas unitarias.**


## 5. Archivo: `tests_import_export.py`

### 5.1. Resultado del análisis

Se realizó la revisión de las 15 pruebas automatizadas contenidas en el archivo `tests_import_export.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

Tras el análisis de su implementación y comportamiento, se determinó que el archivo no contiene pruebas unitarias puras. En consecuencia, ninguna de las pruebas definidas en este archivo forma parte del alcance del presente documento.

### 5.2. Justificación de la clasificación

Las pruebas analizadas validan el proceso completo de importación de datos, involucrando múltiples componentes de la aplicación de manera simultánea. Durante su ejecución se observó la interacción entre archivos de datos, recursos de importación, lógica de validación, modelos y persistencia en base de datos.

De forma general, las pruebas siguen el flujo:

```text
Archivo CSV → Dataset (tablib) → ImportExportResource → ORM → Base de Datos → Verificación de resultados
```

Debido a este comportamiento, las pruebas no aíslan una unidad individual de código y, por tanto, no cumplen con los criterios de una prueba unitaria.

### 5.3. Clasificación identificada

| Tipo de prueba          | Cantidad | Observaciones                                                                         |
| ----------------------- | ------------------- | ------------------------------------------------------------------------------------- |
| Pruebas de integración  | 15                  | Verifican procesos completos de importación de datos y persistencia en base de datos. |
| Pruebas unitarias puras | 0                   | No se identificaron pruebas que aíslen funciones, métodos o clases individuales.      |

### 5.4. Casos representativos identificados

| Prueba               | Propósito principal                                                        |
| -------------------- | -------------------------------------------------------------------------- |
| `test_bmi`           | Verifica la importación de registros de índice de masa corporal.           |
| `test_child`         | Verifica la importación de registros de hijos.                             |
| `test_child_invalid` | Verifica el manejo de errores ante datos inválidos durante la importación. |
| `test_diaperchange`  | Verifica la importación de cambios de pañal.                               |
| `test_feeding`       | Verifica la importación de registros de alimentación.                      |
| `test_sleep`         | Verifica la importación de registros de sueño.                             |
| `test_temperature`   | Verifica la importación de registros de temperatura.                       |
| `test_weight`        | Verifica la importación de registros de peso.                              |

### 5.5. Observaciones

Se identificó que la prueba `test_tagged` presenta una complejidad superior al resto del archivo, ya que además de verificar la importación de datos valida la integridad de relaciones *many-to-many* mediante la comprobación de asociaciones específicas entre entidades.

Asimismo, la prueba `test_child_invalid` constituye el único caso orientado a validar escenarios de error y reglas de validación, mientras que las demás pruebas verifican principalmente escenarios exitosos de importación.

El método auxiliar `import_data()` actúa como mecanismo de reutilización para la carga de datos y reducción de duplicación de código, pero no constituye una prueba independiente.

### 5.6. Resultado

**Archivo excluido del inventario de pruebas unitarias.**


## 6 Archivo: `tests_models.py`

### 6.1. Resultado del análisis

Se realizó la revisión de las pruebas automatizadas contenidas en el archivo `tests_models.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

A diferencia de los archivos previamente analizados, las pruebas de este módulo interactúan directamente con los modelos de dominio y sus métodos, evitando el uso del cliente HTTP, vistas y formularios. Sin embargo, las pruebas continúan utilizando el ORM de Django y la base de datos de prueba para la creación, consulta y modificación de registros.

Debido a esta dependencia de persistencia, no se identificaron pruebas unitarias puras según los criterios establecidos para el presente análisis.

### 6.2. Justificación de la clasificación

Las pruebas ejercitan directamente métodos, propiedades y comportamientos de los modelos, pero mantienen dependencia con la infraestructura de persistencia proporcionada por Django.

Entre las características observadas se encuentran:

* Creación y consulta de registros mediante el ORM.
* Validación de métodos y propiedades de modelos.
* Verificación de representaciones textuales (`__str__`).
* Validación de relaciones entre entidades.
* Uso de métodos de validación de modelos (`full_clean()`).
* Dependencia de la base de datos de prueba durante la ejecución.

Por esta razón, las pruebas fueron clasificadas principalmente como pruebas de integración ligera orientadas al modelo.

### 6.3. Clasificación identificada

| Tipo de prueba                      | Cantidad  | Observaciones                                                                     |
| ----------------------------------- | ------------------- | --------------------------------------------------------------------------------- |
| Pruebas de integración ligera (ORM) | 29                  | Interactúan directamente con modelos y base de datos sin utilizar la capa web.    |
| Pruebas cercanas a unitarias        | 3                   | Verifican lógica de negocio específica con mínima dependencia de infraestructura. |
| Pruebas unitarias puras             | 0                   | No se identificaron pruebas completamente aisladas de la base de datos.           |

### 6.5. Detalle de Pruebas destacadas

Durante el análisis se identificaron tres casos particularmente cercanos al concepto de prueba unitaria:


| Método | Clase | Tipo | Estado | Qué verifica | Datos de entrada | Resultado esperado | Resultado obtenido | Tipo de aserción |
|---|---|---|---|---|---|---|---|---|
| test_diaperchange_attributes | DiaperChangeTestCase | Casi unitaria | PASS | attributes() devuelve lista de atributos legibles para el usuario | wet=1, solid=1, color="black", amount=1.25 | ["Wet", "Solid", "Black"] ordenado y capitalizado | ["Wet", "Solid", "Black"] | assertListEqual |
| test_tag_complementary_color | TagTestCase | Casi unitaria | PASS | complementary_color devuelve el color de contraste correcto según luminosidad | Caso 1: color="#ffffff" / Caso 2: color="#000000" | Caso 1: Tag.DARK_COLOR / Caso 2: Tag.LIGHT_COLOR | DARK_COLOR y LIGHT_COLOR respectivamente | assertEqual x2 |
| test_medication_validation_future_time | MedicationTestCase | Casi unitaria | PASS | full_clean() lanza ValidationError cuando time es futura | time = now() + 1h — objeto en memoria, sin .save() | Se lanza ValidationError antes de persistir | ValidationError lanzado correctamente | assertRaises(ValidationError) |


Estas pruebas validan comportamiento del proyeto de forma más directa que el resto del archivo y constituyen los mejores candidatos para una futura refactorización hacia pruebas unitarias puras.


### 6.6. Observación

El archivo representa el conjunto de pruebas más próximo al nivel unitario identificado hasta el momento. No obstante, la dependencia sistemática de la base de datos de prueba impide clasificar las pruebas como unitarias puras bajo criterios estrictos de aislamiento.

### 6.7. Resultado

**Archivo excluido del inventario de pruebas unitarias puras, aunque identificado como principal candidato para futuras refactorizaciones orientadas a pruebas unitarias.**


## 7. Archivo: `tests_templatetags.py`

### 7.1. Resultado del análisis

Se realizó la revisión de las pruebas automatizadas contenidas en el archivo `tests_templatetags.py` con el objetivo de identificar pruebas unitarias que pudieran ser incluidas en el presente inventario.

A diferencia de los archivos previamente analizados, la mayoría de las pruebas presentes en este módulo ejercitan directamente funciones auxiliares y etiquetas personalizadas de plantilla sin involucrar solicitudes HTTP, vistas, formularios o persistencia de datos.

Como resultado, este archivo constituye la principal fuente de pruebas unitarias identificada hasta el momento dentro del módulo analizado.

### 7.2. Justificación de la clasificación

Las pruebas unitarias identificadas presentan las siguientes características:

* Invocan directamente funciones Python.
* No utilizan el cliente HTTP de Django.
* No dependen de vistas o formularios.
* No requieren interacción con la base de datos.
* Verifican transformaciones de datos, cálculos y formateo de valores.

Estas características permiten aislar adecuadamente la lógica bajo prueba y reducen significativamente la dependencia de infraestructura externa.

### 7.3. Clasificación identificada

| Tipo de prueba                | Cantidad aproximada | Observaciones                                                                        |
| ----------------------------- | ------------------- | ------------------------------------------------------------------------------------ |
| Pruebas unitarias puras       | 7                   | Validan funciones auxiliares y lógica de transformación de datos.                    |
| Pruebas de integración ligera | 2                   | Requieren interacción con componentes adicionales de Django para generar resultados. |
| Pruebas inactivas             | 1                   | Prueba comentada y actualmente excluida de la ejecución automática.                  |

### 7.4. Pruebas unitarias identificadas


| Método | Clase | Tipo | Estado | Qué verifica | Datos de entrada | Resultado esperado | Resultado obtenido | Tipo de aserción |
|---|---|---|---|---|---|---|---|---|
| `test_bootstrap_bool_icon` | `TemplateTagsTestCase` | Unitaria pura | PASS | `bool_icon()` devuelve HTML correcto con clase CSS según booleano | `True`, `False` | `icon-true text-success` / `icon-false text-danger` | Coincide con esperado | `assertEqual` x2 |
| `test_duration_duration_string` | `TemplateTagsTestCase` | Unitaria pura | PASS | `duration_string()` formatea un `timedelta` en texto legible con precisión variable | `timedelta(h=1, m=30, s=15)`, precisiones `"m"`, `"h"`, `""`, `"not a delta"` | Cadena formateada por precisión; `""` para entrada vacía; `TypeError` para inválido | Coincide con esperado | `assertEqual` x4, `assertRaises` (uso incorrecto) |
| `test_duration_hours` | `TemplateTagsTestCase` | Unitaria pura | PASS | `hours()` extrae las horas de un `timedelta` | `timedelta(hours=1)`, `""`, `"not a delta"` | `1`, `0`, `TypeError` | Coincide con esperado | `assertEqual` x2, `assertRaises` (uso incorrecto) |
| `test_duration_minutes` | `TemplateTagsTestCase` | Unitaria pura | PASS | `minutes()` extrae los minutos de un `timedelta` | `timedelta(minutes=45)`, `""`, `"not a delta"` | `45`, `0`, `TypeError` | Coincide con esperado | `assertEqual` x2, `assertRaises` (uso incorrecto) |
| `test_duration_seconds` | `TemplateTagsTestCase` | Unitaria pura | PASS | `seconds()` extrae los segundos de un `timedelta` | `timedelta(seconds=20)`, `""`, `"not a delta"` | `20`, `0`, `TypeError` | Coincide con esperado | `assertEqual` x2, `assertRaises` (uso incorrecto) |
| `test_duration_dayssince` | `TemplateTagsTestCase` | Unitaria pura | PASS | `dayssince()` devuelve texto relativo correcto para distintas fechas de referencia | 3 fechas × 5 deltas: mismo día, -5h, -24h, -48h, -60 días | `"today"`, `"yesterday"`, `"2 days ago"`, `"10 days ago"`, `"60 days ago"` | Coincide con esperado | `assertEqual` x15 |
| `test_duration_deltasince` | `TemplateTagsTestCase` | Unitaria pura | PASS | `deltasince()` calcula el `timedelta` entre dos `datetime` con `now` fijo | 3 pares de `datetime` con `now = 2022-01-01 00:00:02` | `timedelta(s=1)`, `timedelta(s=3)`, `timedelta(days=19326, s=3)` | Coincide con esperado | `assertEqual` dentro de `subTest` x3 |                       |

### 7.5. Pruebas clasificadas como integración ligera

| Método | Clase | Tipo | Estado | Qué verifica | Datos de entrada | Resultado esperado | Resultado obtenido | Tipo de aserción |
|---|---|---|---|---|---|---|---|---|
| `test_instance_add_url` | `TemplateTagsTestCase` | Integración ligera | PASS | `instance_add_url()` genera URL correcta con y sin `child` asociado al timer | Timer sin child / Timer con child `Test Child` | `"/sleep/add/?timer=ID"` / `"/sleep/add/?timer=ID&child=slug"` | Coincide con esperado | `assertEqual` x2 |
| `test_datetime_short` | `TemplateTagsTestCase` | Integración ligera | PASS | `datetime_short()` devuelve `"Today, HH:MM"` para hoy y `"D Mon, HH:MM"` para fechas anteriores | `localtime()` (hoy) / `localtime() - 1 día 6 horas` | Formato `"Today, TIME"` / Formato `"SHORT_MONTH_DAY, TIME"` | Coincide con esperado | `assertEqual` x2 |

### 7.6. Observaciones

Se identificó una prueba comentada e inactiva:

```text
test_child_age_string
```

La prueba no participa actualmente en la ejecución automática de la suite y, por tanto, la funcionalidad asociada carece de cobertura activa.

El motivo probable es la dependencia de fechas calculadas respecto al momento actual de ejecución, lo que introduce comportamiento no determinista y posibles fallos intermitentes.

### 7.7. Resultado

**Se identificaron 7 pruebas unitarias puras que cumplen los criterios de inclusión definidos para el presente inventario.**

El archivo constituye la principal fuente de cobertura unitaria encontrada durante el análisis realizado hasta esta etapa.


**Unitarias puras:**


---

**Integración ligera:**

