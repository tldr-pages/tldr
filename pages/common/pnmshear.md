# pnmshear

> Shear a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmshear.html>.

- Shear a PNM image by the specified angle:

`pnmshear {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Specify the color of the background in the sheared image:

`pnmshear -background {{blue}} {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Do not perform anti-aliasing:

`pnmshear -noantialias {{angle}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
