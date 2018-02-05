# postcss

> PostCSS is a tool for transforming styles with JS plugins.

- Parse and transform a CSS file:

`postcss {{path/to/file}}`

- Parse and transform a CSS file and output to a specific file:

`postcss {{path/to/file}} --output {{path/to/file}}`

- Parse and transform CSS file(s) and output to a specific directory:

`postcss {{path/to/file}} --dir {{path/to/directory}}`

- Parse and transform CSS file(s) in-line:

`postcss {{path/to/file}} --replace`

- Specify a custom PostCSS parser:

`postcss {{path/to/file}} --parser {{parser}}`

- Specify a custom PostCSS syntax:

`postcss {{path/to/file}} --syntax {{syntax}}`

- Parse and transform CSS file(s) by watching for changes:

`postcss {{path/to/file}} --watch`

- Display available options and examples:

`postcss --help`
