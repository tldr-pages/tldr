# agg

> Create a GIF from an `asciinema` terminal session recording.
> More information: <https://docs.asciinema.org/manual/agg/usage/>.

- Create a GIF:

`agg {{path/to/demo.cast}} {{path/to/demo.gif}}`

- Create a GIF that is 80 columns wide and 25 rows in height:

`agg --cols 80 --rows 25 {{path/to/demo.cast}} {{path/to/demo.gif}}`

- Create a GIF with a font size of 24 pixels:

`agg --font-size 24 {{path/to/demo.cast}} {{path/to/demo.gif}}`

- Display help:

`agg {{[-h|--help]}}`
