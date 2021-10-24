# dwebp

> `dwebp` decompresses WebP files into PNG, PAM, PPM or PGM images.
> Animated WebP files are not supported.
> More information: <https://developers.google.com/speed/webp/docs/dwebp/>.

- Convert a `webp` file into a `png` file:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}}`

- Convert a `webp` file into a specific filetype:

`dwebp {{path/to/input.webp}} -bmp|-tiff|-pam|-ppm|-pgm|-yuv -o {{path/to/output}}`

- Convert a `webp` file, using multi-threading if possible:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -mt`

- Convert a `webp` file, but also crop and scale at the same time:

`dwebp {{input.webp}} -o {{output.png}} -crop {{x_pos}} {{y_pos}} {{width}} {{height}} -scale {{width}} {{height}}`

- Convert a `webp` file and flip the output:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -flip`

- Convert a `webp` file and don't use in-loop filtering to speed up the decoding process:

`dwebp {{path/to/input.webp}} -o {{path/to/output.png}} -nofilter`
