# pdf-parser

> Identify fundamental elements of a PDF file without rendering it.
> More information: <https://blog.didierstevens.com/programs/pdf-tools>.

- Display statistics for a PDF file:

`pdf-parser -a {{path/to/file.pdf}}`

- Select objects of a given type in a PDF file:

`pdf-parser -t {{/type}} {{path/to/file.pdf}}`

- Search for strings in indirect objects:

`pdf-parser -s {{search_string}} {{path/to/file.pdf}}`
