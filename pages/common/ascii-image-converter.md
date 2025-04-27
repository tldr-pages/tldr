# ascii-image-converter

> Convert an image into ASCII.
> More information: <https://github.com/TheZoraiz/ascii-image-converter#cli-usage>.

- Convert an image into ASCII:

`ascii-image-converter {{path/to/image|URL}}`

- Colorize the output:

`ascii-image-converter {{[-C|--color]}} {{path/to/image|URL}}`

- Create a tresholded image using braille:

`ascii-image-converter {{[-b|--braille]}} {{path/to/image|URL}}`

- Display the image with negative colors:

`ascii-image-converter {{[-Cn|--color --negative]}} {{path/to/image|URL}}`

- Use a wider range of characters to display an image (may improve image accuracy):

`ascii-image-converter {{[-c|--complex]}} {{path/to/image|URL}}`
