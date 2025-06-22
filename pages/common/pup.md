# pup

> Command-line HTML parsing tool.
> More information: <https://github.com/ericchiang/pup>.

- Transform a raw HTML file into a cleaned, indented, and colored format:

`pup --color < {{index.html}}`

- Filter HTML by element tag name:

`pup '{{tag}}' < {{index.html}}`

- Filter HTML by ID:

`pup '{{div#id}}' < {{index.html}}`

- Filter HTML by attribute value:

`pup '{{input[type="text"]}}' < {{index.html}}`

- Print all text from the filtered HTML elements and their children:

`pup '{{div}} text{}' < {{index.html}}`

- Print HTML as JSON:

`pup '{{div}} json{}' < {{index.html}}`
