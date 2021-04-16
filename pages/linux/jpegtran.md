# jpegtran

> Perform lossless transformation of JPEG files.
> More information: <https://manned.org/jpegtran>.

- Mirror an image horizontally or vertically:

`jpegtran -flip {{horizontal|vertical}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Rotate an image 90, 180 or 270 degrees clockwise:

`jpegtran -rotate {{90|180|270}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Transpose the image across the upper left to lower right axis:

`jpegtran -transpose {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Transverse the image across the upper right to lower left axis:

`jpegtran -transverse {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Convert the image to grayscale:

`jpegtran -grayscale {{path/to/image.jpg}} > {{path/to/output.jpg}}`

- Crop the image to a rectangular region of width `W` and height `H` from the upper left corner, saving the output to a specific file:

`jpegtran -crop {{W}}x{{H}} -outfile {{path/to/output.jpg}} {{path/to/image.jpg}}`

- Crop the image to a rectangular region of width `W` and height `H`, starting at point `X` and `Y` from the upper left corner:

`jpegtran -crop {{W}}x{{H}}+{{X}}+{{Y}} {{path/to/image.jpg}} > {{path/to/output.jpg}}`
