# wkhtmltopdf

> An open-source command-line tool to convert HTML documents or web pages into PDF files.
> More information: <https://wkhtmltopdf.org/>.

- Convert a HTML document into PDF:

`wkhtmltopdf {{input.html}} {{output.pdf}}`

- Specify the PDF page size (please see `PaperSize` of `QPrinter` for supported sizes):

`wkhtmltopdf --page-size {{A4}} {{input.html}} {{output.pdf}}`

- Set the PDF page margins:

`wkhtmltopdf --margin-{{top|bottom|left|right}} {{10mm}} {{input.html}} {{output.pdf}}`

- Set the PDF page orientation:

`wkhtmltopdf --orientation {{Landscape|Portrait}} {{input.html}} {{output.pdf}}`

- Generate a greyscale version of the PDF document:

`wkhtmltopdf --grayscale {{input.html}} {{output.pdf}}`
