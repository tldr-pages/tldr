# sips

> Apple Scriptable Image Processing System.
> Raster/Query images and ColorSync ICC Profiles.
> More information: <https://keith.github.io/xcode-man-pages/sips.1.html>.

- Resize an image and save it to a separate file, preserving the original:

`sips --resampleWidth {{960}} {{path/to/image.png}} --out {{path/to/output.png}}`

- Resample an image to a specified height and width, possibly changing its aspect ratio:

`sips --resampleHeightWidth {{1920}} {{300}} {{path/to/image.ext}}`

- Resample an image so neither dimension exceeds the specified size, preserving its aspect ratio:

`sips --resampleHeightWidthMax {{1920}} {{path/to/image.ext}}`

- Resample all PNG images in a directory in-place to a width of 960 pixels, preserving their aspect ratios:

`sips --resampleWidth 960 {{path/to/directory}}/*.png`

- Convert an image from CMYK to RGB:

`sips --matchTo "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc" {{path/to/image.ext}} --out {{path/to/output_directory}}`

- Remove ColorSync ICC profile from an image:

`sips --deleteProperty profile --deleteColorManagementProperties {{path/to/image_file.ext}}`
