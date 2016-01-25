# convert

> Imagemagick image conversion tool.

- Convert an image from JPG to PNG:

`convert {{image.jpg}} {{image.png}}`

- Scale an image 50% it's original size:

`convert {{image.png}} -resize 50% {{image2.png}}`

- Scale an image keeping the original aspect ratio to a maximum dimension of 640x480:

`convert {{image.png}} -resize 640x480 {{image2.png}}`

- Horizontally append images:

`convert {{image1.png}} {{image2.png}} {{image3.png}} +append {{image123.png}}`
