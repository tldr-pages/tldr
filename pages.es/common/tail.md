# tail

> Muestra las últimas líneas de un archivo de texto determinado.
> Ver también: `head`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html#tail-invocation>.

- Imprime las últimas 'conteo' líneas de un archivo:

`tail --lines {{conteo}} {{ruta/al/archivo}}`

- Imprime un archivo desde una línea específica:

`tail --lines +{{conteo}} {{ruta/al/archivo}}`

- Imprime un número específico de bytes desde el final de algún archivo:

`tail --bytes {{conteo}} {{ruta/al/archivo}}`

- Imprime las últimas líneas de un archivo en tiempo real hasta introducir `Ctrl + C`:

`tail --follow {{ruta/al/archivo}}`

- Mantiene leyendo las últimas líneas de un archivo hasta introducir `Ctrl + C`, aunque el archivo sea inaccesible:

`tail --retry --follow {{ruta/al/archivo}}`

- Imprime las últimas 'conteo' líneas en 'archivo' y se actualiza cada 'n' segundos:

`tail --lines {{conteo}} --sleep-interval {{segundos}} --follow {{ruta/al/archivo}}`
