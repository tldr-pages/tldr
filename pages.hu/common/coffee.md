# coffee

> CoffeeScript szkripteket hajt végre, vagy fordítja le őket JavaScriptre. További információ: <https://coffeescript.org#cli>.

- Szkript futtatása:

`coffee {{path/to/file.coffee}}`

- JavaScriptre fordítás és mentés egy azonos nevű fájlba:

`coffee --compile {{path/to/file.coffee}}`

- JavaScriptre fordítás és mentés egy adott kimeneti fájlba:

`coffee --compile {{path/to/file.coffee}} --output {{path/to/file.js}}`

- REPL (interaktív shell) indítása:

`coffee --interactive`

- Figyelje a szkriptet a változásokra és futtassa újra a szkriptet:

`coffee --watch {{path/to/file.coffee}}`
