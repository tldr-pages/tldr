# ocrmypdf

> Generate a searchable PDF or PDF/A from a scanned PDF or an image of text.
> More information: <https://ocrmypdf.readthedocs.io/en/latest/introduction.html>.

- Create a new searchable PDF/A file from a scanned PDF or image file:

`ocrmypdf {{input_file}} {{output.pdf}}`

- Overwrite a scanned PDF file with a searchable PDF file, if successful:

`ocrmypdf {{input.pdf}}`

- Skip pages of a mixed-format input PDF file that already contain text:

`ocrmypdf --skip-text {{input.pdf}} {{output.pdf}}`

- Automatically clean, de-skew and rotate pages of a poor scan.

`ocrmypdf --clean --deskew --rotate-pages {{input_file}} {{output.pdf}}`

- Set the metadata of the searchable PDF file:

`ocrmypdf --title "Document Title" --author "Document Author" --subject "Subject Description" --keywords "Multiple Keywords" {{input_file}} {{output.pdf}}`

- Display help:

`ocrmypdf --help`
