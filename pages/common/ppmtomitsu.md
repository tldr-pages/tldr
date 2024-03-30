# ppmtomitsu

> Convert a PPM image to a Mitsubishi S340-10 file.
> More information: <https://netpbm.sourceforge.net/doc/ppmtomitsu.html>.

- Convert a PPM image to a MITSU file:

`ppmtomitsu {{path/to/file.ppm}} > {{path/to/file.mitsu}}`

- Enlarge the image by the specified factor, use the specified sharpness and produce `n` copies:

`ppmtomitsu -enlarge {{1|2|3}} -sharpness {{1|2|3|4}} -copy {{n}} {{path/to/file.ppm}} > {{path/to/file.mitsu}}`

- Use the given medium for the printing process:

`ppmtomitsu -media {{A|A4|AS|A4S}} {{path/to/file.ppm}} > {{path/to/file.mitsu}}`
