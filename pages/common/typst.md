# typst

> Compile a Typst file to PDF.
> Note: Specifying the output location is optional.
> More information: <https://github.com/typst/typst>.

- List all discoverable fonts in the system and the given directory:

`typst --font-path {{path/to/fonts_directory}} fonts`

- Compile a Typst file:

`typst compile {{path/to/source.typ}} {{path/to/output.pdf}}`

- Watch a Typst file and recompile on changes:

`typst watch {{path/to/source.typ}} {{path/to/output.pdf}}`
