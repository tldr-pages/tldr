# pdftoppm

> Convert PDF document pages to Portable Pixmap (image formats).
> More information: <https://manned.org/pdftoppm>.

- Specify the range of pages to convert (N-first page, M-last page):

`pdftoppm -f {{N}} -l {{M}} {{file.pdf}} {{image_name_prefix}}`

- Convert only the first page:

`pdftoppm -singlefile {{file.pdf}} {{image_name_prefix}}`

- Generate a monochrome PBM file (instead of a color PPM file):

`pdftoppm -mono {{file.pdf}} {{image_name_prefix}}`

- Generate a grayscale PGM file (instead of a color PPM file):

`pdftoppm -gray {{file.pdf}} {{image_name_prefix}}`

- Generate a PNG file instead a PPM file:

`pdftoppm -png {{file.pdf}} {{image_name_prefix}}`
