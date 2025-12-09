# stty

> Establece opciones para una interfaz del dispositivo terminal.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- Muestra todas las opciones de la terminal actual:

`stty --all`

- Establece el número de filas o columnas:

`stty {{filas|columnas}} {{cuenta}}`

- Obtiene la velocidad de transferencia real de un dispositivo:

`stty --file {{ruta/al/archivo_del_dispositivo}} speed`

- Restablece todos los modos a valores razonables para el terminal actual:

`stty sane`

- Cambia entre modo raw y cooked:

`stty {{raw|cooked}}`

- Desactiva o activa el eco de caracteres:

`stty {{-echo|echo}}`
