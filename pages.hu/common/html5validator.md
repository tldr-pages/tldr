# html5validator

> Egy parancssori eszköz a HTML5 érvényességének tesztelésére. További információ: <https://github.com/svenkreiss/html5validator>.

- Egy adott fájl hitelesítése:

`html5validator {{path/to/file}}`

- Egy adott könyvtárban található összes HTML-fájl hitelesítése:

`html5validator --root {{path/to/directory}}`

- Figyelmeztetések és hibák megjelenítése:

`html5validator --show-warnings {{path/to/file}}`

- Több fájl összevetése glob-mintával:

`html5validator --root {{path/to/directory}} --match "{{*.html *.php}}"`

- Bizonyos könyvtárnevek figyelmen kívül hagyása:

`html5validator --root {{path/to/directory}} --blacklist "{{node_modules vendor}}"`

- Az eredmények meghatározott formátumban történő kiadása:

`html5validator --format {{gnu|xml|json|text}} {{path/to/file}}`

- A naplót egy adott szóbeliségi szinten adja ki:

`html5validator --root {{path/to/directory}} --log {{debug|info|warning}}`
