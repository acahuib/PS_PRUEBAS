## **BABYBUDDY - PLAN DE PRUEBAS UNITARIAS**

## Control de Versiones

| Versión | Autor(es)                   | Descripción                                                              | Fecha      |
| :------ | :-------------------------- | :----------------------------------------------------------------------- | :--------- |
| 1.0     | Anthony L. Chaisa Fernandez | Versión inicial del documento                                            | 27/05/2026 |
| 1.5     | Anthony L. Chaisa Fernandez | Versión mejorada del documento, aplicando ISO/IEC/IEEE 29119             | 01/06/2026 |
| 2.0     | Anthony L. Chaisa Fernandez | Versión mejorada y completa del documento aplicando ISO/IEC/IEEE 29119-3 | 06/06/2026 |

---

## Índice

1. [Introducción](#1-introducción)
   - 1.1. [Alcance](#11-alcance)
   - 1.2. [Referencias](#12-referencias)
   - 1.3. [Glosario](#13-glosario)
2. [Contexto de las Pruebas](#2-contexto-de-las-pruebas)
   - 2.1. [Proyecto / Subprocesos de Prueba](#21-proyecto--subprocesos-de-prueba)
   - 2.2. [Elementos de Prueba](#22-elementos-de-prueba)
   - 2.3. [Alcance de la Prueba](#23-alcance-de-la-prueba)
   - 2.4. [Suposiciones y Restricciones](#24-suposiciones-y-restricciones)
   - 2.5. [Partes Interesadas](#25-partes-interesadas)
3. [Comunicación de las Pruebas](#3-comunicación-de-las-pruebas)
4. [Registro de Riesgos](#4-registro-de-riesgos)
   - 4.1. [Matriz de Riesgos](#41-matriz-de-riesgos)
5. [Estrategia de Prueba](#5-estrategia-de-prueba)
   - 5.1. [Subproceso de Prueba](#51-subproceso-de-prueba)
   - 5.2. [Entregables de Prueba](#52-entregables-de-prueba)
   - 5.3. [Técnicas de diseños de Pruebas](#53-técnicas-de-diseños-de-pruebas)
   - 5.4. [Criterio de Finalización de Prueba](#54-criterio-de-finalización-de-prueba)
   - 5.5. [Metricas](#55-metricas)
   - 5.6. [Requisitos del entorno de Prueba](#56-requisitos-del-entorno-de-prueba)
   - 5.7. [Re-Testing y regresión de las Pruebas](#57-re-testing-y-regresión-de-las-pruebas)
   - 5.8. [Criterios de Suspensión y Reanudación](#58-criterios-de-suspensión-y-reanudación)
6. [Actividades y Estimados de Prueba](#6-actividades-y-estimados-de-prueba)
   - 6.1. [Definición de la Estructura General de Pruebas](#61-definición-de-la-estructura-general-de-pruebas)
   - 6.2. [Diseño de los casos de prueba](#62-diseño-de-los-casos-de-prueba)
   - 6.3. [Preparación del entorno](#63-preparación-del-entorno)
   - 6.4. [Primer ciclo de ejecución de pruebas](#64-primer-ciclo-de-ejecución-de-pruebas)
   - 6.5. [Segundo ciclo de ejecución de pruebas](#65-segundo-ciclo-de-ejecución-de-pruebas)
   - 6.6. [Tercer ciclo de ejecución de pruebas](#66-tercer-ciclo-de-ejecución-de-pruebas)
   - 6.7. [Informe de Reporte de Estados y Finalización](#67-informe-de-reporte-de-estados-y-finalización)
7. [Personal](#7-personal)
   - 7.1. [Roles, Actividades y Responsabilidades](#71-roles-actividades-y-responsabilidades)
   - 7.2. [Necesidades de Contratación](#72-necesidades-de-contratación)
   - 7.3. [Necesidades de Entrenamiento](#73-necesidades-de-entrenamiento)
8. [Cronograma](#8-cronograma)

---

## 1. Introducción

### 1.1. Alcance

El propósito de este documento es proporcionar la información y el marco requerido para planificar y desarrollar las actividades del proceso de pruebas unitarias del sistema "BabyBuddy".

### 1.2. Referencias

- ISO/IEC/IEEE 29119
- Documentación oficial de BABYBUDDY
- Repositorio de BABYBUDDY
- Catalogo de Requisitos Funcionales de BABYBUDDY
- Catalogo de Requisitos NO funcionales de BABYBUDDY

### 1.3. Glosario

En este documento se utilizan los siguientes términos abreviados:

- **UT:** Unit Testing (Pruebas Unitarias)
- **UAT:** User Acceptance Testing, pruebas realizadas por usuarios finales para validar que el sistema cumple requisitos.
- **API:** Application Programming Interface (Interfaz de Programación de Aplicaciones).
- **TDD:** Test-Driven Development, donde las pruebas se escriben antes del código.
- **Django Test:** Framework integrado en Django para crear y ejecutar pruebas automatizadas en aplicaciones web.
- **Gulp:** Herramienta de automatización de tareas, usada para compilar, minificar y optimizar proyectos frontend.
- **Coverage** Métrica que indica qué porcentaje del código está cubierto por pruebas automatizadas.

---

## 2. Contexto de las Pruebas

### 2.1. Proyecto / Subprocesos de Prueba

El Sistema BabyBuddy consta de los siguientes módulos:

- API
- Babybuddy
- Core
- Dashboard
- Reportes

A continuación se muestran como estos módulos interactúan

### 2.2. Elementos de Prueba

Se realizarán pruebas unitarias a los siguientes módulos:

- API
- BabyBuddy
- Core
- Dashboard
- Reportes

### 2.3. Alcance de la Prueba

- El sistema compuesto por los módulos mencionados en el acápite 2.2
- Las pruebas se limitan exclusivamente a la lógica de backend donde se encuentran los archivos en python.
- Los factores de la calidad no funcionales como el rendimiento, la seguridad informática y la usabilidad no se probarán para este proyecto.

### 2.4. Suposiciones y Restricciones

**2.4.1. Suposiciones**

- El ambiente de pruebas es un clon del repositorio original de forma que al probar, crear y/o refactorizar las pruebas unitarias este no afecte al proyecto original.

**2.4.2. Restricciones**

- Las reuniones que requieran la participación completa del equipo se realizarán de forma presencial los días jueves de 12:20-12:40 pm.

### 2.5. Partes Interesadas

| Rol     | Responsabilidades                                                                                                                         |
| :------ | :---------------------------------------------------------------------------------------------------------------------------------------- |
| Docente | Revisión del Plan de Pruebas Unitarias<br>Aprobación del Plan de Pruebas Unitarias<br>Revision del Cronograma<br>Aprobación de Cronograma |

---

## 3. Comunicación de las Pruebas

| Punto de Comunicación | Proposito           | Frecuencia             | Medios          | Responsable | Audiencia |
| :-------------------- | :------------------ | :--------------------- | :-------------- | :---------- | :-------- |
| Reunion de Inicio     | Iniciar el proyecto | Una vez                | Reunion         | Test Lead   | Equipo    |
| Reuniones Internas    | Estado del proyecto | Semanal                | Reunion         | Test Lead   | Equipo    |
| Reporte de Estado     | Estado              | 2 a 3 veces por Semana | GitHub Projects | Test Lead   | Equipo    |
| Reporte de Hitos      | Alcance             | En la fecha indicada   | GitHub Projects | Test Lead   | Equipo    |
| Preguntas, Dudas      | Explicaciones       | Constante              | Whatsapp        | Equipo      | Equipo    |

---

## 4. Registro de Riesgos

En la siguiente tabla se identifican los riesgos del proyecto, así como se determina la severidad de cada uno de los riesgos.

El impacto y la probabilidad se determinan entre 1 y 5, donde 1 es el más bajo y 5 el más alto, donde:

| Sigla | Significado  | Escala |
| :---- | :----------- | :----- |
| P     | Probabilidad | 1-5    |
| I     | Impacto      | 1-5    |
| S     | Severidad    | 1-25   |

### 4.1. Matriz de Riesgos

Fórmula de la Severidad: $P \times I = S$

| N°  | Riesgos                                                                      | P   | I   | S   | Plan de Mitigacion                                                                                                                                                                                                                                                                             |
| :-- | :--------------------------------------------------------------------------- | :-- | :-- | :-- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1   | Retrasos en la implementación de nuevas pruebas unitarias.                   | 2   | 5   | 10  | Evaluar el avance del desarrollo de las pruebas y re-planificar acorde al avance de ser necesario.                                                                                                                                                                                             |
| 2   | Retrasos en la elaboración del informe de pruebas unitarias.                 | 3   | 5   | 15  | Evaluar el progreso del informe, re-planificar acorde al avance.                                                                                                                                                                                                                               |
| 3   | Problemas con el despliegue local de cada miembro del equipo                 | 2   | 4   | 8   | Brindar asesoría personal a cada miembro. De ser necesario realizar una reunión para todo el equipo.                                                                                                                                                                                           |
| 4   | Errores en la configuración de las herramientas de automatización de pruebas | 3   | 4   | 12  | Adquirir conocimientos adicionales sobre estas herramientas y la manera adecuada de utilizarlas.                                                                                                                                                                                               |
| 5   | Retrasos en la corrección de defectos debido a la disponibilidad del equipo  | 4   | 4   | 16  | Asignar tiempo específico del equipo para la resolución de defectos de pruebas.                                                                                                                                                                                                                |
| 6   | Retraso de algún integrante en sus responsabilidades o tareas                | 4   | 5   | 20  | Realizar revisiones de progreso interdiarias. Ofrecer apoyo y resolver dudas del integrante. De existir la posibilidad siempre y cuando no afecte al desarrollo propuesto del HITO 1, se puede extender la fecha de entrega. El miembro tiene que explicar al Test Lead el motivo del retraso. |

---

## 5. Estrategia de Prueba

### 5.1. Subproceso de Prueba

Las pruebas para el Sistema "BabyBuddy" incluyen los siguientes subprocesos de prueba:

- Pruebas Unitarias

### 5.2. Entregables de Prueba

Para cada subproceso de prueba se debe entregar la siguiente información/documentación:

- Progreso en GitHub Actions
- Informe/Reporte de Pruebas Unitarias

### 5.3. Técnicas de diseños de Pruebas

Se estima el uso de pruebas de caja negra como:

- Particion de Equivalencia (PE)
- Analisis de Valores Limite (AVL)

### 5.4. Criterio de Finalización de Prueba

Las pruebas deben alcanzar una cobertura de requisitos del 85% y todos los procedimientos de pruebas deben ejecutarse sin fallas de gravedad.

### 5.5. Metricas

Las siguientes métricas se recogen durante el transcurso de la ejecución de las pruebas:

- Número de casos de prueba ejecutados
- Número de casos de prueba por requisito
- Número de caso de prueba resueltos
- Número de casos de prueba resuelto por requisito
- Número de incidentes ocurridos
- Número de incidentes resueltos.
  _Tasa de éxito de pruebas: (Casos de prueba exitosos / Total de casos de prueba ejecutados) _ 100%
- Tasa de detección de defectos: Defectos detectados / Total de casos de prueba ejecutados
- Tiempo promedio de resolución de defectos: Tiempo promedio acontecido entre la deteccion y resolucion de un defecto
- Cobertura de requisitos: (Cantidad de requisitos probados / Requisitos totales)
- Cantidad de líneas de código efectuadas por caso de prueba.
- Esfuerzo por caso de prueba: (Total de horas dedicadas / Total de casos de prueba ejecutados)

### 5.6. Requisitos del entorno de Prueba

**5.6.1. Ambiente de pruebas**

| Componente          | Detalles                                            |
| :------------------ | :-------------------------------------------------- |
| Navegadores         | Microsoft Edge, Brave                               |
| Sistemas Operativos | Windows 11 Pro, Windows 11 Home, Debian 13.5 Trixie |

**5.6.2. Herramientas de pruebas**

| Herramienta | Funcion                                                                           |
| :---------- | :-------------------------------------------------------------------------------- |
| Django Test | Framework que ejecuta la suite de pruebas unitarias.                              |
| Gulp        | Automatizador de tareas, prepara el entorno.                                      |
| Coverage    | Mide el porcentaje exacto de código cubierto durante la ejecución de las pruebas. |

### 5.7. Re-Testing y regresión de las Pruebas

Se ejecutarán las pruebas de confirmación necesarias para asegurar que las incidencias reportadas fueron resueltas satisfactoriamente. Dicho proceso se centrará en la repetición de los casos de prueba fallidos bajo los mismos parámetros técnicos documentados en el hallazgo original.

### 5.8. Criterios de Suspensión y Reanudación

**5.8.1. Criterios de suspensión**

- Alguna funcionalidad clave descrita en los requisitos del sistema BABYBUDDY no puede ejecutarse debido a errores bloqueantes.
- Fallas entre los componentes principales del sistema.
- El entorno de pruebas presenta inestabilidad o errores que impiden la obtención de resultados confiables.
- No se dispone de datos de prueba adecuados para continuar con la ejecución.
- Durante la suspensión, el equipo documentará la situación por Whatsapp y notificará al Test Lead para la coordinación con el equipo de desarrollo.

**5.8.2. Criterio de reanudación**

- Los defectos críticos se hayan corregido y validados mediante el re-testing.
- Se disponga de datos de prueba válidos que permitan la continuidad del proceso.
- El Test Lead y el Instructor aprueben la reanudación formal mediante reunión de revisión.

---

## 6. Actividades y Estimados de Prueba

### 6.1. Definición de la Estructura General de Pruebas

- Definir qué módulos de la aplicación se van a probar priorizando las más criticas.

### 6.2. Diseño de los casos de prueba

- Crear en base al catálogo de requisitos una lista detallada con los escenarios que se van a probar, utilizando límites lógicos.

### 6.3. Preparación del entorno

- Instalar y configurar de forma local, tanto el proyecto como todas las herramientas necesarias para ejecutar las pruebas y ver la cobertura.

### 6.4. Primer ciclo de ejecución de pruebas

- Ejecutar las pruebas encontradas con el objetivo de encontrar fallos en el sistema, corregir el código cuando se detecte algún problema.

### 6.5. Segundo ciclo de ejecución de pruebas

- Volver a ejecutar las pruebas para asegurar que las correcciones no afecten a otras partes que ya funcionaban.
- Implementar nuevas pruebas unitarias que estén fuera del happy path encontrado.

### 6.6. Tercer ciclo de ejecución de pruebas

- Ejecutar las pruebas unitarias para encontrar fallos y ver que estas nuevas no afecten al funcionamiento entre las diferentes partes del sistema.

### 6.7. Informe de Reporte de Estados y Finalización

- Generar reportes de resultados (defectos, cobertura, estado de pruebas) y un informe de finalización.
- Presentar hallazgos al docente, incluyendo los problemas superados como las lecciones aprendidas.

---

## 7. Personal

### 7.1. Roles, Actividades y Responsabilidades

Se utiliza la matriz RACI (Responsable, Apoyo, Consultado e Informado) donde:

- **R - Responsable:** Las personas que ejecutan la tarea o actividad, es decir, son quienes hacen el trabajo.
- **A - Aprobador / Responsable final (Accountable):** La persona que tiene la autoridad final sobre la actividad y se asegura de que se complete correctamente. Solo puede haber un "A" por actividad el cual es el TEST LEAD.
- **C - Consultado:** Personas que deben ser consultadas antes o durante la ejecución de la actividad. Son expertos o partes clave que brindan asesoría o información.
- **I - Informado:** Personas que deben ser notificadas del avance o resultados de la actividad. No participan directamente, pero necesitan estar al tanto.

| Rol/Actividad  | 1   | 2   | 3   | 4   | 5   | 6   | 7   |
| :------------- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| Instructor     | I   | I   | I   | I   | 1   | I   | I   |
| Test Lead      | A   | A   | I   | A   | A   | A   | A   |
| Test Analyst   | C   | R   | C   | R   | R   | R   | C   |
| Test Design    | R   | C   | C   | C   | C   | C   | C   |
| Test Architect | C   | I   | R   | I   | I   | I   | I   |

### 7.2. Necesidades de Contratación

Para este proyecto y en base a la carga estimada y el cronograma establecido para las actividades de prueba de BABYBUDDY, se ha llegado a la conclusión de que el equipo cuenta con los miembros necesarios para está primera etapa de pruebas unitarias.

### 7.3. Necesidades de Entrenamiento

Para garantizar un ejecucion de pruebas adecuado a las actividades se indicó que cada miembro del equipo indistintamente de su rol en el proyecto, OBLIGATORIAMENTE tiene que correr de forma local el proyecto e introducirse en el mismo de forma individual, con el fin de que cada miembro comprenda el sistema a su debido tiempo. De ser necesario se indicó que...

---

## 8. Cronograma

El cronograma de actividades está ubicado dentro de la herramienta “GitHub Projects” del proyecto.

- **Enlace:** https://github.com/users/acahuib/projects/3
