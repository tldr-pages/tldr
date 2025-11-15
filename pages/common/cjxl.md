# cjxl

> Compress images to JPEG XL.
> Accepted input extensions are PNG, APNG, GIF, JPEG, EXR, PPM, PFM, PAM, PGX, and JXL.
> More information: <https://github.com/libjxl/libjxl>.

- Convert an image to JPEG XL:

`cjxl {{path/to/image.ext}} {{path/to/output.jxl}}`

- Set quality to lossless and maximize compression of the resulting image:

`cjxl --distance 0 --effort 9 {{path/to/image.ext}} {{path/to/output.jxl}}`

- Display an extremely detailed help page:

`cjxl {{[-h -v -v -v -v|--help --verbose --verbose --verbose --verbose]}}`
