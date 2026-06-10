### 4.3.2. Editar perfil de bebé

| ID                      | CPF-0002                                                                                                                                                                                              |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Funcionalidad**       | Editar perfil de bebé                                                                                                                                                                                 |
| **Descripción**         | Formulario que permite modificar los datos de un bebé previamente registrado en el sistema.                                                                                                           |
| **Requisito Asociado**  | RF-003.2                                                                                                                                                                                              |
| **Precondiciones**      | Acceder a la página estando autenticado en el sistema. Debe existir al menos un bebé registrado previamente.                                                                                          |
| **Datos de Entrada**    | Nombre<br>Apellido<br>Fecha de nacimiento<br>Hora de nacimiento<br>Foto                                                                                                                               |
| **Pasos de Ejecución**  | 1. Ingresar a la lista de bebés.<br>2. Seleccionar el perfil del bebé existente.<br>3. Hacer clic en "Editar".<br>4. Modificar los datos deseados.<br>5. Presionar el botón para guardar los cambios. |
| **Técnicas de Pruebas** | Partición de equivalencia<br>Valores Límites                                                                                                                                                          |
| **Prioridad**           | Media                                                                                                                                                                                                 |

#### Técnicas de pruebas implementadas

**Partición de equivalencia**

| Cod.         | Campo               | Clase Válida                    | Clases No Válidas                    |
| :----------- | :------------------ | :------------------------------ | :----------------------------------- |
| FN3.2-PE-001 | Nombre              | Texto modificado válido         | Texto borrado (vacío), solo espacios |
| FN3.2-PE-002 | Apellido            | Texto modificado, borrado       | N/A                                  |
| FN3.2-PE-003 | Fecha de Nacimiento | Fecha modificada válida         | Fecha borrada, formato incorrecto    |
| FN3.2-PE-004 | Hora de Nacimiento  | Hora modificada válida, borrada | Formato incorrecto (letras)          |
| FN3.2-PE-005 | Foto                | Reemplazo por imagen válida     | Archivo que no es imagen (.pdf)      |

**Valores límite**

| Cod.         | Campo               | Límite Inferior Válido                 | Límite Inferior No Válido  | Límite Superior Válido     | Límite Superior No Válido        |
| :----------- | :------------------ | :------------------------------------- | :------------------------- | :------------------------- | :------------------------------- |
| FN3.2-VL-001 | Nombre              | 1 caracter                             | 0 caracteres (vacío)       | 255 caracteres             | 256 caracteres                   |
| FN3.2-VL-002 | Fecha de Nacimiento | Fecha antigua lógica (Ej. hace 5 años) | Fechas ilógicas (Ej. 1970) | Día de Hoy                 | Día de Mañana (Futuro)           |
| FN3.2-VL-003 | Hora de Nacimiento  | 00:00 (Inicio del día)                 | N/A                        | Hora actual (Si nació Hoy) | Hora en el futuro (Si nació Hoy) |

**Catálogo de Pruebas**

| #CP          | Códigos de regla  | Datos de Entrada                                 | Resultado Esperado                                        | Obs |
| :----------- | :---------------- | :----------------------------------------------- | :-------------------------------------------------------- | :-- |
| FN3.2-CP-001 | FN3.2-PE-001      | Cambiar Nombre a "Mateo"                         | Datos del bebé actualizados correctamente                 | f+  |
| FN3.2-CP-002 | FN3.2-VL-001      | Borrar el Nombre por completo (0 chars)          | Error: El nombre es obligatorio                           | f-  |
| FN3.2-CP-003 | FN3.2-PE-003      | Modificar Fecha de nacimiento a "texto-invalido" | Error: Formato de fecha incorrecto                        | f-  |
| FN3.2-CP-004 | FN3.2-VL-001      | Añadir más letras al Nombre hasta llegar a 256   | Error: El nombre es demasiado largo                       | f-  |
| FN3.2-CP-005 | FN3.2-VL-002      | Cambiar Fecha de nacimiento al "Día de Mañana"   | Error: La fecha no puede ser en el futuro                 | f-  |
| FN3.2-CP-006 | FN3.2-PE-005      | Reemplazar Foto actual con un archivo ".pdf"     | Error: El archivo debe ser una imagen                     | f-  |
| FN3.2-CP-007 | FN3.2-VL-002      | Modificar Fecha de nacimiento a "01/01/1970"     | Error: Edad superior al límite lógico para un bebé        | f-  |
| FN3.2-CP-008 | FN3.2-VL-003      | Modificar Hora al futuro (manteniendo fecha Hoy) | Error: La hora no puede ser en el futuro si nació hoy     | f-  |
| FN3.2-CP-009 | FN3.2-PE-004      | Modificar Hora de nacimiento a "mediodia"        | Error: Formato de hora incorrecto                         | f-  |
| FN3.2-CP-010 | Lógica de Negocio | Cambiar Nombre a uno ya existente en otro bebé   | Datos actualizados, genera URL única para evitar colisión | f+  |

---

**Justificación de técnicas utilizadas:**
Al igual que en la creación, se utilizó la **Partición de Equivalencia** para validar que las modificaciones de formato de archivo o fechas/horas mantengan coherencia lógica al actualizar el registro. Los **Valores Límite** aseguran que al editar no se pueda exceder el tamaño asignado por la base de datos ni establecer parámetros temporales absurdos (como retrasar un nacimiento existente al año 1970 o adelantarlo al futuro). No se requirió Tabla de Decisión porque la edición reemplaza campos independientes y directos, sin generar ramificaciones lógicas.
