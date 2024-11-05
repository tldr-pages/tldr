# pandoc

> Convert documents between various formats.
> More information: <https://pandoc.org/MANUAL.html>.

- Convert file to PDF (the output format is determined by file extension):

`pandoc {{path/to/input.md}} {{-o|--output}} {{path/to/output.pdf}}`

- Convert to a standalone file with the appropriate headers/footers (for LaTeX, HTML, etc.):

`pandoc {{path/to/input.md}} {{-s|--standalone}} {{-o|--output}} {{path/to/output.html}}`

- Manually specify format detection and conversion (overriding automatic format detection using filename extension or when filename extension is missing altogether):

`pandoc {{-f|-r|--from|--read}} {{docx|...}} {{path/to/input}} {{-t|-w|--to|--write}} {{pdf|...}} {{-o|--output}} {{path/to/output}}`

- List all supported input formats:

`pandoc --list-input-formats`

- List all supported output formats:

`pandoc --list-output-formats`
