# pstoedit

> Convert PDF files into various image formats.
> More information: <http://www.pstoedit.net/>

- Convert a PDF page to PNG or JPEG [f]ormat:

'pstoedit -page {{page_number}}  -f magick {{filename}}  page.png|page.jpg'

- Convert multiple PDF pages to numbered images:

'pstoedit -f magick {{filename}} page%d.png|page%d.jpg'

