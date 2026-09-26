# agg

> Maak een GIF van een `asciinema` terminal opname.
> Meer informatie: <https://docs.asciinema.org/manual/agg/usage/>.

- Maak een GIF:

`agg {{pad/naar/demo.cast}} {{pad/naar/demo.gif}}`

- Maak een GIF die 80 kolommen breed en 25 rijen hoog is:

`agg --cols 80 --rows 25 {{pad/naar/demo.cast}} {{pad/naar/demo.gif}}`

- Maak een GIF met een lettergrootte van 24 pixels:

`agg --font-size 24 {{pad/naar/demo.cast}} {{pad/naar/demo.gif}}`

- Toon de help:

`agg {{[-h|--help]}}`
