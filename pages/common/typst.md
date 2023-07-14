# typst

> Compile a typst file to PDF.
> More information: <https://github.com/typst/typst>.

- List all discoverable fonts in the system and the given directory:

`typst --font-path {{path/to/fontDir}} fonts`

- Compile a Typst file directly:

`typst compile {{path/to/source.typ path/to/output.pdf}}`

- Watch changes on a Typst file and compile dynamically:

`typst watch {{path/to/source.typ path/to/output.pdf}}`
