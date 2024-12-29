# ppmwheel

> Generate a PPM image of a color wheel.
> More information: <https://netpbm.sourceforge.net/doc/ppmwheel.html>.

- Generate a color wheel of type `Ppmcirc`:

`ppmwheel {{diameter}} > {{path/to/output.ppm}}`

- Generate a color wheel of type `Hue-value`:

`ppmwheel -huevalue {{diameter}} > {{path/to/output.ppm}}`

- Generate a color wheel of type `Hue-saturation`:

`ppmwheel -huesaturation {{diameter}} > {{path/to/output.ppm}}`
