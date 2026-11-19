# karbon

> Calligra's vector drawing and diagramming application.
> See also: `calligraflow`, `calligrastage`, `calligrawords`, `calligrasheets`.
> More information: <https://manned.org/karbon>.

- Launch the drawing application:

`karbon`

- Open a specific drawing:

`karbon {{path/to/file.svg}}`

- Create a new document from a template file:

`karbon --new {{path/to/file.svg}}`

- Launch Calligra Stage with an interactive dialog to print the document:

`karbon {{path/to/file.svg}} --print`

- Launch Calligra Stage with an interactive dialog to export the document to PDF:

`karbon {{path/to/file.svg}} --export-pdf`

- Launch Calligra Stage and export document to PDF to a specific file:

`karbon {{path/to/input.svg}} --export-pdf --export-filename {{path/to/output.pdf}}`

- Display help or version:

`karbon --{{help|version}}`
