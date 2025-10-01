# fmt

> Reformatea un archivo de texto uniendo sus párrafos y limitando el ancho de línea a un número de caracteres (75 por defecto).
> Más información: <https://www.gnu.org/software/coreutils/manual/html_node/fmt-invocation.html>.

- Reformatea un archivo:

`fmt {{ruta/al/archivo}}`

- Reformatea un archivo produciendo líneas de salida de (como máximo) `n` caracteres:

`fmt {{[-w|--width]}} {{n}} {{ruta/al/archivo}}`

- Reformatea un archivo sin unir las líneas más cortas respecto al ancho dado:

`fmt {{[-s|--split-only]}} {{ruta/al/archivo}}`

- Reformatea un archivo con espaciado uniforme (1 espacio entre palabras y 2 espacios entre párrafos):

`fmt {{[-u|--uniform-spacing]}} {{ruta/al/archivo}}`
