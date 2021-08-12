# decaffeinate

> Mutați sursa dvs. de CoffeeScript în JavaScript modern.
> Mai multe informaţii: <https://decaffeinate-project.org>

- Conversia unui fișier CoffeesCript în JavaScript:

`decaffeinate {{path/to/file.coffee}}`

- Conversia unui fișier v2 CoffeeScript în JavaScript:

`decaffeinate --use-cs2 {{path/to/file.coffee}}`

- Conversia necesită și `module.exports` pentru a importa și exporta:

`decaffeinate --use-js-modules {{path/to/file.coffee}}`

- Conversia unui CoffeeScript, permițând exporturile numite:

`decaffeinate --loose-js-modules {{path/to/file.coffee}}`
