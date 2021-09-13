# img2pdf

> Command-line lossless converter of raster images to PDF
> More information: <https://pypi.org/project/img2pdf/>.

- Convert images to PDF:

`img2pdf {{image1.jpg}} {{image2.jpg}} -o out.pdf`

- Convert all PNGs in the current directory to a single pdf:

`img2pdf *.{{png}} -o out.pdf`

- Convert only the first page of multi-page images to pdf:

`img2pdf example.gif {{--first-frame-only}} -o out.pdf`

- Auto orient to A4 page size in landscape mode and a border of 2cm horizontally and 5.1cm vertically:

`img2pdf example.jpeg --auto-orient --pagesize {{A4^T}} --border {{2cm:5.1cm}} -o out.pdf `

- Shrink only larger images to a 10cm by 15cm rectangle inside a 30x20cm page:

`img2pdf example.tiff --pagesize {{30cmx20cm}} --imgsize {{10cmx15cm}} --fit {{shrink}} -o out.pdf`

- Set metadata:

`img2pdf example.png --title {{title}} --author {{author}} --creationdate {{1970-01-31}} --keywords {{keywords}} --subject {{subject}} -o out.pdf`

- Force RGB as colorspace:

`img2pdf example.png --colorspace {{RGB}} -o out.pdf`
