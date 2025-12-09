# pdfdetach

> List or extract attachments (embedded files) from a PDF file.
> See also: `pdfattach`, `pdfimages`, `pdfinfo`.
> More information: <https://manned.org/pdfdetach>.

- List all attachments in a file with a specific text encoding:

`pdfdetach list -enc {{UTF-8}} {{path/to/input.pdf}}`

- Save specific embedded file by specifying its number:

`pdfdetach -save {{number}} {{path/to/input.pdf}}`

- Save specific embedded file by specifying its name:

`pdfdetach -savefile {{name}} {{path/to/input.pdf}}`

- Save the embedded file with a custom output filename:

`pdfdetach -save {{number}} -o {{path/to/output}} {{path/to/input.pdf}}`

- Save the attachment from a file secured by owner/user password:

`pdfdetach -save {{number}} {{-opw|-upw}} {{password}} {{path/to/input.pdf}}`
