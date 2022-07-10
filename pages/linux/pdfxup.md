# pdfxup

> N-up PDF pages.
> More information: <https://ctan.org/pkg/pdfxup>.

- 2-up a PDF:

`pdfxup -o {{output.pdf}} {{input.pdf}}`

- Create a PDF with 3 columns and 2 lines per page:

`pdfxup -x {{3}} -y {{2}} -o {{output.pdf}} {{input.pdf}}`

- Booklet mode (2-up and pages are sorted to form a book when folded):

`pdfxup -b -o {{output.pdf}} {{input.pdf}}`
