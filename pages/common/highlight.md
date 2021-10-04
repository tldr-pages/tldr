# highlight

> Outputs syntax-highlighted source code to a variety of formats.
> More information: <http://www.andre-simon.de/doku/highlight/highlight.php>.

- Produce a complete HTML document from a source code file:

`highlight -O {{html}} --style {{theme_name}} --syntax={{language}} {{path/to/source_code}}`

- Produce an HTML fragment, suitable for inclusion in a larger document:

`highlight -O html --fragment --syntax={{language}} {{source file}}`

- Inline the CSS styling in every tag:

`highlight -O html --inline-css --syntax={{language}} {{source file}}`

- List all supported languages:

`highlight --list-scripts lang`

- List all installed syntax highlighting themes:

`highlight --list-scripts themes`

- Print a CSS stylesheet for a theme:

`highlight -O html --print-style --style {{theme name}} --syntax {{language}}] --stdout`
