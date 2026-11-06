# calligrasheets

> Calligra's spreadsheet application.
> See also: `calligraflow`, `calligrastage`, `calligrawords`, `karbon`.
> More information: <https://manned.org/calligrasheets>.

- Launch the spreadsheet application:

`calligrasheets`

- Open a specific spreadsheet:

`calligrasheets {{path/to/file.ods}}`

- Create a new document from a template file:

`calligrasheets --new {{path/to/file.ods}}`

- Launch Calligra Sheets with an interactive dialog to print the document:

`calligrasheets {{path/to/file.ods}} --print`

- Launch Calligra Sheets with an interactive dialog to export the document to PDF:

`calligrasheets {{path/to/file.ods}} --export-pdf`

- Launch Calligra Sheets and export document to PDF to a specific file:

`calligrasheets {{path/to/input.ods}} --export-pdf --export-filename {{path/to/output.pdf}}`

- Display help or version:

`calligrasheets --{{help|version}}`
