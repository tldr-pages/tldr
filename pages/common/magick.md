# magick

> Create, edit, compose, or convert between image formats.
> ImageMagick version 7+. See `convert` for versions 6 and below.
> More information: <https://imagemagick.org/>.

- Convert between image formats:

`magick {{path/to/input_image.png}} {{path/to/output_image.jpg}}`

- Resize an image, making a new copy:

`magick {{path/to/input_image.jpg}} -resize {{100x100}} {{path/to/output_image.jpg}}`

- Create a GIF out of all JPEG images in the current directory:

`magick {{*.jpg}} {{path/to/images.gif}}`

- Create a checkerboard pattern:

`magick -size {{640x480}} pattern:checkerboard {{path/to/checkerboard.png}}`

- Create a PDF file out of all JPEG images in the current directory:

`magick {{*.jpg}} -adjoin {{path/to/file.pdf}}`
