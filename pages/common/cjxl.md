# cjxl

> Convert and compress images to JPEG XL.
> Accepted input extensions are PNG, APNG, GIF, JPEG, EXR, PPM, PFM, PAM, PGX, and JXL.
> More information: <https://github.com/libjxl/libjxl/blob/main/doc/man/cjxl.txt>.

- Convert an image to JPEG XL:

`cjxl {{path/to/image.ext}} {{path/to/output.jxl}}`

- Convert with a specific effort level ('1' - fastest but worst results, '10' - slowest but best results, '7' - default):

`cjxl {{[-e|--effort]}} {{1..10}} {{path/to/image.ext}} {{path/to/output.jxl}}`

- Convert with a specific quality:

`cjxl {{[-q|--quality]}} {{0..100}} {{path/to/image.ext}} {{path/to/output.jxl}}`

- Convert a JPEG to a JPEG XL with specific lossy quality:

`cjxl {{[-q|--quality]}} {{0..100}} --lossless_jpeg {{0}} {{path/to/image.jpeg}} {{path/to/output.jxl}}`

- Display an extremely detailed help:

`cjxl {{[-h -v -v -v -v|--help --verbose --verbose --verbose --verbose]}}`
