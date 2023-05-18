# WebApps_Tarea 1 y 2
**Desarrollo de Aplicaciones Web CC5002-1**  
+ Tarea 1 [Entregada el: 11-04-2023]  
+ Tarea 2 [Entregada el: --]  

**Enunciado 2**  
Implementar usando python con Flask y MySQL  

+ **URL inicio**: menu que permita acceder a las demás funcionalidades del sistema "Agregar Donacion", "Agregar Pedido", "Ver Donaciones" y "Ver Perdidos"  
(
    <span style="color:lightgreen"> **Backend** </span>
    | <span style="color:lightgreen"> **Frontend** </span>
)  
+ **Agregar Donación**: mostrar el mismo formulario desarrollado en la tarea 1, mantener todas las validaciones realizadas con JS, pero al agregar y confirmar debe validar los datos en el lado del servidor e inserta un registro en la base de datos en la tabla "donacion" junto con almacenar los archivos que corresponda. Si todo resulta bien llevar a la pagina de inicio con un mensaje apropiado. Si fallan las validaciones mantener en el formulario. con los mensajes de validacion correspondientes.  
(
    <span style="color:lightgreen"> **validación** </span> 
    | <span style="color:lightgreen"> **registrar donación en BD** </span>
    | <span style="color:lightgreen"> **registrar foto en BD** </span>
    | <span style="color:lightgreen"> **Acierto validación** </span>
    | <span style="color:lightgreen"> **Fallo validación** </span>
    | <span style="color:#d9c43f"> **Frontend** </span>
)  

+ **Agregar Pedido**: lo mismo de agregar donación pero con la tabla "pedido".  
(
    <span style="color:lightgreen"> **validación** </span> 
    | <span style="color:lightgreen"> **registrar pedido en BD** </span>
    | <span style="color:lightgreen"> **Acierto validación** </span>
    | <span style="color:lightgreen"> **Fallo validación** </span>
    | <span style="color:#d9c43f"> **Frontend** </span>
)  
+ **Ver donaciones**: mostrar los datos tal como se indicó en la tarea 1, pero debe considerar grupos de 5 filas, si hay más de 5 debe mostrar las donaciones por página permitiendo avanzar y retroceder según corresponda. Si hace click en una donacion se debe mostrar la informacion de la donacion como se pidio en la tarea 1.  
(
    <span style="color:lightgreen"> **Llamada a BD** </span>
    | <span style="color:lightgreen"> **Funcionamiento páginas** </span>
    | <span style="color:lightgreen"> **Link a donación** </span>
    | <span style="color:#d9c43f"> **Frontend** </span>
)  
+ **Ver pedidos**: lo mismo de ver donaciones pero con los datos de pedidos.  
(
    <span style="color:lightgreen"> **Llamada a BD** </span>
    | <span style="color:lightgreen"> **Funcionamiento páginas** </span>
    | <span style="color:lightgreen"> **Link a pedido** </span>
    | <span style="color:#d9c43f"> **Frontend** </span>
)

###### Significado de Colores:  <span style="color:lightgreen"> **Implementado Funciona** </span> | <span style="color:#d9c43f"> **Implementado no funciona | Revizar** </span> | <span style="color:#cf2533"> **No Implementado** </span>  



**NOTAS:**  
+ Hay fotos que daban libre uso a condicion de tener un link al sitio original. Es por eso que algunas imagenes llevan a una pagina externa. Todas las fotos fueron sacadas de sitios que daban libre uso de ellas.  
+ La primera fila de donaciones lleva a informacion-donacion.html  
+ La última fila de pedidos lleva a informacion-pedido.html  
+ Con '`python app.py`' en la terminal corre la aplicación en debug
+ Librerías instaladas en el env. utilizado: flask, filetype, mysql

[comment]: # (
    PALETA DE COLORES: 
    verde: lightgreen , 
    amarillo: #d9c43f , 
    rojo:     #cf2533 
    )