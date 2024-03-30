# pnmremap

> Replace the colors in a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmremap.html>.

- Replace the colors in an image with those in the specified color palette:

`pnmremap -mapfile {{path/to/palette_file.ppm}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Use Floyd-Steinberg dithering for representing colors missing in the color palette:

`pnmremap -mapfile {{path/to/palette_file.ppm}} -floyd {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Use the first color in the palette for representing colors missing in the color palette:

`pnmremap -mapfile {{path/to/palette_file.ppm}} -firstisdefault {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Use the specified color for representing colors missing in the color palette:

`pnmremap -mapfile {{path/to/palette_file.ppm}} -missingcolor {{color}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
