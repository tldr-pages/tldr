# rasttopnm

> Convert a Sun rasterfile to a PNM file.
> More information: <https://netpbm.sourceforge.net/doc/rasttopnm.html>.

- Convert a RAST image to a PNM file:

`rasttopnm {{path/to/input.rast}} > {{path/to/output.pnm}}`

- Use the color map indices in the raster if they are color values:

`rasttopnm -index {{path/to/input.rast}} > {{path/to/output.pnm}}`
