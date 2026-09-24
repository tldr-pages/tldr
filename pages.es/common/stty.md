# stty

> Establece u obtiene opciones para la interfaz de un dispositivo de terminal.
> Vea también: `tput`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/stty-invocation.html>.

- Muestra el tamaño actual del terminal:

`stty size`

- Muestra todos los ajustes del terminal actual:

`stty {{[-a|--all]}}`

- Establece el número de filas o columnas:

`stty {{rows|cols}} {{cuenta}}`

- Obtiene la velocidad de transferencia real de un dispositivo:

`stty {{[-F|--file]}} {{ruta/al/archivo_del_dispositivo}} speed`

- Restablece todos los modos a valores razonables para la terminal actual:

`stty sane`

- Cambia entre el modo sin procesar y el modo normal:

`stty {{raw|cooked}}`

- Activa o desactiva el eco de caracteres:

`stty {{-echo|echo}}`

- Muestra la ayuda:

`stty --help`
