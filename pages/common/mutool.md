# mutool

> Convert PDF files, query information and extract data.
> More information: <https://mupdf.readthedocs.io/en/latest/mupdf-command-line.html>.

- Convert pages 1-10 into 10 PNGs (Note: `%nd` in the output placeholder must be replaced with a print modifier like `%d` or `%2d`):

`mutool convert -o {{path/to/output%nd.png}} {{path/to/input.pdf}} {{1-10}}`

- Convert pages 2, 3 and 5 of a PDF into text in the standard output:

`mutool draw -F {{txt}} {{path/to/input.pdf}} {{2,3,5}}`

- Concatenate multiple PDF files:

`mutool merge -o {{path/to/output.pdf}} {{path/to/input1.pdf path/to/input2.pdf ...}}`

- Query information about all content embedded in a PDF:

`mutool info {{path/to/input.pdf}}`

- Extract all images, fonts and resources embedded in a PDF out into the current directory:

`mutool extract {{path/to/input.pdf}}`

- Print the outline (table of contents) of a PDF:

`mutool show {{path/to/input.pdf}} outline`
