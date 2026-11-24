# markitdown

> Convert various files (PDF, Office, images, audio) to Markdown.
> More information: <https://github.com/microsoft/markitdown>.

- Convert a file and print to `stdout`:

`markitdown {{path/to/file.pdf}}`

- Save output to a specific file:

`markitdown {{path/to/file.pdf}} {{[-o|--output]}} {{path/to/output.md}}`

- Keep embedded base64 images instead of truncating them (such as from DOCX or HTML):

`markitdown --keep-data-uris {{path/to/file.docx}}`

- Convert a file using Azure Document Intelligence:

`markitdown {{path/to/file.pdf}} {{[-d|--use-docintel]}} {{[-e|--endpoint]}} {{endpoint_url}}`

- Display help:

`markitdown {{[-h|--help]}}`
