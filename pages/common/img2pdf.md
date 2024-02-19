# img2pdf

> Losslessly convert raster images to a PDF file.
> Some supported image formats are: GIF, JPEG, JPEG2000, PNG, GIF and TIFF.
> More information: <https://gitlab.mister-muffin.de/josch/img2pdf>.

- Convert one or more images to a single PDF, each image being on its own page:

`img2pdf {{path/to/image1.ext path/to/image2.ext ...}} --output {{path/to/file.pdf}}`

- Convert only the first frame of a multi-frame image to PDF:

`img2pdf {{path/to/file.gif}} --first-frame-only --output {{path/to/file.pdf}}`

- Auto orient the image, use a specific  page size in landscape mode, and set a border of specific sizes horizontally and vertically:

`img2pdf {{path/to/image.ext}} --auto-orient --pagesize {{A4^T}} --border {{2cm}}:{{5.1cm}} --output {{path/to/file.pdf}}`

- Shrink only larger images to a rectangle of specified dimensions inside a page with a specific size:

`img2pdf {{path/to/image.ext}} --pagesize {{30cm}}x{{20cm}} --imgsize {{10cm}}x{{15cm}} --fit {{shrink}} --output {{path/to/file.pdf}}`

- Convert an image to PDF, and specify metadata for the resulting file:

`img2pdf {{path/to/image.ext}} --title {{title}} --author {{author}} --creationdate {{1970-01-31}} --keywords {{keyword1 keyword2}} --subject {{subject}} --output {{path/to/file.pdf}}`
