# html5validator

> Un instrument de linie de comandă pentru testarea validității HTML5.
> Mai multe informaţii: <https://github.com/svenkreiss/html5validator>

- Validează un anumit fișier:

`html5validator {{path/to/file}}`

- Validează toate fișierele HTML într-un anumit director:

`html5validator --root {{path/to/directory}}`

- Afișați avertismente precum și erori:

`html5validator --show-warnings {{path/to/file}}`

- Potriviți mai multe fișiere folosind un model glob:

`html5validator --root {{path/to/directory}} --match "{{*.html *.php}}"`

- Ignoră anumite nume de directoare:

`html5validator --root {{path/to/directory}} --blacklist "{{node_modules vendor}}"`

- Ieșiți rezultatele într-un format specific:

`html5validator --format {{gnu|xml|json|text}} {{path/to/file}}`

- Ieșiți jurnalul la un anumit nivel de verbozitate:

`html5validator --root {{path/to/directory}} --log {{debug|info|warning}}`
