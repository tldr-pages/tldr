# pdfimages

> Utility for extracting images from PDFs.

- Extract all images from a PDF file and save them as PNGs:

`pdfimages -png {{PDF-file}} {{image-root}}`

- Extract images from pages 3 to 5:

`pdfimages -f {{3}} -l {{5}} {{PDF-file}} {{image-root}}`

- Extract images from a PDF file and include the page number in the output filenames:

`pdfimages -p {{PDF-file}} {{image-root}}`

- List information about all the images in a PDF file:

`pdfimages -list {{PDF-file}}`
