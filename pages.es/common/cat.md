# cat

> Imprime y concatena archivos.

- Imprime el contenido de un archivo por la salida estándar:

`cat {{archivo}}`

- Concatena múltiples archivos dentro de un archivo determinado:

`cat {{archivo1}} {{archivo2}} > {{archivo_final}}`

- Añade múltiples archivos dentro de un archivo determinado:

`cat {{archivo1}} {{archivo2}} >> {{archivo_final}}`

- Muestra el número de líneas de un archivo:

`cat -n {{archivo}}`

- Muestra los carácteres no imprimibles y espacios en blanco (con el prefijo `M-` si no es ASCII):

`cat -v -t -e {{archivo}}`
