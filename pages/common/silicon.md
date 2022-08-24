# silicon

> Create images of source code files.
> More information: <https://github.com/Aloxaf/silicon>.

- Generate an image from a specific source file:

`silicon  {{path/to/source_file}} --output {{path/to/output_image.png}}`

- Generate an image from a source file with a specific programing language syntax highlighting (e.g. `rust`, `py`, `js`, etc.):

`silicon  {{path/to/source_file}} --output {{path/to/output_image.png}} --language {{language_or_file_extension}}`

- Generate an image from stdin:

`{{command}} | silicon --output {{path/to/output_image.png}}`
