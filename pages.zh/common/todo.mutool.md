# mutool

> Convert PDF files, query information and extract data.
> More information: <https://mupdf.com/docs>.

- Convert pages 1-10 into 10 PNG images:

`mutool convert -o {{image%d.png}} {{file.pdf}} {{1-10}}`

- Convert pages 2, 3 and 5 of a PDF into text in the standard output:

`mutool draw -F {{txt}} {{file.pdf}} {{2,3,5}}`

- Concatenate two PDFs:

`mutool merge -o {{output.pdf}} {{input1.pdf}} {{input2.pdf}}`

- Query information about all content embedded in a PDF:

`mutool info {{input.pdf}}`

- Extract all images, fonts and resources embedded in a PDF out into the current directory:

`mutool extract {{input.pdf}}`
