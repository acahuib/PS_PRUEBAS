Diseño de Casos de Pruebas Funcionales

Basado en el catálogo de requisitos versión 1.1

**Requisito Funcional 3**

1. Desarrollo de los Casos de prueba
   1. Añadir perfil de bebe (RF 3.1)

| ID                      | CPF-0001                                                                                                                                                                    |
| :---------------------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Funcionalidad**       | Añadir perfil de bebe                                                                                                                                                       |
| **Descripción**         | _Permite al cuidador registrar a un nuevo bebé en el sistema con su información básica._                                                                                    |
| **Requisito Asociado**  | RF-003                                                                                                                                                                      |
| **Precondiciones**      | Acceder a la página estando autenticado en el sistema.                                                                                                                      |
| **Datos de Entrada**    | Nombre Apellido Fecha de Nacimiento Hora de Nacimiento Foto                                                                                                                 |
| **Pasos de Ejecución**  | Ingresar a la página principal Hacer click en botón “Children” Se selecciona la opción “+ Child” Ingresar los datos mencionados anteriormente Presionar el botón para crear |
| **Técnicas de Pruebas** | Partición de equivalencia Valores Límites                                                                                                                                   |
| **Prioridad**           | Alta                                                                                                                                                                        |

    **Técnicas de pruebas implementadas**

    **Partición de equivalencia**

| Cod.       | Campo               | Clase Válida                          | Clases No Válidas                      |
| :--------- | :------------------ | :------------------------------------ | :------------------------------------- |
| FN3-PE-001 | Nombre              | Texto alfanumérico, no vacío          | Vacío, solo espacios                   |
| FN3-PE-002 | Apellido            | Texto alfanumérico, vacío             | N/A, debido a que es un campo OPCIONAL |
| FN3-PE-003 | Fecha de Nacimiento | Formato de fecha válido               | Vacío, formato incorrecto (letras)     |
| FN3-PE-004 | Hora de Nacimiento  | Formato de hora válido (HH:MM), Vacío | Formato incorrecto (letras)            |
| FN3-PE-005 | Foto                | formato archivo de imagen             | Archivos que no son imagen             |

    **Valores Limite**

| Cod.       | Campo               | Límite Inferior No Válido | Límite Inferior Válido | Límite Superior Válido     | Límite Superior No Válido        |
| :--------- | :------------------ | :------------------------ | :--------------------- | :------------------------- | :------------------------------- |
| FN3-VL-001 | Nombre              | 0 caracteres              | 1 carácter             | 255 caracteres             | 256 caracteres                   |
| FN3-VL-002 | Fecha de Nacimiento | Fechas ilógicas           | Fecha antigua lógica   | Día de Hoy                 | Día de Mañana (Futuro)           |
| FN3-VL-003 | Hora de Nacimiento  | N/A                       | 00:00 (Inicio del día) | Hora actual (Si nació Hoy) | Hora en el futuro (Si nació Hoy) |

    **Catálogo de Pruebas**

| \#CP       | Códigos de regla                                           | Datos de Entrada                                         | Resultado Esperado                                                    | Obs |
| :--------- | :--------------------------------------------------------- | :------------------------------------------------------- | :-------------------------------------------------------------------- | :-- |
| FN3-CP-001 | FN3-PE-001, FN3-PE-002, FN3-PE-003, FN3-VL-001, FN3-VL-002 | Nombre: "Lucas", Apellido: "Perez", Fecha: "Hoy"         | Bebé agregado correctamente                                           | f+  |
| FN3-CP-002 | FN3-PE-001, FN3-VL-001                                     | Nombre: "" (vacío), Fecha: "Hoy"                         | Error: El nombre es obligatorio                                       | f-  |
| FN3-CP-003 | FN3-VL-001                                                 | Nombre: (256 caracteres), Fecha: "Hoy"                   | Error: El nombre es demasiado largo                                   | f-  |
| FN3-CP-004 | FN3-PE-003                                                 | Nombre: "Lucas", Fecha: "trece de marzo"                 | Error: Formato de fecha incorrecto (Evadiendo UI)                     | f-  |
| FN3-CP-005 | FN3-VL-002                                                 | Nombre: "Lucas", Fecha: "Día de Mañana"                  | Error: La fecha no puede ser en el futuro                             | f-  |
| FN3-CP-006 | FN3-PE-005                                                 | Nombre: "Lucas", Fecha: "Hoy", Foto: "documento.pdf"     | Error: El archivo debe ser una imagen                                 | f-  |
| FN3-CP-007 | FN3-VL-002                                                 | Nombre: "Adulto", Fecha: "01/01/1970"                    | Error: Edad superior a límite lógico para un bebé                     | f-  |
| FN3-CP-008 | FN3-VL-003                                                 | Nombre: "Lucas", Fecha: "Hoy", Hora: "Dentro de 2 horas" | Error: La hora no puede ser en el futuro si nació hoy                 | f-  |
| FN3-CP-009 | FN3-PE-004                                                 | Nombre: "Lucas", Fecha: "Hoy", Hora: "mediodia"          | Error: Formato de hora incorrecto                                     | f-  |
| FN3-CP-010 |                                                            | Nombre: "Lucas" (Ya existe otro "Lucas")                 | Bebé guardado con éxito, genera URL única autoincremental (/lucas-1/) | f+  |

2. Editar perfil de bebe (3.2) 3. Eliminar perfil de bebe (3.3) 4. Listar y ver perfil de bebe

3.
