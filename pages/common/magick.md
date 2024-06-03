# magick

> Create, edit, compose, or convert between image formats.
> This tool replaces `convert` in ImageMagick 7+. See `magick convert` to use the old tool in versions 7+.
> Some subcommands, such as `mogrify` have their own usage documentation.
> More information: <https://imagemagick.org>.

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
