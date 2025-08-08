# pdfbook2

> Create a double sided printable pdf booklet from an INPUT pdf.
> The OUTPUT pdf file will be named "INPUT-book.pdf" and created in the same directory as the INPUT file.
> Printing Note: the booklet needs to be printed double sided in landscape mode, flipped on the long edge.
> More information: <https://github.com/jenom/pdfbook2>.

- Basic command to create a booklet with sane defaults:

`pdfbook2 input.pdf`

- Output a booklet with the paper size set to A4:

`pdfbook2 --paper=a4paper input.pdf`

- Output booklet has the inner margin reduced to 50 pixels (default = 150px):

`pdfbook2 --paper=a4paper --inner-margin=50 input.pdf`

- Large input files can be output in print signatures for binding into a larger booklet (signatures must be divisible by 4):

`pdfbook2 --paper=a4paper --signature=24 input.pdf`
