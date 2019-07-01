# coffee

> Esegui script CoffeScript o compilali in JavaScript.
> Maggiori informazioni: <https://coffeescript.org#cli>.

- Esegui uno script:

`coffee {{percorso/al/file.coffee}}`

- Compila in JavaScript e salva lo script con lo stesso nome:

`coffee --compile {{percorso/al/file.coffee}}`

- Compila in JavaScript e salva lo script specificandone il nome:

`coffee --compile {{percorso/al/file.coffee}} --output {{percorso/al/file.js}}`

- Esegui una console REPL interattiva:

`coffee --interactive`

- Monitora cambiamenti in uno script rieseguendolo ogni volta:

`coffee --watch {{percorso/al/file.coffee}}`
