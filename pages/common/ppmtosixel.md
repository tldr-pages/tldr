# ppmtosixel

> Convert a PPM image to DEC sixel format.
> More information: <https://netpbm.sourceforge.net/doc/ppmtosixel.html>.

- Convert a PPM image to DEC sixel format:

`ppmtosixel {{path/to/file.ppm}} > {{path/to/file.sixel}}`

- Produce an uncompressed SIXEL file that is much slower to print:

`ppmtosixel -raw {{path/to/file.ppm}} > {{path/to/file.sixel}}`

- Add a left margin of 1.5 inches:

`ppmtosixel -margin {{path/to/file.ppm}} > {{path/to/file.sixel}}`

- Encode control codes in a more portable (although less space-efficient) way:

`ppmtosixel -7bit {{path/to/file.ppm}} > {{path/to/file.sixel}}`
