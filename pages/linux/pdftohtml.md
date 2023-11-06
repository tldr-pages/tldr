# pdftohtml

> Convert PDF files into HTML, XML and PNG images.
> More information: <https://manned.org/pdftohtml>.

- Convert a PDF file to an HTML file:

`pdftohtml {{path/to/file.pdf}} {{path/to/output_file.html}}`

- Ignore images in the PDF file:

`pdftohtml -i {{path/to/file.pdf}} {{path/to/output_file.html}}`

- Generate a single HTML file that includes all PDF pages:

`pdftohtml -s {{path/to/file.pdf}} {{path/to/output_file.html}}`

- Convert a PDF file to an XML file:

`pdftohtml -xml {{path/to/file.pdf}} {{path/to/output_file.xml}}`
