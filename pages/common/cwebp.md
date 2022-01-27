# cwebp

> Compress an image file to a WebP file
> More information: <https://developers.google.com/speed/webp/docs/cwebp>.

- Compress a WebP with default (quality = 75) settings:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}}`

- Compress a WebP with the best quality and largest file size:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{100}}`

- Compress a WebP with the worst quality and smallest file size:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -q {{0}}`

- Compress a WebP and apply resize to image:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -resize {{width}} {{height}}`

- Compress a WebP and drop alpha channel information:

`cwebp {{path/to/image_file}} -o {{path/to/output.webp}} -noalpha`
