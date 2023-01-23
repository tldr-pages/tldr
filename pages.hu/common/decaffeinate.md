# decaffeinate

> A CoffeeScript forráskódjának modern JavaScriptre való átvitele. További információ: <https://decaffeinate-project.org>.

- CoffeeScript fájl átalakítása JavaScriptre:

`decaffeinate {{path/to/file.coffee}}`

- CoffeeScript v2 fájl átalakítása JavaScriptre:

`decaffeinate --use-cs2 {{path/to/file.coffee}}`

- Konvertálja a require és a `module.exports` importálásra és exportálásra:

`decaffeinate --use-js-modules {{path/to/file.coffee}}`

- Konvertáljon egy CoffeeScriptet, lehetővé téve a névre szóló exportot:

`decaffeinate --loose-js-modules {{path/to/file.coffee}}`
