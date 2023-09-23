# pdftohtml

> Pdftohtml is a program to convert PDF files into HTML, XML and PNG images.
> More information: <https://linux.die.net/man/1/pdftohtml>.

- Convert a pdf file to a html file:

`pdftohtml {{path/to/pdf}} {{path/to/html}}`

- Ignore images in the pdf file:

`pdftohtml -i {{path/to/pdf}} {{path/to/html}}`

- Generate a single HTML that includes all pdf pages:

`pdftohtml -s {{path/to/pdf}} {{path/to/html}}`

- Convert a pdf file to a xml file:

`pdftohtml -xml {{path/to/pdf}} {{path/to/html}}`
