# cat

> Imprime y concatena ficheros.

- Imprime el contenido de un fichero por la salida estándar:

`cat {{fichero}}`

- Concatena múltiples ficheros dentro de un fichero determinado:

`cat {{fichero1}} {{fichero2}} > {{fichero_final}}`

- Añade múltiples ficheros dentro de un fichero determinado:

`cat {{fichero1}} {{fichero2}} >> {{fichero_final}}`

- Muestra el número de líneas de un fichero:

`cat -n {{fichero}}`

- Muestra los carácteres no imprimibles y espacios en blanco (con el prefijo `M-` si no es ASCII):

`cat -v -t -e {{fichero}}`
