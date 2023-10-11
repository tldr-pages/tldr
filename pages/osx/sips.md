# sips

> Apple Scriptable Image Processing System.
> Raster/Query images and ColorSync ICC Profiles.
> More information: <https://ss64.com/osx/sips.html>.

- Specify an output directory so that originals do not get modified:

`sips --out {{path/to/out_dir}}`

- Resample image at specified size, Image aspect ratio may be altered:

`sips --resampleHeightWidth {{1920}} {{300}} {{image_file.ext}}`

- Resample image so height and width aren't greater than specified size (notice the capital Z):

`sips --resampleHeightWidthMax {{1920}} {{300}} {{image_file.ext}}`

- Resample all images in a directory to fit a width of 960px (honoring aspect ratio):

`sips --resampleWidth {{960}} {{path/to/images}}`

- Convert an image from CMYK to RGB:

`sips --matchTo "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc" {{path/to/image.ext}} {{path/to/out_dir}}`

- Remove ColorSync ICC profile from an image:

`sips --deleteProperty profile --deleteColorManagementProperties {{path/to/image_file.ext}}`
