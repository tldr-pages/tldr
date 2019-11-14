# html5validator

> A command line tool for testing HTML5 validity.
> More information: <https://github.com/svenkreiss/html5validator>.

- Validate a specific file:

`html5validator {{path/to/file}}`

- Validate all HTML files in a specific directory:

`html5validator --root {{path/to/directory}}`

- Show warnings as well as errors:

`html5validator --show-warnings {{path/to/file}}`

- Match multiple files using a glob pattern:

`html5validator --root {{path/to/directory}} --match "{{*.html *.php}}"`

- Ignore specific directory names:

`html5validator --root {{path/to/directory}} --blacklist "{{node_modules vendor}}"`

- Output the results in a specific format:

`html5validator --format {{gnu|xml|json|text}} {{path/to/file}}`

- Output the log at a specific verbosity level:

`html5validator --root {{path/to/directory}} --log {{debug|info|warning}}`
