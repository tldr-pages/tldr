# htmlq

> Use CSS selectors to extract content from HTML files.
> More information: <https://github.com/mgdm/htmlq>.

- Return all elements of class `card`:

`htmlq '.card' < {{path/to/file.html}}`

- Get the text content of the first paragraph:

`htmlq --text 'p:first-of-type' < {{path/to/file.html}}`

- Find all the links in a page:

`htmlq --attribute href 'a' < {{path/to/file.html}}`

- Remove all images and SVGs from a page:

`htmlq --remove-nodes 'img' --remove-nodes 'svg' < {{path/to/file.html}}`

- Pretty print and write the output to a file:

`htmlq --pretty --filename {{path/to/input.html}} --output {{path/to/output.html}}`
