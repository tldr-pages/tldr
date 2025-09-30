# pnmremap

> Replace the colors in a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmremap.html>.

- Replace the colors in an image with those in the specified color palette:

`pnmremap {{[-ma|-mapfile]}} {{path/to/palette_file.ppm}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Use Floyd-Steinberg dithering for representing colors missing in the color palette:

`pnmremap {{[-ma|-mapfile]}} {{path/to/palette_file.ppm}} {{[-fs|-floyd]}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Use the first color in the palette for representing colors missing in the color palette:

`pnmremap {{[-ma|-mapfile]}} {{path/to/palette_file.ppm}} {{[-fi|-firstisdefault]}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Use the specified color for representing colors missing in the color palette:

`pnmremap {{[-ma|-mapfile]}} {{path/to/palette_file.ppm}} {{[-m|-missingcolor]}} {{color}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
