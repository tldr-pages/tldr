# magick convert

> Convert between image formats, scale, join, and create images, and much more.
> Note: this tool (previously `convert`) has been replaced by `magick` in ImageMagick 7+.
> More information: <https://imagemagick.org/script/convert.php>.

- Convert an image from JPEG to PNG:

`magick convert {{path/to/input_image.jpg}} {{path/to/output_image.png}}`

- Scale an image to 50% of its original size:

`magick convert {{path/to/input_image.png}} -resize 50% {{path/to/output_image.png}}`

- Scale an image keeping the original aspect ratio to a maximum dimension of 640x480:

`magick convert {{path/to/input_image.png}} -resize 640x480 {{path/to/output_image.png}}`

- Scale an image to have a specified file size:

`magick convert {{path/to/input_image.png}} -define jpeg:extent=512kb {{path/to/output_image.jpg}}`

- Vertically/Horizontally append images:

`magick convert {{path/to/image1.png path/to/image2.png ...}} {{-append|+append}} {{path/to/output_image.png}}`

- Create a GIF from a series of images with 100ms delay between them:

`magick convert {{path/to/image1.png path/to/image2.png ...}} -delay {{10}} {{path/to/animation.gif}}`

- Create an image with nothing but a solid red background:

`magick convert -size {{800x600}} "xc:{{#ff0000}}" {{path/to/image.png}}`

- Create a favicon from several images of different sizes:

`magick convert {{path/to/image1.png path/to/image2.png ...}} {{path/to/favicon.ico}}`
