# ppmdither

> Reduce the number of colors in an image by applying dithering.
> More information: <https://netpbm.sourceforge.net/doc/ppmdither.html>.

- Read a PPM image, apply dithering and save it to a file:

`ppmdither {{path/to/image.ppm}} > {{path/to/file.ppm}}`

- Specify the desired number of shades for each primary color:

`ppmdither -red {{2}} -green {{3}} -blue {{2}} {{path/to/image.ppm}} > {{path/to/file.ppm}}`

- Specify the dimensions of the dithering matrix:

`ppmdither -dim {{2}} {{path/to/image.ppm}} > {{path/to/file.ppm}}`
