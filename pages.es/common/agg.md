# agg

> Crea un archivo GIF a partir de una grabación de sesión de terminal de `asciinema`.
> Más información: <https://docs.asciinema.org/manual/agg/usage/>.

- Crea un archivo GIF:

`agg {{ruta/a/demo.cast}} {{ruta/a/demo.gif}}`

- Crea un archivo GIF de 80 columnas de ancho y 25 filas de alto:

`agg --cols 80 --rows 25 {{ruta/a/demo.cast}} {{ruta/a/demo.gif}}`

- Crea un archivo GIF con un tamaño de fuente de 24 píxeles:

`agg --font-size 24 {{ruta/a/demo.cast}} {{ruta/a/demo.gif}}`

- Muestra la ayuda:

`agg {{[-h|--help]}}`
