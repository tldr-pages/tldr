# wkhtmltopdf

> It is an open-source command-line tool that allows you to convert HTML documents or web pages into PDF files.
> t is primarily a command-line tool, which means you use it by running commands in a terminal or shell.
> More information: <https://wkhtmltopdf.org/docs.html>.

- Basic Conversion:

`wkhtmltopdf input.html output.pdf`

- Specifying Page Size:

`wkhtmltopdf --page-size A4 input.html output.pdf`

- Setting Margins:

`wkhtmltopdf --margin-top 10mm --margin-bottom 10mm --margin-left 10mm --margin-right 10mm input.html output.pdf`

- Custom Page Orientation:

`wkhtmltopdf --orientation Landscape input.html output.pdf`

- Generating Grayscale PDF:

`wkhtmltopdf --grayscale input.html output.pdf`
