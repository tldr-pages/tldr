# postcss

> Transform styles with JS plugins.
> More information: <https://github.com/postcss/postcss-cli#usage>.

- Parse and transform a CSS file:

`postcss {{path/to/file}}`

- Parse and transform a CSS file and output to a specific file:

`postcss {{path/to/file}} {{[-o|--output]}} {{path/to/file}}`

- Parse and transform a CSS file and output to a specific directory:

`postcss {{path/to/file}} {{[-d|--dir]}} {{path/to/directory}}`

- Parse and transform a CSS file in-place:

`postcss {{path/to/file}} {{[-r|--replace]}}`

- Specify a custom PostCSS parser:

`postcss {{path/to/file}} --parser {{parser}}`

- Specify a custom PostCSS syntax:

`postcss {{path/to/file}} --syntax {{syntax}}`

- Watch for changes to a CSS file:

`postcss {{path/to/file}} {{[-w|--watch]}}`

- Display help:

`postcss {{[-h|--help]}}`
