# elm

> Compila ed esegui file sorgente Elm.
> Maggiori informazioni: <https://elm-lang.org>.

- Inizializza un progetto Elm, generando un file `elm.json`:

`elm init`

- Avvia una shell Elm interattiva:

`elm repl`

- Compila un file Elm, scrivendo il risultato in un file `index.html`:

`elm make {{sorgente}}`

- Compila un file Elm, scrivendo il risultato in un file JavaScript:

`elm make {{sorgente}} --output={{destinazione}}.js`

- Avvia un web server locale che compila file Elm al caricamento delle pagine:

`elm reactor`

- Installa un pacchetto Elm da <https://package.elm-lang.org>:

`elm install {{author}}/{{package}}`
