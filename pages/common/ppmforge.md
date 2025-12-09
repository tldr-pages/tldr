# ppmforge

> Generate fractals resembling clouds, planets and starry skies.
> More information: <https://netpbm.sourceforge.net/doc/ppmforge.html>.

- Generate an image of a planet:

`ppmforge > {{path/to/image.ppm}}`

- Generate an image of clouds or the night sky:

`ppmforge -{{night|clouds}} > {{path/to/image.ppm}}`

- Use a custom mesh size and dimension for fractal generation and specify the dimensions of the output:

`ppmforge {{[-m|-mesh]}} {{512}} {{[-d|-dimension]}} {{2.5}} {{[-x|-xsize]}} {{1000}} {{[-y|-ysize]}} {{1000}} > {{path/to/image.ppm}}`

- Control the tilt and the angle from which the generated planet is illuminated:

`ppmforge {{[-t|-tilt]}} {{-15}} {{[-ho|-hour]}} {{12}} > {{path/to/image.ppm}}`
