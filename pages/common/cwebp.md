# cwebp

> Compress an image file to a WebP file.
> More information: <https://developers.google.com/speed/webp/docs/cwebp>.

- Compress a WebP file with default settings (lossy compression, q = 75) to the [o]utput file:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}}`

- Compress a WebP file with the best lossy compression [q]uality and largest file size:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{100}}`

- Compress a WebP file with the worst lossy compression [q]uality and smallest file size:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{0}}`

- Compress a WebP file with lossless compression and smallest possible file size:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -z 9`

- Compress a WebP file and apply resize to image (if width or height are 0, scaling preserves aspect ratio):

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -resize {{width}} {{height}}`

- Compress a WebP file and drop alpha channel information:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -noalpha`
