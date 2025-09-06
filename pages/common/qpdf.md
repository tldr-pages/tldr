# qpdf

> Versatile PDF transformation software.
> More information: <https://github.com/qpdf/qpdf>.

- Extract pages 1-3, 5 and 6-10 from a PDF file and save them as another one:

`qpdf --empty --pages {{path/to/input.pdf}} {{1-3,5,6-10}} -- {{path/to/output.pdf}}`

- Merge (concatenate) all the pages of multiple PDF files and save the result as a new PDF:

`qpdf --empty --pages {{path/to/file1.pdf file2.pdf ...}} -- {{path/to/output.pdf}}`

- Merge (concatenate) given pages from a list of PDF files and save the result as a new PDF:

`qpdf --empty --pages {{path/to/file1.pdf}} {{1,6-8}} {{path/to/file2.pdf}} {{3,4,5}} -- {{path/to/output.pdf}}`

- Write each group of `n` pages to a separate output file with a given filename pattern:

`qpdf --split-pages={{n}} {{path/to/input.pdf}} {{path/to/out_%d.pdf}}`

- Rotate certain pages of a PDF with a given angle:

`qpdf --rotate={{90:2,4,6}} --rotate={{180:7-8}} {{path/to/input.pdf}} {{path/to/output.pdf}}`

- Remove the password from a password-protected file:

`qpdf --password={{password}} --decrypt {{path/to/input.pdf}} {{path/to/output.pdf}}`
