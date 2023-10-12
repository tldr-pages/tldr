# pstoedit

> Convert PDF files into various image formats.
> More information: <http://www.pstoedit.net>.

- Convert a PDF page to PNG or JPEG format:

`pstoedit -page {{page_number}} -f magick {{path/to/file.pdf}} {{page.png|page.jpg]}}`

- Convert multiple PDF pages to numbered images:

`pstoedit -f magick {{path/to/file}} {{page%d.png|page%d.jpg}}`
