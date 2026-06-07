# Catalogo de Requisitos No Funcionales: Baby Buddy

## version 1.0

### Se trasaladara a la wiki cuando se requiera

## 1. Introducción

Este documento detalla los Requisitos No Funcionales (RNF) del sistema Baby Buddy, basándose en los estándares de calidad de software (como ISO 25010) y adaptados a las particularidades del proyecto. Se establecen las características de calidad, rendimiento y restricciones que el sistema debe cumplir para garantizar una experiencia óptima para los cuidadores.

## 2. Requerimientos No Funcionales

### i. RNF-USAB - Usabilidad

<table>
  <tr style="background-color: #a4c2f4;">
    <td width="20%"><b>RNF-USAB-01</b></td>
    <td width="80%"><b>Usabilidad en Entornos Rápidos</b></td>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>La interfaz debe ser intuitiva y operable fácilmente por cuidadores que pueden estar cansados, con prisa o con una mano ocupada.</li>
        <li>Debe permitir iniciar el registro de actividades críticas (sueño, alimentación, pañales) con un máximo de dos clics desde el panel principal (Dashboard).</li>
        <li>La paleta de colores y la tipografía deben ofrecer alto contraste y legibilidad para visualización rápida.</li>
      </ul>
    </td>
  </tr>
</table>

### ii. RNF-REND - Rendimiento y Eficiencia

<table>
  <tr style="background-color: #a4c2f4;">
    <td width="20%"><b>RNF-REND-01</b></td>
    <td width="80%"><b>Tiempos de Respuesta Esperados</b></td>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>El sistema debe procesar y almacenar registros diarios comunes (como cambios de pañal o registros manuales) en un tiempo máximo de 1.5 segundos.</li>
        <li>La carga inicial del Dashboard, incluyendo todos los cálculos de tiempo transcurrido desde la última actividad, no debe exceder los 2.0 segundos bajo una conexión 4G estándar (aprox. 15 Mbps).</li>
      </ul>
    </td>
  </tr>
</table>

### iii. RNF-SEG - Seguridad y Privacidad

<table>
  <tr style="background-color: #a4c2f4;">
    <td width="20%"><b>RNF-SEG-01</b></td>
    <td width="80%"><b>Protección de Datos y Autenticación</b></td>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Todos los datos sensibles (información médica, medicación, métricas de crecimiento y rutinas del menor) deben almacenarse protegiendo la privacidad de los usuarios.</li>
        <li>El acceso a la plataforma debe estar estrictamente limitado mediante un sistema de autenticación seguro basado en sesiones o tokens.</li>
        <li>Debe requerirse autorización específica para compartir el acceso de un perfil de bebé con otros cuidadores, evitando el acceso público.</li>
      </ul>
    </td>
  </tr>
</table>

### iv. RNF-CONF - Confiabilidad y Disponibilidad

<table>
  <tr style="background-color: #a4c2f4;">
    <td width="20%"><b>RNF-CONF-01</b></td>
    <td width="80%"><b>Prevención de Pérdida de Datos</b></td>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>El sistema debe utilizar transacciones seguras en la base de datos (Django ORM) para evitar la corrupción o pérdida de registros durante interrupciones del servidor.</li>
        <li>Los temporizadores activos (ej. de sueño o extracción de leche) deben mantener su estado en el backend, permitiendo su recuperación inmediata incluso si el usuario cierra la aplicación o cambia de dispositivo.</li>
      </ul>
    </td>
  </tr>
</table>

### v. RNF-PORT - Portabilidad y Compatibilidad

<table>
  <tr style="background-color: #a4c2f4;">
    <td width="20%"><b>RNF-PORT-01</b></td>
    <td width="80%"><b>Diseño Responsivo e Integraciones API</b></td>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>La aplicación debe tener un diseño web estrictamente responsivo (Mobile-First), garantizando su correcto funcionamiento en navegadores de smartphones, tablets y pantallas de escritorio.</li>
        <li>El sistema debe exponer una API REST funcional que permita integraciones externas, posibilitando que plataformas como Home Assistant o botones IoT (ej. ESP32) envíen comandos de registro automático.</li>
      </ul>
    </td>
  </tr>
</table>

### vi. RNF-MANT - Mantenibilidad

<table>
  <tr style="background-color: #a4c2f4;">
    <td width="20%"><b>RNF-MANT-01</b></td>
    <td width="80%"><b>Código Limpio y Estándares Open Source</b></td>
  </tr>
  <tr>
    <td colspan="2">
      <ul>
        <li>Dado que es un proyecto Open Source basado en Python/Django, el código fuente debe apegarse rigurosamente a las guías de estilo PEP 8.</li>
        <li>El código debe incluir comentarios descriptivos y la lógica de negocio debe estar desacoplada, facilitando que nuevos colaboradores entiendan e implementen nuevas características.</li>
        <li>Se debe contar con una cobertura de pruebas automatizadas adecuada para validar regresiones ante futuras actualizaciones de versiones del backend en Django, y de las herramientas de compilación frontend (ej. Gulp/Node.js).</li>
      </ul>
    </td>
  </tr>
</table>
