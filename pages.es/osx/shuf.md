# shuf

> Genera permutaciones aleatorias.
> Más información: <https://keith.github.io/xcode-man-pages/shuf.1.html>.

- Ordena aleatoriamente las líneas de un fichero y muestra el resultado:

`shuf {{nombre_archivo}}`

- Sólo muestra las 5 primeras entradas del resultado:

`shuf --head-count={{5}} {{nombre_archivo}}`

- Escribe el resultado en otro archivo:

`shuf {{nombre_archivo}} --output={{nombre_archivo_salida}}`

- Genera números aleatorios en el rango 1-10:

`shuf --input-range={{1-10}}`
