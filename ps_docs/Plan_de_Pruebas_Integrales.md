**BABYBUDDY - PLAN DE PRUEBAS INTEGRALES**
---

## Control de Versiones

| Versión | Autor(es) | Descripción | Fecha |
| :--- | :--- | :--- | :--- |
| 1.0 | Manuel M. Champi Sanchez | Versión inicial del documento | 03/05/2026 |
| 1.5 | Manuel M. Champi Sanchez | Versión mejorada del documento, aplicando ISO/IEC/IEEE 29119 | 10/06/2026 |

## 1. Introducción

### 1.1. Alcance
El propósito de este plan es organizar y definir cómo vamos a revisar que las distintas partes de Baby Buddy se comuniquen bien entre sí. La intereaccion entre los diferentes módulos (como las pantallas, la base de datos y los reportes) como intercambian información de forma correcta, rápida y sin perder datos en el camino.

### 1.2. Referencias
* ISO/IEC/IEEE 29119
* Documentación oficial de BABYBUDDY
* Repositorio de BABYBUDDY


### 1.3. Glosario
En este documento se utilizan los siguientes términos abreviados:
* **Integration Testing:** Tipo de prueba enfocada en verificar el correcto ensamblaje y comunicación entre múltiples componentes o módulos de software.
* **API:** Interfaz de Programación de Aplicaciones (Application Programming Interface).
* **CRUD:**  Crear, Leer, Actualizar, Eliminar (Create, Read, Update, Delete).
* **REST:** Transferencia de Estado Representacional (Representational State Transfer).
* **UI:** Interfaz de Usuario (User Interface).
* **ORM:**  Mapeo Objeto-Relacional (Object-Relational Mapping).
* **JSON:** Formato de texto ligero para el intercambio de datos (JavaScript Object Notation).
---

## 2. Contexto de las Pruebas
### 2.1. Proyecto / Subprocesos de Prueba
El Sistema BabyBuddy consta de los siguientes módulos:
* **Módulo CORE (El motor del sistema):** Es el corazón de la aplicación. Guarda los datos clave como las comidas, siestas y pañales del bebé. Verificamos cómo se conecta con los formularios que llena el usuario.
* **Módulo API (El puente externo):** Es la puerta trasera que permite que un reloj inteligente o una aplicación de celular mande o reciba datos de Baby Buddy sin abrir la página web. Probamos cómo traduce la información para el motor central.
* **Módulo BABYBUDDY (El director de orquesta):** Controla las configuraciones generales del sistema (como los idiomas y la hora). Probamos que aplique estas reglas a todos los demás módulos de forma transparente.
* **Módulo DASHBOARD (El panel de inicio):** La pantalla principal que ve el usuario apenas entra. Revisa en tiempo real los datos del motor central para hacer cálculos al instante.
* **Módulo REPORTS (Los reportes y gráficos):** Agarra el historial de varias semanas del motor central y lo convierte en gráficos organizados para el médico.

### 2.2. Elementos de Prueba
En esta fase probamos las conexiones lógicas entre las piezas clave de la aplicación:

* **Integración del formulario con la pantalla y la base de datos (Core-Forms-Views):** Probamos el camino completo que hacen los datos. Nos aseguramos de que cuando un usuario escribe en la pantalla cuánta leche tomó el bebé, el sistema verifique que no haya errores (como que pongan números negativos), pase la información correctamente y la guarde de forma segura en la base de datos sin que se pierda nada en el camino.
* **Integración de los registros con la Línea de Tiempo (Core-Timeline):** Probamos el orden automático de los eventos. Si un papá registra una siesta a las 2:00 PM, una comida a las 4:00 PM y un cambio de pañal a las 3:00 PM, el sistema debe ser lo suficientemente inteligente como para ordenarlos cronológicamente por hora exacta y mostrar una línea de tiempo perfecta y fácil de leer.
* **Integración de la API y el "Traductor" de datos (Core-API-Serializers):** Probamos cómo la aplicación habla con el mundo exterior. Si en el futuro se conecta una aplicación móvil o un reloj inteligente para mandar datos a Baby Buddy, probamos que el sistema funcione como un buen "traductor", convirtiendo la información de la base de datos a un formato universal (JSON) que cualquier otro dispositivo pueda entender a la perfección.
* **Integración del control de hora automática (Babybuddy-Middleware-Core):** Probamos el detector automático de zonas horarias. Si el usuario configuró que vive en Perú, un "guardián invisible" en el código debe interceptar cada registro de sleep o comida y asegurarse de ponerle la hora exacta de Perú, evitando que se guarde con la hora del servidor de internet (que podría estar en Estados Unidos o Europa).
* **Integración del Panel de Inicio en tiempo real (Dashboard-Core-Templates):** Probamos que los datos de la pantalla principal se calculen y muestren bien. El sistema debe ir a la base de datos, ver a qué hora fue el último pañal (por ejemplo, a las 4:00 PM), hacer la matemática en el acto y pintarle al usuario un botón o letrero dinámico que diga: "Hace 2 horas cambiaste el último pañal".
* **Integración de los Reportes con los Gráficos visuales (Reports-Core-Graphs):** Probamos la fábrica de estadísticas para el pediatra. Nos aseguramos de que el sistema pueda juntar el historial de todo un mes (por ejemplo, todas las horas de sueño de mayo), agruparlas limpiamente y pasárselas al motor visual para que dibuje una gráfica interactiva, bonita y sin errores de datos.

### 2.3. Alcance de la Prueba
* El sistema compuesto por los módulos mencionados en el acápite 2.2
* La interacción entre las 5 partes mencionadas. 
* El intercambio de datos a través del traductor de la API y la forma en que el Panel de Inicio y los Gráficos se actualizan cuando guardamos datos nuevos.

### 2.4. Suposiciones y Restricciones

**2.4.1. Suposiciones**
* El ambiente de pruebas es un clon del repositorio original de forma que al probar este no afecte al proyecto original.

**2.4.2. Restricciones**
* Las reuniones que requieran la participación completa del equipo se realizarán de forma presencial los días jueves de 12:20-12:40 pm.

### 2.5. Partes Interesadas

| :--- | :--- |
| Docente | Revisión del Plan de Pruebas Unitarias<br>Aprobación del Plan de Pruebas Unitarias<br>Revision del Cronograma<br>Aprobación de Cronograma |


---

## 3. Comunicación de las Pruebas

| Punto de Comunicación | Proposito | Frecuencia | Medios | Responsable | Audiencia |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Reunion de Inicio | Explicar cómo se conectan los módulos y qué va a probar cada uno.| Una vez | Reunion | Test Lead | Equipo |
| Reuniones Internas | Ver si las pantallas y la base de datos se están conectando bien. | Semanal | Reunion | Test Lead | Equipo |
| Reporte de Estado | Reportar qué flujos ya se probaron y cuáles fallaron.| 2 a 3 veces por Semana | GitHub Projects | Test Lead | Equipo |
| Reporte de Hitos | Alcance | En la fecha indicada | GitHub Projects | Test Lead | Equipo |
| Preguntas, Dudas | Explicaciones | Constante | Whatsapp | Equipo | Equipo |

---

## 4. Registro de Riesgos
En la siguiente tabla se identifican los riesgos del proyecto, así como se determina la severidad de cada uno de los riesgos.

El impacto y la probabilidad se determinan entre 1 y 5, donde 1 es el más bajo y 5 el más alto, donde:

| Sigla | Significado | Escala |
| :--- | :--- | :--- |
| P | Probabilidad | 1-5 |
| I | Impacto | 1-5 |
| S | Severidad | 1-25 |


### 4.1. Matriz de Riesgos
Fórmula de la Severidad: $P \times I = S$

| N° | Riesgos | P | I | S | Plan de Mitigacion |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | Retrasos en la implementación de pruebas integrales. | 2 | 5 | 10 | Evaluar el avance del desarrollo de las pruebas y re-planificar acorde al avance de ser necesario. |
| 2 | Retrasos en la elaboración del informe de pruebas integrales. | 3 | 5 | 15 | Evaluar el progreso del informe, re-planificar acorde al avance. |
| 3 | Problemas con el despliegue local de cada miembro del equipo | 2 | 4 | 8 | Brindar asesoría personal a cada miembro. De ser necesario realizar una reunión para todo el equipo. |
| 4 | Errores en la configuración de las herramientas de automatización de pruebas | 3 | 4 | 12 | Adquirir conocimientos adicionales sobre estas herramientas y la manera adecuada de utilizarlas. |
| 5 | Retrasos en la corrección de defectos debido a la disponibilidad del equipo | 4 | 4 | 16 | Asignar tiempo específico del equipo para la resolución de defectos de pruebas. |
| 6 | Retraso de algún integrante en sus responsabilidades o tareas | 4 | 5 | 20 | Realizar revisiones de progreso interdiarias. Ofrecer apoyo y resolver dudas del integrante. De existir la posibilidad siempre y cuando no afecte al desarrollo propuesto del HITO 2, se puede extender la fecha de entrega. El miembro tiene que explicar al Test Lead el motivo del retraso. |

---

## 5. Estrategia de Prueba

### 5.1. Subproceso de Prueba
Las pruebas para el Sistema "BabyBuddy" incluyen los siguientes subprocesos de prueba:
* Pruebas Integrales

### 5.2. Entregables de Prueba
Para cada subproceso de prueba se debe entregar la siguiente información/documentación:
* Progreso en GitHub Actions
* Informe/Reporte donde listamos qué conexiones funcionaron, cuáles fallaron y cuántos errores encontramos.

### 5.3. Técnicas de diseños de Pruebas
Se estima el uso de pruebas de caja negra como:
* Partición de Equivalencia (PE)
* Análisis de Valores Limite (AVL)
* Tabla de Decisión
* Transición de estados

### 5.4. Criterio de Finalización de Prueba
Las pruebas deben alcanzar una cobertura de requisitos del 85% y todos los procedimientos de pruebas deben ejecutarse sin fallas de gravedad.

### 5.5. Metricas
Las siguientes métricas se recogen durante el transcurso de la ejecución de las pruebas:
* Número de casos de prueba ejecutados
* Número de casos de prueba por requisito
* Número de caso de prueba resueltos
* Número de casos de prueba resuelto por requisito
* Número de incidentes ocurridos
* Número de incidentes resueltos.
*Tasa de éxito de pruebas: (Casos de prueba exitosos / Total de casos de prueba ejecutados) * 100%
* Tasa de detección de defectos: Defectos detectados / Total de casos de prueba ejecutados
* Tiempo promedio de resolución de defectos: Tiempo promedio acontecido entre la deteccion y resolucion de un defecto
* Cobertura de requisitos: (Cantidad de requisitos probados / Requisitos totales)
* Cantidad de líneas de código efectuadas por caso de prueba.
* Esfuerzo por caso de prueba: (Total de horas dedicadas / Total de casos de prueba ejecutados)

### 5.6. Requisitos del entorno de Prueba

**5.6.1. Ambiente de pruebas**

| Componente | Detalles |
| :--- | :--- |
| Navegadores | Microsoft Edge, Brave |
| Sistemas Operativos | Windows 11 Pro, Windows 11 Home, Debian 13.5 Trixie |


**5.6.2. Herramientas de pruebas**

| Herramienta | Funcion |
| :--- | :--- |
| Django Test | Framework que ejecuta la suite de pruebas unitarias. |
| Gulp | Automatizador de tareas, prepara el entorno. |
| Coverage | Mide el porcentaje exacto de código cubierto durante la ejecución de las pruebas. |
| Docker Compose | Una herramienta que empaqueta todo Baby Buddy en un contenedor cerrado para que funcione igual en la computadora de cualquier alumno. |

### 5.7. Re-Testing y regresión de las Pruebas
Se ejecutarán las pruebas de confirmación necesarias para asegurar que las incidencias reportadas fueron resueltas satisfactoriamente. Dicho proceso se centrará en la repetición de los casos de prueba fallidos bajo los mismos parámetros técnicos documentados en el hallazgo original.

### 5.8. Criterios de Suspensión y Reanudación

**5.8.1. Criterios de suspensión**
* Alguna funcionalidad clave descrita en los requisitos del sistema BABYBUDDY no puede ejecutarse debido a errores bloqueantes.
* Fallas entre los componentes principales del sistema.
* El entorno de pruebas presenta inestabilidad o errores que impiden la obtención de resultados confiables.
* No se dispone de datos de prueba adecuados para continuar con la ejecución.
* Durante la suspensión, el equipo documentará la situación por Whatsapp y notificará al Test Lead para la coordinación con el equipo de desarrollo.

**5.8.2. Criterio de reanudación**
* Los defectos críticos se hayan corregido y validados mediante el re-testing.
* Se disponga de datos de prueba válidos que permitan la continuidad del proceso.
* El Test Lead y el Instructor aprueben la reanudación formal mediante reunión de revisión.

---

## 6. Actividades y Estimados de Prueba

### 6.1. Definición de la Estructura General de Pruebas
* Hacer una lista de todos los puntos donde los módulos de Baby Buddy se tocan (ej: dónde se junta la API con el Core) para saber exactamente qué cables lógicos vamos a revisar.

### 6.2. Diseño de los casos de prueba
* Crear en base al catálogo de requisitos una lista detallada con los escenarios que se van a probar, utilizando límites lógicos.

### 6.3. Preparación del entorno
* Encender Docker en todas las computadoras del grupo, cargar los datos falsos iniciales de los bebés y verificar que Postman tenga acceso libre a las rutas de la aplicación.

### 6.4. Primer ciclo de ejecución de pruebas
* Ejecutar las pruebas encontradas con el objetivo de encontrar fallos en el sistema, corregir el código cuando se detecte algún problema.

### 6.5. Segundo ciclo de ejecución de pruebas
* Volver a ejecutar las pruebas para asegurar que las correcciones no afecten a otras partes que ya funcionaban.
* Implementar nuevas pruebas unitarias que estén fuera del happy path encontrado.

### 6.6. Tercer ciclo de ejecución de pruebas
* Ejecutar las pruebas para encontrar fallos y ver que estas nuevas no afecten al funcionamiento entre las diferentes partes del sistema.

### 6.7. Informe de Reporte de Estados y Finalización
* Generar reportes de resultados (defectos, cobertura, estado de pruebas) y un informe de finalización.
* Presentar hallazgos al docente, incluyendo los problemas superados como las lecciones aprendidas.

---

### 7.1. Roles, Actividades y Responsabilidades
Se utiliza la matriz RACI (Responsable, Apoyo, Consultado e Informado) donde:
* **R - Responsable:** Las personas que ejecutan la tarea o actividad, es decir, son quienes hacen el trabajo.
* **A - Aprobador / Responsable final (Accountable):** La persona que tiene la autoridad final sobre la actividad y se asegura de que se complete correctamente. Solo puede haber un "A" por actividad el cual es el TEST LEAD.
* **C - Consultado:** Personas que deben ser consultadas antes o durante la ejecución de la actividad. Son expertos o partes clave que brindan asesoría o información.
* **I - Informado:** Personas que deben ser notificadas del avance o resultados de la actividad. No participan directamente, pero necesitan estar al tanto.

| Rol/Actividad | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Instructor | I | I | I| I | 1 | I | I |
| Test Lead | A | A | I| A | A | A | A |
| Test Analyst | C | R | C | R | R | R | C |
| Test Design | R | C | C | C | C | C | C |
| Test Architect| C | I | R | I | I | I | I |

### 7.2. Necesidades de Contratación
Para este proyecto y en base a la carga estimada y el cronograma establecido para las actividades de prueba de BABYBUDDY, se ha llegado a la conclusión de que el equipo cuenta con integrantes comprometidos a llevara cabo la tercera parte de pruebas de integracion..

### 7.3. Necesidades de Entrenamiento
Para garantizar un ejecucion de pruebas adecuado a las actividades se indicó que cada miembro del equipo indistintamente de su rol en el proyecto, OBLIGATORIAMENTE tiene que correr de forma local el proyecto e introducirse en el mismo de forma individual, con el fin de que cada miembro comprenda el sistema a su debido tiempo. De ser necesario se indicó que...

---

## 8. Cronograma
El cronograma de actividades está ubicado dentro de la herramienta “GitHub Projects” del proyecto.
* **Enlace:** https://github.com/users/acahuib/projects/3
