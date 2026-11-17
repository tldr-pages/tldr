# docling

> Convert documents (PDF, DOCX, PPTX, HTML, images) to Markdown, JSON, or HTML using AI layout analysis and OCR.
> More information: <https://github.com/docling-project/docling>.

- Convert a file to Markdown in the current directory:

`docling {{path/to/file.pdf}}`

- Save the converted output to a specific directory:

`docling {{path/to/file.pdf}} --output {{path/to/directory}}`

- Replace images with placeholders, or export them as separate PNG files referenced from the output:

`docling --image-export-mode {{placeholder|referenced}} {{path/to/file.pdf}}`

- Export the document structure and tables to a specific format:

`docling --to {{json|html|md|text}} {{path/to/file.pdf}}`

- Skip OCR to convert native digital PDFs much faster:

`docling --no-ocr {{path/to/file.pdf}}`

- Display help:

`docling {{[-h|--help]}}`
