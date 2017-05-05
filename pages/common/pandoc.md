# pandoc

> Convert documents between various formats.

- Convert file to pdf (the output format is automatically determined from the output file's extension):

`pandoc {{input.md}} -o {{output.pdf}}`

- Convert a file to a specific output format (useful for when the extension alone is ambiguous):

`pandoc {{input.docx}} --to {{markdown_github}} -o {{output.md}}`

- List all supported input formats:

`pandoc --list-input-formats`

- List all supported output formats:

`pandoc --list-output-formats`
