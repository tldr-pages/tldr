# elm

> Elm forrásfájlok fordítása és futtatása. További információ: <https://elm-lang.org>.

- Elm projekt inicializálása, elm.json fájl generálása:

`elm init`

- Interaktív Elm shell indítása:

`elm repl`

- Elm fájl fordítása, az eredmény kimenete a `index.html` fájlba:

`elm make {{source}}`

- Elm fájl fordítása, az eredmény kimenete egy JavaScript fájlba:

`elm make {{source}} --output={{destination}}.js`

- Helyi webkiszolgáló indítása, amely az Elm-fájlokat oldalbetöltéskor fordítja:

`elm reactor`

- Elm csomag telepítése a https://package.elm-lang.org oldalról:

`elm install {{author}}/{{package}}`
