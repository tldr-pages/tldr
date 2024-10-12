# pandoc

> Convert documents between various formats.
> More information: <https://pandoc.org>.

- Convert file to PDF (the output format is determined by file extension):

`pandoc {{input.md}} -o {{output.pdf}}`

- Convert to a standalone file with the appropriate headers/footers (for LaTeX, HTML, etc.):

`pandoc {{input.md}} -s -o {{output.html}}`

- Force conversion to use a specific format:

`pandoc {{input.docx}} --to {{gfm}} -o {{output.md}}`

- List all supported input formats:

`pandoc --list-input-formats`

- List all supported output formats:

`pandoc --list-output-formats`
