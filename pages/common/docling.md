# docling

> Convert documents (PDF, DOCX, PPTX, HTML, images) to Markdown, JSON, or HTML using AI layout analysis and OCR.
> More information: <https://github.com/docling-project/docling>.

- Convert a file to Markdown in the current directory (replaces images with placeholders):

`docling {{path/to/file.pdf}}`

- Save the converted output to a specific directory:

`docling {{path/to/file.pdf}} --output {{path/to/directory}}`

- Extract images as separate PNG files linked in Markdown, or embed them as base64:

`docling --image-export-mode {{referenced|embedded}} {{path/to/file.pdf}}`

- Export the document structure and tables to a specific format:

`docling --to {{json|html|md|text}} {{path/to/file.pdf}}`

- Skip OCR to convert native digital PDFs much faster:

`docling --no-ocr {{path/to/file.pdf}}`

- Display help:

`docling {{[-h|--help]}}`
