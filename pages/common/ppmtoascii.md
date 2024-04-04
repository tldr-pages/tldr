# ppmtoascii

> Convert a PPM image to an ASCII image using ANSI terminal color codes.
> See also: `ppmtoterm`, `pbmtoascii`, `pbmto4425`.
> More information: <https://netpbm.sourceforge.net/doc/ppmtoascii.html>.

- Convert a PPM image to an ASCII image, combining an area of 1x2 pixels into a character:

`ppmtoascii {{path/to/input.ppm}} > {{path/to/output.txt}}`

- Convert a PPM image to an ASCII image, combining an area of 2x4 pixels into a character:

`ppmtoascii -2x4 {{path/to/input.ppm}} > {{path/to/output.txt}}`
