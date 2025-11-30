# htmlq

> Use CSS selectors to extract content from HTML files.
> More information: <https://github.com/mgdm/htmlq#usage>.

- Return all elements of class `card`:

`cat {{path/to/file.html}} | htmlq '.card'`

- Get the text content of the first paragraph:

`cat {{path/to/file.html}} | htmlq {{[-t|--text]}} 'p:first-of-type'`

- Find all the links in a page:

`cat {{path/to/file.html}} | htmlq {{[-a|--attribute]}} href 'a'`

- Remove all images and SVGs from a page:

`cat {{path/to/file.html}} | htmlq {{[-r|--remove-nodes]}} 'img' {{[-r|--remove-nodes]}} 'svg'`

- Pretty print and write the output to a file:

`htmlq {{[-p|--pretty]}} {{[-f|--filename]}} {{path/to/input.html}} {{[-o|--output]}} {{path/to/output.html}}`
