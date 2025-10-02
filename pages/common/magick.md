# magick

> Create, edit, compose, and convert images.
> This is the unified command-line interface for ImageMagick v7+.
> More information: <https://imagemagick.org/script/magick.php>.

- Convert an image from JPEG to PNG:

`magick {{path/to/input.jpg}} {{path/to/output.png}}`

- Resize an image to 50% of its original dimensions:

`magick {{path/to/input.png}} -resize 50% {{path/to/output.png}}`

- Resize an image to specific dimensions, keeping aspect ratio:

`magick {{path/to/input.png}} -resize {{800x600}} {{path/to/output.png}}`

- Create a GIF from a series of images with 100ms delay between frames:

`magick {{path/to/frame*.jpg}} -delay {{10}} {{path/to/animation.gif}}`

- Rotate an image 90 degrees clockwise:

`magick {{path/to/input.png}} -rotate {{90}} {{path/to/output.png}}`

- Apply a blur effect to an image:

`magick {{path/to/input.png}} -blur {{0x8}} {{path/to/output.png}}`

- Add text to an image:

`magick {{path/to/input.png}} -pointsize {{36}} -fill {{white}} -annotate {{+10+50}} {{text}} {{path/to/output.png}}`

- Display information about an image:

`magick identify {{path/to/image.png}}`
