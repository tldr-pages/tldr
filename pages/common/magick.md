# ImageMagick

> Create, edit, compose, or convert bitmap images.
> More information: <https://imagemagick.org/>.

- Convert file type:

`magick {{image.png}} {{image.jpg}}`

- Resize an image, making a new copy:

`magick convert -resize {{100x100}} {{image.jpg}} {{image.jpg}}`

- Create a GIF using images:

`magick {{*.jpg}} {{images.gif}}`

- Create checkerboard pattern:

`magick -size {{640x480}} pattern:checkerboard {{checkerboard.png}}`

- Convert images to individual PDF pages:

`magick {{*.jpg}} +adjoin {{page-%d.pdf}}`
