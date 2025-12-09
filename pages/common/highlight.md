# highlight

> Outputs syntax-highlighted source code to a variety of formats.
> More information: <http://andre-simon.de/doku/highlight/en/highlight.php>.

- Produce a complete HTML document from a source code file:

`highlight {{[-o|--out-format]}} {{html}} {{[-s|--style]}} {{theme_name}} {{[-S|--syntax]}} {{language}} {{path/to/source_code}}`

- Produce an HTML fragment, suitable for inclusion in a larger document:

`highlight {{[-o|--out-format]}} {{html}} {{[-f|--fragment]}} {{[-S|--syntax]}} {{language}} {{source_file}}`

- Inline the CSS styling in every tag:

`highlight {{[-o|--out-format]}} {{html}} --inline-css {{[-S|--syntax]}} {{language}} {{source_file}}`

- List all supported languages, themes, or plugins:

`highlight --list-scripts {{langs|themes|plugins}}`

- Print a CSS stylesheet for a theme:

`highlight {{[-o|--out-format]}} {{html}} --print-style {{[-s|--style]}} {{theme_name}} {{[-S|--syntax]}} {{language}} --stdout`
