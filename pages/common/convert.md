# convert

> ImageMagick image conversion tool.
> More information: <https://imagemagick.org/script/convert.php>.

- Convert an image from JPG to PNG:

`convert {{image.jpg}} {{image.png}}`

- Scale an image 50% its original size:

`convert {{image.png}} -resize 50% {{image2.png}}`

- Scale an image keeping the original aspect ratio to a maximum dimension of 640x480:

`convert {{image.png}} -resize 640x480 {{image2.png}}`

- Horizontally append images:

`convert {{image1.png}} {{image2.png}} {{image3.png}} +append {{image123.png}}`

- Vertically append images:

`convert {{image1.png}} {{image2.png}} {{image3.png}} -append {{image123.png}}`

- Create a GIF from a series of images with 100ms delay between them:

`convert {{image1.png}} {{image2.png}} {{image3.png}} -delay {{10}} {{animation.gif}}`

- Create an image with nothing but a solid background:

`convert -size {{800x600}} "xc:{{#ff0000}}" {{image.png}}`

- Create a favicon from several images of different sizes:

`convert {{image1.png}} {{image2.png}} {{image3.png}} {{image.ico}}`
