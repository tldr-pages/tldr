# webpack

> Egy webes projekt js fájljainak és egyéb eszközeinek egyetlen kimeneti fájlba történő csomagolása. További információ: <https://webpack.js.org>.

- Egyetlen kimeneti fájl létrehozása egy belépési pontfájlból:

`webpack {{app.js}} {{bundle.js}}`

- CSS-fájlok betöltése is a JavaScript-fájlból (ez a `.css` fájlok CSS-töltőjét használja):

`webpack {{app.js}} {{bundle.js}} --module-bind '{{css=css}}'`

- Adjon át egy konfigurációs fájlt (pl. a belépési szkriptet és a kimeneti fájlnevet), és mutassa meg a fordítás előrehaladását:

`webpack --config {{webpack.config.js}} --progress`

- Automatikusan újrafordítja a projektfájlok módosításakor:

`webpack --watch {{app.js}} {{bundle.js}}`
