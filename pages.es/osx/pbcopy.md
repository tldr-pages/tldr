# pbcopy

> Copia datos de `stdin` al portapapeles.
> Comparable a pulsar Cmd + C en el teclado.
> Más información: <https://ss64.com/osx/pbcopy.html>.

- Coloca el contenido de un archivo específico en el portapapeles:

`pbcopy < {{ruta/al/archivo}}`

- Coloca los resultados de un comando específico en el portapapeles:

`find . -type t -name "*.png" | pbcopy`
