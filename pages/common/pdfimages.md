# pdfimages

> Utility for extracting images from PDFs.

- Extract all images from a PDF file and save them in PNG format:

`pdfimages -png {{PDF-file}} {{image-root}}`

- Extract images from a PDF file from pages 3-5:

`pdfimages -f 3 -l 5 {{PDF-file}} {{image-root}}`

- Extract images from a PDF file and include the page number in their names:

`pdfimages -p {{PDF-file}} {{image-root}}`

- List information about all the images in a PDF file:

`pdfimages -list {{PDF-file}}`

