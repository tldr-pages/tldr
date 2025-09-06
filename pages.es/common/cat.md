# cat

> Imprime y concatena archivos.
> Más información: <https://manned.org/cat.1posix>.

- Imprime el contenido de un fichero a `stdout`:

`cat {{ruta/al/archivo}}`

- Concatena varios archivos en un archivo de salida:

`cat {{ruta/al/archivo1 ruta/al/archivo2 ...}} > {{ruta/al/archivo_salida}}`

- Añade el contenido de varios archivos a un archivo de salida:

`cat {{ruta/al/archivo1 ruta/al/archivo2 ...}} >> {{ruta/al/archivo_salida}}`

- Copia el contenido de un archivo en un archivo de salida sin almacenamiento en el búfer:

`cat -u {{/dev/tty12}} > {{/dev/tty13}}`

- Copia `stdin` en un archivo:

`cat - > {{ruta/al/archivo}}`
