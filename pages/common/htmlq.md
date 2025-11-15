# htmlq

> Use CSS selectors to extract content from HTML files.
> More information: <https://github.com/mgdm/htmlq>.

- Return all elements of class `card`:

`cat {{path/to/file.html}} | htmlq '.card'`

- Get the text content of the first paragraph:

`cat {{path/to/file.html}} | htmlq --text 'p:first-of-type'`

- Find all the links in a page:

`cat {{path/to/file.html}} | htmlq --attribute href 'a'`

- Remove all images and SVGs from a page:

`cat {{path/to/file.html}} | htmlq --remove-nodes 'img' --remove-nodes 'svg'`

- Pretty print and write the output to a file:

`htmlq --pretty --filename {{path/to/input.html}} --output {{path/to/output.html}}`
