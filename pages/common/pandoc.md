# pandoc

> Convert documents between various formats.
> More information: <https://pandoc.org>.

- Convert file to pdf (the output format is determined by file extension):

`pandoc {{input.md}} -o {{output.pdf}}`

- Force conversion to use a specific format:

`pandoc {{input.docx}} --to {{markdown_github}} -o {{output.md}}`

- Convert to a standalone file with the appropriate headers/footers (for LaTeX, HTML, etc.):

`pandoc {{input.md}} -s -o {{output.tex}}`

- List all supported input formats:

`pandoc --list-input-formats`

- List all supported output formats:

`pandoc --list-output-formats`
