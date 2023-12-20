# pnmcolormap

> Create quantization color map for a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmcolormap.html>.

- Generate an image using only `n_colors` or less colors as close as possible to the input image:

`pnmcolormap {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Use the splitspread strategy for determining the output colors, possibly producing a better result for images with small details:

`pnmcolormap -splitspread {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.ppm}}`

- Sort the resulting colormap, which is useful for comparing colormaps:

`pnmcolormap -sort {{path/to/input.pnm}} > {{path/to/output.ppm}}`
