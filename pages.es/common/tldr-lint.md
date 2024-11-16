# tldr-lint

> Verifica y formatea páginas `tldr`.
> Más información: <https://github.com/tldr-pages/tldr-lint>.

- Verifica (lint) todas las páginas:

`tldr-lint {{pages_directory}}`

- Formatea una página específica hacia `stdout`:

`tldr-lint --format {{page.md}}`

- Formatea cada página sin escribir otros archivos o en la salida estándar:

`tldr-lint --format --in-place {{pages_directory}}`
