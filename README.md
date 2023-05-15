# WebApps_Tarea 1 y 2
**Desarrollo de Aplicaciones Web CC5002-1**  
+ Tarea 1 [Entregada el: 11-04-2023]  
+ Tarea 2 [Entregada el: --]  

**Enunciado 2**  
Implementar usando python con Flask y MySQL  

+ **URL inicio**: menu que permita acceder a las demás funcionalidades del sistema "Agregar Donacion", "Agregar Pedido", "Ver Donaciones" y "Ver Perdidos"  
(
    <span style="color:lightgreen">
        **backend** 
    </span>
    |
    <span style="color:yellow">
        frontend
    </span>
)  
+ **Agregar Donación**: mostrar el mismo formulario desarrollado en la tarea 1, mantener todas las validaciones realizadas con JS, pero al agregar y confirmar debe validar los datos en el lado del servidor e inserta un registro en la base de datos en la tabla "donacion" junto con almacenar los archivos que corresponda. Si todo resulta bien llevar a la pagina de inicio con un mensaje apropiado. Si fallan las validaciones mantener en el formulario. con los mensajes de validacion correspondientes.  
(
    <span style="color:red">
        backend 
    </span>
    |
    <span style="color:yellow">
        frontend
    </span>
)  
+ **Agregar Pedido**: lo mismo de agregar donacio pero con la tabla "pedido".  
(
    <span style="color:red">
        backend 
    </span>
    |
    <span style="color:yellow">
        frontend
    </span>
)
+ **Ver donaciones**: mostrar los datos tal como se indicó en la tarea 1, pero debe considerar grupos de 5 filas, si hay más de 5 debe mostrar las donaciones por página permitiendo avanzar y retroceder según corresponda. Si hace click en una donacion se debe mostrar la informacion de la donacion como se pidio en la tarea 1.  
(
    <span style="color:red">
        backend 
    </span>
    |
    <span style="color:yellow">
        frontend
    </span>
)  
+ **Ver pedidos**: lo mismo de ver donaciones pero con los datos de pedidos.  
(
    <span style="color:red">
        backend 
    </span>
    |
    <span style="color:yellow">
        frontend
    </span>
)

**NOTAS:**  
+ Hay fotos que daban libre uso a condicion de tener un link al sitio original. Es por eso que algunas imagenes llevan a una pagina externa.  
Todas las fotos fueron scadas de sitios que daban libre uso de ellas.  
+ La primera fila de donaciones lleva a informacion-donacion.html  
+ La ultima fila de pedidos lleva a informacion-pedido.html  
+ Con '`python app.py`' en la terminal corre la aplicación en debug
+ Librerías instaladas en el env. utilizado: flask, filetype, mysql