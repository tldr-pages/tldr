# markdown2pdf

> Convert markdown to PDF.
> More information: <https://github.com/theiskaa/markdown2pdf>.

- Convert a Markdown file to a PDF:

`markdown2pdf {{[-p|--path]}} {{path/to/input_file.md}}`

- Convert a Markdown file to a PDF with a specific path:

`markdown2pdf {{[-p|--path]}} {{path/to/input_file.md}} {{[-o|--output]}} {{path/to/output_file.pdf}}`

- Convert Markdown content provided as a string:

`markdown2pdf {{[-s|--string]}} {{markdown_text}} {{[-o|--output]}} {{path/to/output_file.pdf}}`

- Convert from URL (this will convert a Markdown file at that URL to a local PDF file):

`markdown2pdf {{[-u|--url]}} {{URL}} {{[-o|--output]}} {{path/to/output_file.pdf}}`
