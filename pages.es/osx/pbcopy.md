# pbcopy

> Copia datos de `stdin` al portapapeles.
> Comparable a pulsar Cmd + C en el teclado.
> Más información: <https://keith.github.io/xcode-man-pages/pbcopy.1.html>.

- Coloca el contenido de un archivo específico en el portapapeles:

`pbcopy < {{ruta/al/archivo}}`

- Coloca los resultados de un comando específico en el portapapeles:

`find . -type t -name "*.png" | pbcopy`
