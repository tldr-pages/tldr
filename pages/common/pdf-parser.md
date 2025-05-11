# pdf-parser

> Identify fundamental elements of a PDF file without rendering it.
> More information: <https://blog.didierstevens.com/programs/pdf-tools>.

- Display statistics for a PDF file:

`pdf-parser {{[-a|--stats]}} {{path/to/file.pdf}}`

- Display objects of type `/Font` in a PDF file:

`pdf-parser {{[-t|--type]}} {{/Font}} {{path/to/file.pdf}}`

- Search for strings in indirect objects:

`pdf-parser {{[-s|--search]}} {{search_string}} {{path/to/file.pdf}}`
