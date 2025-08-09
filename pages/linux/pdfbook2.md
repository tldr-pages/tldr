# pdfbook2

> Create a double sided printable pdf booklet from an INPUT pdf.
> Printing Note: the booklet needs to be printed double sided in landscape mode, flipped on the long edge.
> More information: <https://github.com/jenom/pdfbook2>.

- Create a booklet named `file-book.pdf` with sane defaults:

`pdfbook2 {{path/to/file.pdf}}`

- Create a booklet with the paper size set to A4:

`pdfbook2 {{[-p|--paper]}} a4paper {{path/to/file.pdf}}`

- Output booklet has the inner margin reduced to 50 pixels (default = 150px):

`pdfbook2 --paper=a4paper --inner-margin=50 input.pdf`

- Large INPUT files can be OUTPUT organised in print signatures for binding into a larger booklet (signatures must be divisible by 4):

`pdfbook2 --paper=a4paper --signature=24 input.pdf`
