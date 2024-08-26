# cjxl

> Compress images to JPEG XL.
> More information: <https://github.com/libjxl/libjxl>.

- Convert an image to JPEG XL:

`cjxl {{path/to/image}} {{path/to/output.jxl}} `

- Maximize the quality and compression of the resulting image:

`cjxl --distance 0 --effort 9 {{path/to/image}} {{path/to/target.jxl}}`
