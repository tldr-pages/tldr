# tee

> Lee desde la entrada estándar y escribe a la salida estándar a la vez que a archivos o comandos.
> Más información: <https://manned.org/tee.1>

- Copia la entrada estándar al archivo, reemplazando su contenido, y también ala salida estándar:

`echo {{ejemplo}} | tee {{ruta/al/archivo}}`

- Anexa la entrada estándar al archivo, sin reemplazar:

`echo {{ejemplo}} | tee -a {{ruta/al/archivo}}`

- Imprime la entrada estándar a la terminal, y también lo reenvía a otro programa para posterior procesamiento:

`echo {{ejemplo}} | tee {{/dev/tty}} | {{xargs printf "[%s]"}}`
