# qpdf

> Versatile PDF transformation software.

- Extract a few pages from a pdf into another one:

`qpdf --empty --pages {{input.pdf}} 1,6-8,12 -- {{output.pdf}}`

- Extract pages from multiple pdf files into one:

`qpdf --empty --pages {{file 1.pdf}} 1,6-8 --pages {{file 2.pdf}} 3,4,5 -- {{output.pdf}}`

- Write each group of n pages to a separate output file:

`qpdf --split-pages=n {{input.pdf}} {{page %d.pdf}}`

- Rotate and transform the PDF:

`qpdf --rotate=+90:2,4,6 --rotate=180:7-8 {{input.pdf}} {{output.pdf}}`

- Remove the password from a password protected file:

`qpdf --password={{password}} --decrypt {{input.pdf}} {{output.pdf}}`
