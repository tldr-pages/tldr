# tail

> Muestra las últimas líneas de un archivo de texto determinado.
> Ver también: `head`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html#tail-invocation>.

- Imprime las últimas líneas de 'recuento' de un archivo:

`tail --lines {{recuento}} {{ruta/al/archivo}}`

- Imprime un archivo desde una línea específica:

`tail --lines +{{recuento}} {{ruta/al/archivo}}`

- Imprime un número específico de bytes desde el final de algún archivo:

`tail --bytes {{recuento}} {{ruta/al/archivo}}`

- Imprime las últimas líneas de un archivo en tiempo real hasta presionar `Ctrl + C`:

`tail --follow {{ruta/al/archivo}}`

- Mantiene leyendo las últimas líneas de un archivo hasta presionar `Ctrl + C`, aunque el archivo sea inaccesible:

`tail --retry --follow {{ruta/al/archivo}}`

- Imprime las últimas líneas de 'recuento' en 'archivo' y se actualiza cada 'n' segundos:

`tail --lines {{recuento}} --sleep-interval {{segundos}} --follow {{ruta/al/archivo}}`
