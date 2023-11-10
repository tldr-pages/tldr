# ppmforge

> Generate fractals resembling clouds, planets and starry skies.
> More information: <https://netpbm.sourceforge.net/doc/ppmforge.html>.

- Generate an image of a planet:

`ppmforge > {{path/to/image.ppm}}`

- Generate an image of clouds or the night sky:

`ppmforge -{{night|clouds}} > {{path/to/image.ppm}}`

- Use a custom mesh size and dimension for fractal generation and specify the dimensions of the output:

`ppmforge -mesh {{512}} -dimension {{2.5}} -xsize {{1000}} -ysize {{1000}} > {{path/to/image.ppm}}`

- Control the tilt and the angle from which the generated planet is illuminated:

`ppmforge -tilt {{-15}} -hour {{12}} > {{path/to/image.ppm}}`
