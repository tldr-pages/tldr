# ocrmypdf

> Generates a searchable PDF or PDF/A from a scanned PDF or an image of text.
> More information: <https://ocrmypdf.readthedocs.io/en/latest/introduction.html>

- Create a new searchable PDF/A file from a scanned PDF or image file:

`ocrmypdf {{input_pdf_or_image}} {{searchable.PDF}}`

- Overwrite a scanned PDF file with a searchable PDF file, if successful:

`ocrmypdf {{input.PDF}}`

- Skip pages of a mixed-format input PDF that already contain text:

`ocrmypdf --skip-text {{input.PDF}} {{searchable.PDF}}`

- Automatically clean, de-skew and rotate pages of a poor scan.

`ocrmypdf --clean --deskew --rotate-pages {{input_pdf_or_image}} {{searchable.PDF}}`

- Set the output PDF file's metadata:

`ocrmypdf --title "Document Title" --author "Document Author"
--subject "Subject Description" --keywords "Multiple Keywords"
{{input_pdf_or_image}} {{searchable.PDF}}`

- Display help:

`ocrmypdf --help`
