# cat

> Imprime y concatena archivos.
> Más información: <https://www.gnu.org/software/coreutils/cat>.

- Imprime el contenido de un archivo a `stdout`:

`cat {{ruta/al/archivo}}`

- Concatena varios archivos en un archivo:

`cat {{ruta/al/archivo1 ruta/al/archivo2 ...}} > {{ruta/al/archivo_resultado}}`

- Añade varios archivos a un archivo:

`cat {{ruta/al/archivo1 ruta/al/archivo2 ...}} >> {{ruta/al/archivo_resultado}}`

- Escribe `stdin` a un archivo:

`cat - > {{ruta/al/archivo}}`

- [n]umera todas las líneas de salida:

`cat -n {{ruta/al/archivo}}`

- Muestra caracteres no imprimibles y en blanco (con prefijo `M-` si no es ASCII):

`cat -v -t -e {{ruta/al/archivo}}`
