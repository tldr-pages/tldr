# pup

> HTML parsing tool.

- Transform raw HTML file into a cleaned, indented, and colored format:

`cat {{index.html}} | pup --color`

- Filter HTML by element tag name:

`cat {{index.html}} | pup '{{tag}}'`

- Filter HTML by id:

`cat {{index.html}} | pup '{{tag#id}}'`

- Filter HTML by attribute value:

`cat {{index.html}} | pup '{{tag[attribute="value"}}'`

- Print all text from selected nodes and children:

`cat {{index.html}} | pup '{{tag}} text{}`

- Print HTML as JSON:

`cat {{index.html}} | pup '{{tag}} json{}'`

