# tail

> Muestra las últimas líneas de un archivo de texto determinado.
> Vea también: `head`.
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Imprime las últimas líneas de 'recuento' de un archivo:

`tail {{[-n|--lines]}} {{recuento}} {{ruta/al/archivo}}`

- Imprime un archivo desde una línea específica:

`tail {{[-n|--lines]}} +{{recuento}} {{ruta/al/archivo}}`

- Imprime un número específico de bytes desde el final de algún archivo:

`tail {{[-n|--lines]}} {{recuento}} {{ruta/al/archivo}}`

- Imprime las últimas líneas de un archivo en tiempo real hasta presionar `<Ctrl c>`:

`tail {{[-f|--follow]}} {{ruta/al/archivo}}`

- Mantiene leyendo las últimas líneas de un archivo hasta presionar `<Ctrl c>`, aunque el archivo sea inaccesible:

`tail {{[-F|--retry --follow]}} {{ruta/al/archivo}}`

- Imprime las últimas líneas de 'recuento' en 'archivo' y se actualiza cada 'n' segundos:

`tail {{[-n|--lines]}} {{recuento}} {{[-s|--sleep-interval]}} {{segundos}} {{[-f|--follow]}} {{ruta/al/archivo}}`
