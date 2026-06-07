# CATALOGO DE REQUISITOS - BABYBUDDY

### version 1.0

#### Se trasladara a la wiki cuando se requiera

## 1. Introducción

El sistema Baby Buddy es una aplicación web de código abierto diseñada para ayudar a los cuidadores a llevar un registro detallado de las actividades diarias de un bebé, tales como sueño, alimentación, cambios de pañal y parámetros de salud. El propósito de este documento es especificar de manera detallada los requisitos funcionales del sistema basándose en la plantilla de documentación CIGARRA.

## 2. Objetivos

### a. General

Definir y documentar los requisitos funcionales del sistema Baby Buddy para garantizar que el desarrollo cumpla con las expectativas y necesidades de los padres y cuidadores en el seguimiento de las rutinas de sus bebés.

### b. Específicos

- Elaborar un catálogo de requisitos que contemple el código, nombre, descripción, prioridad, y requisitos asociados.
- Dividir los requisitos en módulos lógicos que representen las características núcleo de Baby Buddy.

## 3. Catálogo de requisitos

### a. Requisitos Funcionales

#### i. RF-001 – Dashboard

- **RF-001.1 - Visualización del estado actual**

| **Código**                  | RF-001.1                                                                                                                                                                                                                        |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Nombre**                  | Visualización del estado actual                                                                                                                                                                                                 |
| **Descripción**             | Permite al usuario visualizar un resumen en tiempo real de las actividades recientes del bebé (último sueño, última alimentación, último cambio de pañal).                                                                      |
| **Prioridad**               | Alta                                                                                                                                                                                                                            |
| **Criterios de aceptación** | - Debe mostrar el tiempo transcurrido desde la última actividad de cada tipo.<br>- Debe indicar si hay actividades en curso (ej. temporizador de sueño activo).<br>- Debe actualizarse automáticamente o al recargar la página. |
| **Requisitos asociados**    | RF-004.1, RF-004.3, RF-004.6                                                                                                                                                                                                    |

- **RF-001.2 - Gestión de accesos rápidos**

| **Código**                  | RF-001.2                                                                                                                                                                     |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Gestión de accesos rápidos                                                                                                                                                   |
| **Descripción**             | Proporciona botones de acceso rápido en el panel principal para iniciar el registro de las actividades más comunes.                                                          |
| **Prioridad**               | Media                                                                                                                                                                        |
| **Criterios de aceptación** | - Debe permitir un solo clic para abrir el formulario de registro rápido.<br>- Debe permitir iniciar temporizadores de alimentación o sueño directamente desde el dashboard. |
| **Requisitos asociados**    | RF-004.2, RF-004.4, RF-004.12                                                                                                                                                |

#### ii. RF-002 – Gestión de Cuentas y Ajustes de Usuario

- **RF-002.1 - Creación y autenticación de usuarios**

| **Código**                  | RF-002.1                                                                                                                                                                  |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Nombre**                  | Creación y autenticación de usuarios                                                                                                                                      |
| **Descripción**             | Permite a los usuarios registrarse, iniciar sesión y recuperar contraseñas para acceder al sistema.                                                                       |
| **Prioridad**               | Alta                                                                                                                                                                      |
| **Criterios de aceptación** | - Debe validar credenciales únicas (email/usuario).<br>- Debe manejar encriptación de contraseñas.<br>- Debe permitir recuperación de acceso mediante correo electrónico. |
| **Requisitos asociados**    | Ninguno                                                                                                                                                                   |

- **RF-002.2 - Configuración de preferencias regionales**

| **Código**                  | RF-002.2                                                                                                                                                                                                   |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Configuración de preferencias regionales                                                                                                                                                                   |
| **Descripción**             | Permite al usuario configurar el idioma de la interfaz y su zona horaria local.                                                                                                                            |
| **Prioridad**               | Media                                                                                                                                                                                                      |
| **Criterios de aceptación** | - Debe permitir selección de idioma de una lista soportada.<br>- Debe permitir selección de zona horaria.<br>- Debe adaptar todas las fechas y horas mostradas en la aplicación a la zona horaria elegida. |
| **Requisitos asociados**    | RF-004.1 (Registros de fecha y hora)                                                                                                                                                                       |

- **RF-002.3 - Configuración del panel principal (Dashboard)**

| **Código**                  | RF-002.3                                                                                                                                                                                                                           |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Configuración del panel principal                                                                                                                                                                                                  |
| **Descripción**             | Permite personalizar qué y cómo se visualizan las tarjetas en el dashboard y la paginación de tablas.                                                                                                                              |
| **Prioridad**               | Baja                                                                                                                                                                                                                               |
| **Criterios de aceptación** | - Debe permitir configurar la tasa de refresco automático del dashboard.<br>- Debe permitir ocultar tarjetas vacías o información antigua.<br>- Debe permitir configurar el número de elementos por página en las vistas de lista. |
| **Requisitos asociados**    | RF-001.1                                                                                                                                                                                                                           |

- **RF-002.4 - Gestión de API Keys**

| **Código**                  | RF-002.4                                                                                                                                    |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------ |
| **Nombre**                  | Gestión de API Keys                                                                                                                         |
| **Descripción**             | Permite al usuario generar y regenerar claves de API para integraciones con aplicaciones de terceros.                                       |
| **Prioridad**               | Media                                                                                                                                       |
| **Criterios de aceptación** | - Debe mostrar la clave API actual del usuario de forma segura.<br>- Debe permitir generar una nueva clave invalidando la anterior (reset). |
| **Requisitos asociados**    | Ninguno                                                                                                                                     |

#### iii. RF-003 – Gestión de Bebés

- **RF-003.1 - Añadir perfil de bebé**

| **Código**                  | RF-003.1                                                                                                                                                                                      |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Añadir perfil de bebé                                                                                                                                                                         |
| **Descripción**             | Permite al cuidador registrar a un nuevo bebé en el sistema con su información básica.                                                                                                        |
| **Prioridad**               | Alta                                                                                                                                                                                          |
| **Criterios de aceptación** | - Debe validar campos obligatorios: nombre, fecha de nacimiento.<br>- Debe permitir subir o seleccionar una foto de perfil.<br>- Debe asignar al bebé automáticamente al usuario que lo crea. |
| **Requisitos asociados**    | RF-003.2                                                                                                                                                                                      |

- **RF-003.2 - Editar perfil de bebé**

| **Código**                  | RF-003.2                                                                                                                                                                         |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Editar perfil de bebé                                                                                                                                                            |
| **Descripción**             | Permite modificar la información existente de un bebé registrado.                                                                                                                |
| **Prioridad**               | Media                                                                                                                                                                            |
| **Criterios de aceptación** | - Debe cargar los datos actuales del bebé en el formulario.<br>- Debe validar correctamente los cambios en la fecha de nacimiento.<br>- Debe confirmar la actualización exitosa. |
| **Requisitos asociados**    | RF-003.1                                                                                                                                                                         |

#### iv. RF-004 – Registros de Actividades (Core)

**Submódulo: Gestión de Sueño**

- **RF-004.1 - Registrar sesión de sueño manual**

| **Código**                  | RF-004.1                                                                                                                                                                     |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Registrar sesión de sueño manual                                                                                                                                             |
| **Descripción**             | Permite al usuario introducir manualmente una sesión de sueño completada, especificando hora de inicio y fin.                                                                |
| **Prioridad**               | Alta                                                                                                                                                                         |
| **Criterios de aceptación** | - Debe validar que la hora de fin sea posterior a la de inicio.<br>- Debe permitir añadir notas adicionales al registro.<br>- Debe asociar el registro al bebé seleccionado. |
| **Requisitos asociados**    | RF-001.1, RF-006.1                                                                                                                                                           |

- **RF-004.2 - Registrar sueño con temporizador**

| **Código**                  | RF-004.2                                                                                                                                                                                                                                             |
| :-------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Registrar sueño con temporizador                                                                                                                                                                                                                     |
| **Descripción**             | Permite iniciar un cronómetro en tiempo real cuando el bebé se duerme y detenerlo cuando despierta.                                                                                                                                                  |
| **Prioridad**               | Media                                                                                                                                                                                                                                                |
| **Criterios de aceptación** | - Debe mostrar el tiempo transcurrido en vivo en la interfaz.<br>- Debe permitir guardar automáticamente el registro con los tiempos capturados al detener el temporizador.<br>- Debe funcionar correctamente aunque se cierre y abra la sesión web. |
| **Requisitos asociados**    | RF-004.1, RF-004.12                                                                                                                                                                                                                                  |

**Submódulo: Gestión de Alimentación**

- **RF-004.3 - Registrar alimentación**

| **Código**                  | RF-004.3                                                                                                                                                                                                            |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Nombre**                  | Registrar alimentación                                                                                                                                                                                              |
| **Descripción**             | Permite registrar una toma de alimento indicando el tipo (pecho, biberón, fórmula, sólidos).                                                                                                                        |
| **Prioridad**               | Alta                                                                                                                                                                                                                |
| **Criterios de aceptación** | - Debe mostrar campos dinámicos según el tipo de alimentación (ej. cantidad para biberón, lado/duración para pecho).<br>- Debe permitir especificar la hora de la toma.<br>- Debe permitir añadir notas opcionales. |
| **Requisitos asociados**    | RF-004.4, RF-006.1                                                                                                                                                                                                  |

- **RF-004.4 - Registrar alimentación con temporizador**

| **Código**                  | RF-004.4                                                                                                                                                                                                            |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Nombre**                  | Registrar alimentación con temporizador                                                                                                                                                                             |
| **Descripción**             | Permite iniciar un cronómetro en tiempo real para medir la duración de la toma de alimento (ideal para amamantar).                                                                                                  |
| **Prioridad**               | Media                                                                                                                                                                                                               |
| **Criterios de aceptación** | - Debe mostrar el tiempo transcurrido en la interfaz.<br>- Debe pre-llenar la hora de inicio y fin en el formulario al detener el temporizador.<br>- Debe soportar reinicio del temporizador si hay interrupciones. |
| **Requisitos asociados**    | RF-004.3, RF-004.12                                                                                                                                                                                                 |

- **RF-004.5 - Registrar extracción de leche (Pumping)**

| **Código**                  | RF-004.5                                                                                                                                                                   |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Registrar extracción de leche                                                                                                                                              |
| **Descripción**             | Permite registrar sesiones de extracción de leche materna con cantidad y tiempo.                                                                                           |
| **Prioridad**               | Media                                                                                                                                                                      |
| **Criterios de aceptación** | - Debe permitir registrar hora de inicio y fin, calculando la duración.<br>- Debe permitir registrar cantidad extraída.<br>- Debe soportar registro mediante temporizador. |
| **Requisitos asociados**    | RF-004.12, RF-006.1                                                                                                                                                        |

**Submódulo: Gestión de Cambios de Pañal**

- **RF-004.6 - Registrar cambio de pañal**

| **Código**                  | RF-004.6                                                                                                                                                                             |
| :-------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Registrar cambio de pañal                                                                                                                                                            |
| **Descripción**             | Permite registrar un cambio de pañal especificando la hora y el contenido (mojado, sucio, ambos).                                                                                    |
| **Prioridad**               | Alta                                                                                                                                                                                 |
| **Criterios de aceptación** | - Debe requerir seleccionar al menos un estado (mojado/sucio).<br>- Debe permitir registrar el color y consistencia si es necesario.<br>- Debe registrar la fecha y hora del evento. |
| **Requisitos asociados**    | RF-006.1                                                                                                                                                                             |

**Submódulo: Gestión de Tummy Time**

- **RF-004.7 - Registrar sesión de Tummy Time**

| **Código**                  | RF-004.7                                                                                                    |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Registrar sesión de Tummy Time                                                                              |
| **Descripción**             | Permite al usuario registrar el tiempo que el bebé pasó boca abajo, con fecha y duración.                   |
| **Prioridad**               | Baja                                                                                                        |
| **Criterios de aceptación** | - Debe permitir registro manual de hora de inicio y fin.<br>- Debe permitir registro mediante temporizador. |
| **Requisitos asociados**    | RF-004.12                                                                                                   |

**Submódulo: Gestión de Medidas de Salud**

- **RF-004.8 - Registrar peso, altura, perímetro cefálico e IMC**

| **Código**                  | RF-004.8                                                                                                                                                                                                                              |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Nombre**                  | Registrar peso, altura, perímetro cefálico e IMC                                                                                                                                                                                      |
| **Descripción**             | Permite ingresar y calcular registros periódicos de salud y crecimiento físico del bebé.                                                                                                                                              |
| **Prioridad**               | Media                                                                                                                                                                                                                                 |
| **Criterios de aceptación** | - Debe permitir ingresar peso, altura y perímetro cefálico.<br>- Debe calcular o permitir registrar el Índice de Masa Corporal (IMC) y percentiles.<br>- Debe permitir registrar la fecha de la medición y observaciones adicionales. |
| **Requisitos asociados**    | RF-006.1                                                                                                                                                                                                                              |

- **RF-004.9 - Registrar administración de medicamentos**

| **Código**                  | RF-004.9                                                                                                                         |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Registrar administración de medicamentos                                                                                         |
| **Descripción**             | Permite documentar dosis de medicamentos administradas al bebé.                                                                  |
| **Prioridad**               | Alta                                                                                                                             |
| **Criterios de aceptación** | - Debe registrar el nombre del medicamento, dosis y unidad (mg, ml, gotas, etc.).<br>- Debe registrar la hora de administración. |
| **Requisitos asociados**    | RF-006.1                                                                                                                         |

**Submódulo: Gestión de Notas y Etiquetas**

- **RF-004.10 - Gestión de notas diarias**

| **Código**                  | RF-004.10                                                                                                       |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Gestión de notas diarias                                                                                        |
| **Descripción**             | Permite crear entradas de texto libre o diario con imágenes adjuntas.                                           |
| **Prioridad**               | Baja                                                                                                            |
| **Criterios de aceptación** | - Debe permitir ingresar texto y subir fotos de forma opcional.<br>- Debe registrar la fecha y hora de la nota. |
| **Requisitos asociados**    | RF-004.11                                                                                                       |

- **RF-004.11 - Sistema de etiquetado (Tags)**

| **Código**                  | RF-004.11                                                                                                                                                      |
| :-------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Sistema de etiquetado                                                                                                                                          |
| **Descripción**             | Permite asignar etiquetas personalizadas con colores a cualquier actividad o nota registrada.                                                                  |
| **Prioridad**               | Baja                                                                                                                                                           |
| **Criterios de aceptación** | - Debe permitir crear etiquetas con nombres y colores definidos.<br>- Debe permitir asociar las etiquetas a los registros de actividades de forma transversal. |
| **Requisitos asociados**    | Ninguno                                                                                                                                                        |

**Submódulo: Gestión Global de Temporizadores**

- **RF-004.12 - Gestión de temporizadores en vivo**

| **Código**                  | RF-004.12                                                                                                                                                                                                                                                             |
| :-------------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Gestión de temporizadores en vivo                                                                                                                                                                                                                                     |
| **Descripción**             | Permite crear, nombrar y administrar múltiples temporizadores independientes que luego pueden convertirse en un registro de actividad.                                                                                                                                |
| **Prioridad**               | Media                                                                                                                                                                                                                                                                 |
| **Criterios de aceptación** | - Debe permitir tener más de un temporizador activo simultáneamente.<br>- Debe permitir asociar un temporizador a un bebé específico.<br>- Al detener el temporizador, debe sugerir convertirlo en registro de sueño, alimentación, extracción de leche o tummy time. |
| **Requisitos asociados**    | RF-004.2, RF-004.4, RF-004.5, RF-004.7                                                                                                                                                                                                                                |

#### v. RF-005 – Exportación e Importación de Datos

- **RF-005.1 - Exportación de datos a CSV**

| **Código**                  | RF-005.1                                                                                                                                                    |
| :-------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Exportación de datos a CSV                                                                                                                                  |
| **Descripción**             | Permite descargar todo el historial de actividades del bebé en formato CSV.                                                                                 |
| **Prioridad**               | Media                                                                                                                                                       |
| **Criterios de aceptación** | - Debe permitir filtrar por rango de fechas antes de exportar.<br>- El archivo descargado debe separar los datos por columnas lógicas (fecha, tipo, notas). |
| **Requisitos asociados**    | Ninguno                                                                                                                                                     |

#### vi. RF-006 – Generación de Reportes

- **RF-006.1 - Generar gráficas de actividades y salud**

| **Código**                  | RF-006.1                                                                                                                                                                                                                                                                                                                             |
| :-------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nombre**                  | Generar gráficas de actividades y salud                                                                                                                                                                                                                                                                                              |
| **Descripción**             | Visualiza gráficas estadísticas interactivas sobre el comportamiento y crecimiento del bebé.                                                                                                                                                                                                                                         |
| **Prioridad**               | Media                                                                                                                                                                                                                                                                                                                                |
| **Criterios de aceptación** | - Debe mostrar gráficas avanzadas de todas las actividades (patrones e intervalos de sueño, alimentación, pañales, medicación, extracción de leche).<br>- Debe calcular percentiles para métricas de crecimiento basadas en sexo (peso, altura, perímetro cefálico).<br>- Debe permitir visualizar tendencias a lo largo del tiempo. |
| **Requisitos asociados**    | RF-004.1, RF-004.3, RF-004.5, RF-004.6, RF-004.8, RF-004.9                                                                                                                                                                                                                                                                           |

---

## 4. Resumen

| Cód.   | Nombre             | Descripción resumida                          | Caso de uso asociado          | Prioridad         | Criterios de aceptación                                                | Requisito(s) asociado(s)                                    |
| :----- | :----------------- | :-------------------------------------------- | :---------------------------- | :---------------- | :--------------------------------------------------------------------- | :---------------------------------------------------------- |
| RF-001 | Dashboard          | Ver resumen y accesos directos.               | Consultar estado actual       | Alta              | Actualización en tiempo real, mostrar última actividad.                | RF-004.1, RF-004.2, RF-004.3, RF-004.4, RF-004.6, RF-004.12 |
| RF-002 | Gestión de Cuentas | Registro, login, preferencias y API Keys.     | Administrar perfil de usuario | Alta              | Validación de credenciales, configuración de dashboard y zona horaria. | RF-001.1                                                    |
| RF-003 | Gestión de Bebés   | Crear y modificar perfiles de bebés.          | Administrar bebés             | Alta              | Validación de nombre y fecha de nacimiento.                            | RF-003.1, RF-003.2                                          |
| RF-004 | Registros Core     | Registrar sueño, comida, pañales y salud.     | Registrar actividad diaria    | Alta, Media, Baja | Validación de fechas/horas, manejo dinámico según tipo de registro.    | RF-001.1, RF-006.1                                          |
| RF-005 | Exportación        | Descargar registros en CSV.                   | Exportar datos                | Media             | Filtros por fechas y formato delimitado por comas.                     | Ninguno                                                     |
| RF-006 | Reportes           | Visualizar gráficas de tendencias y patrones. | Visualizar estadísticas       | Media             | Gráficas por cada módulo, cálculo de percentiles.                      | RF-004.1, RF-004.3, RF-004.5, RF-004.6, RF-004.8, RF-004.9  |
