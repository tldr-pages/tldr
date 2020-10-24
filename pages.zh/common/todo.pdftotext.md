# pdftotext

> Convert PDF files to plain text format.

- Convert filename.pdf to plain text and print it to standard output:

`pdftotext {{filename.pdf}} -`

- Convert filename.pdf to plain text and save it as filename.txt:

`pdftotext {{filename.pdf}}`

- Convert filename.pdf to plain text and preserve the layout:

`pdftotext -layout {{filename.pdf}}`

- Convert input.pdf to plain text and save it as output.txt:

`pdftotext {{input.pdf}} {{output.txt}}`

- Convert pages 2, 3 and 4 of input.pdf to plain text and save them as output.txt:

`pdftotext -f {{2}} -l {{4}} {{input.pdf}} {{output.txt}}`
