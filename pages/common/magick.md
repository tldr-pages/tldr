# magick

> Create, edit, compose, or convert bitmap images.
> ImageMagick version 7+. See `convert` for versions 6 and below.
> More information: <https://imagemagick.org/>.

- Convert file type:

`magick {{image.png}} {{image.jpg}}`

- Resize an image, making a new copy:

`magick {{image1.jpg}} -resize {{100x100}} {{image2.jpg}}`

- Create a GIF using images:

`magick {{*.jpg}} {{images.gif}}`

- Create checkerboard pattern:

`magick -size {{640x480}} pattern:checkerboard {{checkerboard.png}}`

- Convert images to individual PDF pages:

`magick {{*.jpg}} +adjoin {{page-%d.pdf}}`
