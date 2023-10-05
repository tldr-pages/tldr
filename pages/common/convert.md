# convert

> Image conversion tool.
> Part of ImageMagick.
> More information: <https://imagemagick.org/script/convert.php>.

- Convert an image from JPG to PNG:

`convert {{path/to/input_image.jpg}} {{path/to/output_image.png}}`

- Scale an image to 50% of its original size:

`convert {{path/to/input_image.png}} -resize 50% {{path/to/output_image.png}}`

- Scale an image keeping the original aspect ratio to a maximum dimension of 640x480:

`convert {{path/to/input_image.png}} -resize 640x480 {{path/to/output_image.png}}`

- Horizontally append images:

`convert {{path/to/image1.png path/to/image2.png ...}} +append {{path/to/output_image.png}}`

- Vertically append images:

`convert {{path/to/image1.png path/to/image2.png ...}} -append {{path/to/output_image.png}}`

- Create a GIF from a series of images with 100ms delay between them:

`convert {{path/to/image1.png path/to/image2.png ...}} -delay {{10}} {{path/to/animation.gif}}`

- Create an image with nothing but a solid red background:

`convert -size {{800x600}} "xc:{{#ff0000}}" {{path/to/image.png}}`

- Create a favicon from several images of different sizes:

`convert {{path/to/image1.png path/to/image2.png ...}} {{path/to/favicon.ico}}`
