# wkhtmltopdf

> An open-source command-line tool to convert HTML documents or web pages into PDF files.
> More information: <https://wkhtmltopdf.org/>.

- Basic Conversion:

`wkhtmltopdf {{input.html}} {{output.pdf}}`

- Specify Page Size (please see `PaperSize` of `QPrinter` for supported sizes):

`wkhtmltopdf --page-size {{A4}} {{input.html}} {{output.pdf}}`

- Set Margins:

`wkhtmltopdf --margin-top 10mm --margin-bottom 10mm --margin-left 10mm --margin-right 10mm input.html output.pdf`

- Custom Page Orientation:

`wkhtmltopdf --orientation Landscape input.html output.pdf`

- Generate Grayscale PDF:

`wkhtmltopdf --grayscale input.html output.pdf`
