# pdfbook2

> Create a double sided printable PDF booklet from a PDF.
> Note: The booklet needs to be printed double-sided in landscape mode, flipped on the long edge.
> More information: <https://github.com/jenom/pdfbook2#examples>.

- Create a booklet named `file-book.pdf` with sane defaults:

`pdfbook2 {{path/to/file.pdf}}`

- Create a booklet with the paper size set to A4:

`pdfbook2 {{[-p|--paper]}} a4paper {{path/to/file.pdf}}`

- Create a booklet that has the inner margin reduced to 50 pixels (default = 150px):

`pdfbook2 {{[-p|--paper]}} a4paper {{[-i|--inner-margin]}} 50 {{path/to/file.pdf}}`

- Organize a large file with print signatures for binding into a larger booklet (signatures must be divisible by 4):

`pdfbook2 {{[-p|--paper]}} a4paper --signature {{24}} {{path/to/file.pdf}}`
