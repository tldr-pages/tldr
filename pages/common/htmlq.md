# htmlq

> Use CSS selectors to extract content from HTML files.
> More information: <https://github.com/mgdm/htmlq>.

- Return all elements of class "card":

`cat file.html | htmlq '.card'`

- Get the text content of the first paragraph:

`cat file.html | htmlq --text 'p:first-of-type'`

- Find all the links in a page:

`cat file.html | htmlq --attribute href 'a'`

- Remove all images and SVGs from a page:

`cat file.html | htmlq --remove-nodes 'img' --remove-nodes 'svg'`

- Pretty print, this time using filepaths instead of stdin and stdout:

`htmlq --pretty --filename in.html --output out.html`
