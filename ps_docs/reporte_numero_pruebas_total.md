# Reporte de Pruebas de Software

A continuación se detalla la cantidad de pruebas realizadas según los reportes revisados:

---

### 1. API

| Componente | Cantidad | Notas              |
| :--------- | :------- | :----------------- |
| Tests      | 119      | Solo es un archivo |

---

### 2. BABYBUDDY

| Componente         | Cantidad | Notas                                                      |
| :----------------- | :------- | :--------------------------------------------------------- |
| Commands           | 4        |                                                            |
| Forms              | 16       |                                                            |
| Home assistant     | 4        | 1 error, falso positivo                                    |
| Models             | 1        |                                                            |
| Reverse_proxy_auth | 2        |                                                            |
| Site_settings      | 2        |                                                            |
| Templatetags       | 2        |                                                            |
| Views              | 9        | 5 fallas, posibilidad de falsos positivos ($302 \neq 200$) |
| **TOTAL**          | **40**   |                                                            |

---

### 3. CORE

| Componente    | Cantidad | Notas |
| :------------ | :------- | :---- |
| Forms         | 63       |       |
| Import_export | 15       |       |
| Models        | 32       |       |
| Templatetags  | 9        |       |
| Utils         | 4        |       |
| Views         | 16       |       |
| **TOTAL**     | **139**  |       |

---

### 4. DASHBOARD

| Componente   | Cantidad |
| :----------- | :------- |
| Templatetags | 20       |
| Views        | 1        |

---

### 5. REPORTS

| Componente                 | Cantidad |
| :------------------------- | :------- |
| Graph.feedings_pattern     | 1        |
| Graph.medication_frequency | 1        |
| Graph.medication_intervals | 1        |
| Graph.sleep_pattern        | 1        |
| Views                      | 1        |

---

## Resumen Total

- **Total de pruebas contabilizadas:** 324
