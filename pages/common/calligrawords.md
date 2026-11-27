# calligrawords

> Calligra's word processor application.
> See also: `calligraflow`, `calligrastage`, `calligrasheets`, `karbon`.
> More information: <https://manned.org/calligrawords>.

- Launch the word processor application:

`calligrawords`

- Open a specific document:

`calligrawords {{path/to/file.odt}}`

- Create a new document from a template file:

`calligrawords --new {{path/to/file.odt}}`

- Launch Calligra Words with an interactive dialog to print the document:

`calligrawords {{path/to/file.odt}} --print`

- Launch Calligra Words with an interactive dialog to export the document to PDF:

`calligrawords {{path/to/file.odt}} --export-pdf`

- Launch Calligra Words and export document to PDF to a specific file:

`calligrawords {{path/to/input.odt}} --export-pdf --export-filename {{path/to/output.pdf}}`

- Display help or version:

`calligrawords --{{help|version}}`
