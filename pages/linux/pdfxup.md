# pdfxup

> N-up PDF pages.
> More information: <https://ctan.org/pkg/pdfxup>.

- Create a 2-up PDF:

`pdfxup -o {{path/to/output.pdf}} {{path/to/input.pdf}}`

- Create a PDF with 3 columns and 2 lines per page:

`pdfxup -x {{3}} -y {{2}} -o {{path/to/output.pdf}} {{path/to/input.pdf}}`

- Booklet mode (2-up and pages are sorted to form a book when folded):

`pdfxup -b -o {{output.pdf}} {{input.pdf}}`
