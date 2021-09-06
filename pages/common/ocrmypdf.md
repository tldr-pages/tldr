# ocrmypdf

> Generate a searchable PDF or PDF/A from a scanned PDF or an image of text.
> More information: <https://ocrmypdf.readthedocs.io/en/latest/cookbook.html>.

- Create a new searchable PDF/A file from a scanned PDF or image file:

`ocrmypdf {{path/to/input_file}} {{path/to/output.pdf}}`

- Replace a scanned PDF file with a searchable PDF file:

`ocrmypdf {{path/to/file.pdf}} {{path/to/file.pdf}}`

- Skip pages of a mixed-format input PDF file that already contain text:

`ocrmypdf --skip-text {{path/to/input.pdf}} {{path/to/output.pdf}}`

- Clean, de-skew, and rotate pages of a poor scan:

`ocrmypdf --clean --deskew --rotate-pages {{path/to/input_file}} {{path/to/output.pdf}}`

- Set the metadata of the searchable PDF file:

`ocrmypdf --title "{{title}}" --author "{{author}}" --subject "{{subject}}" --keywords "{{keyword; key phrase; ...}}" {{path/to/input_file}} {{path/to/output.pdf}}`

- Display help:

`ocrmypdf --help`
