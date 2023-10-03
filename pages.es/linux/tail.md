# tail

> Muestra las ultimas líneas de un archivo de texto en especifico.
> Más información: <https://www.linuxfoundation.org/blog/blog/classic-sysadmin-14-tail-and-head-commands-in-linux-unix>.

- Imprime las ultimas 'conteo' lineas de un archivo:

`tail --lines {{conteo}} {{/ruta/al/archivo}}`

- Imprime un archivo desde una linea en especifico:

`tail --lines +{{conteo}} {{/ruta/al/archivo}}`

- Imprime un numero especifico de bytes desde el final de algun archivo:

`tail --bytes {{conteo}} {{/ruta/al/archivo}}`

- Imprime las últimas líneas de un archivo en tiempo real hasta introducir `Ctrl + C`:

`tail --follow {{/ruta/al/archivo}}`

- Mantiene leyendo las ultimas lineas de un archivo hasta introducir `Ctrl + C`, aunque el archivo sea inaccedible:

`tail --retry --follow {{/ruta/al/archivo}}`

- Imprime las últimas 'conteo' lineas en 'archivo' y se refresca cada 'n' segundos:

`tail --lines {{conteo}} --sleep-interval {{segundos}} --follow {{ruta/al/archivo}}`
