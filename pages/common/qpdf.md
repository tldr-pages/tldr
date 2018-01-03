# qpdf

> Versatile PDF transformation software.

- Extract pages 1-3, 5 and 6-10 from a PDF file and save them as another one:

`qpdf --empty --pages {{input.pdf}} {{1-3,5,6-10}} -- {{output.pdf}}`

- Merge (concatenate) a list of PDF files and save the result as another one:

`qpdf --empty --pages {{file 1.pdf}} {{1,6-8}} --pages {{file 2.pdf}} {{3,4,5}} -- {{output.pdf}}`

- Write each group of n pages to a separate output file with a given filename pattern:

`qpdf --split-pages=n {{input.pdf}} {{out_%d.pdf}}`

- Rotate and transform the PDF:

`qpdf --rotate={{90:2,4,6}} --rotate={{180:7-8}} {{input.pdf}} {{output.pdf}}`

- Remove the password from a password protected file:

`qpdf --password={{password}} --decrypt {{input.pdf}} {{output.pdf}}`
