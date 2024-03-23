# pamundice

> Combine a grid of Netpbm images into one.
> See also: `pamdice`.
> More information: <https://netpbm.sourceforge.net/doc/pamundice.html>.

- Combine the images whose names match the `printf`-style filename expression. Assume a grid with a specific size:

`pamundice {{filename_%1d_%1a.ppm}} -across {{grid_width}} -down {{grid_height}} > {{path/to/output.ppm}}`

- Assume that the tiles overlap horizontally and vertically by the specified amount:

`pamundice {{filename_%1d_%1a.ppm}} -across {{x_value}} -down {{y_value}} -hoverlap {{value}} -voverlap {{value}} > {{path/to/output.ppm}}`

- Specify the images to be combined through a text file containing one filename per line:

`pamundice -listfile {{path/to/file.txt}} -across {{x_value}} -down {{y_value}} > {{path/to/output.ppm}}`
