# silicon

> Create an image of source code.
> See also: `freeze`.
> More information: <https://github.com/Aloxaf/silicon#examples>.

- Generate an image from a specific source file:

`silicon {{path/to/source_file}} {{[-o|--output]}} {{path/to/output_image}}`

- Generate an image from a source file with a specific programming language syntax highlighting (e.g. `rust`, `py`, `js`, etc.):

`silicon {{path/to/source_file}} {{[-o|--output]}} {{path/to/output_image}} {{[-l|--language]}} {{language|extension}}`

- Do not generate window decorations in the image:

`silicon {{path/to/source_file}} {{[-o|--output]}} {{path/to/output_image}} --no-window-controls`

- Generate an image from `stdin`:

`{{command}} | silicon {{[-o|--output]}} {{path/to/output_image}}`

- Display help:

`silicon {{[-h|--help]}}`
