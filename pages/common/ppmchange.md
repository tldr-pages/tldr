# ppmchange

> Change all pixels of one color in a PPM image to another color.
> More information: <https://netpbm.sourceforge.net/doc/ppmchange.html>.

- Exchange the first color in each `oldcolor` - `newcolor` pair with the second color:

`ppmchange {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`

- Specify how similar colors must be in order to be considered the same:

`ppmchange -closeness {{percentage}} {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`

- Replace all pixels not specified in the arguments by a color:

`ppmchange -remainder {{color}} {{oldcolor1 newcolor1 oldcolor2 newcolor2 ...}} {{path/to/input.ppm}} > {{path/to/output.ppm}}`
