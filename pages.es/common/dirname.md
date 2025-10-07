# dirname

> Calcula el directorio padre de una ruta de archivo o directorio.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/dirname-invocation.html>.

- Calcula el directorio padre de una ruta dada:

`dirname {{ruta/a/archivo_o_directorio}}`

- Calcula el directorio padre de múltiples rutas:

`dirname {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`

- Delimita la salida con un carácter NUL en lugar de una nueva línea (útil cuando se combina con `xargs`):

`dirname {{[-z|--zero]}} {{ruta/al/archivo_o_directorio1 ruta/al/archivo_o_directorio2 ...}}`
