# mupdf

> MuPDF is a lightweight PDF, XPS, and E-book viewer.
> More information: <https://www.mupdf.com>.

- Open a PDF on the first page:

`mupdf {{filename}}`

- Open a PDF on page 3:

`mupdf {{filename}} {{3}}`

- Open a password secured PDF:

`mupdf -p {{password}} {{filename}}`

- Open a PDF with an initial zoom level, specified as DPI, of 72:

`mupdf -r {{72}} {{filename}}`

- Open a PDF with inverted color:

`mupdf -I {{filename}}`

- Open a PDF tinted red #FF0000 (hexadecimal color syntax RRGGBB):

`mupdf -C {{FF0000}}`

- Open a PDF without anti-aliasing (0 = off, 8 = best):

`mupdf -A {{0}}`
