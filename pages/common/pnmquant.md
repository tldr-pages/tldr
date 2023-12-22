# pnmquant

> Quantize the colors in a PNM image into a smaller set.
> This command is a combination of `pnmcolormap` and `pnmremap` and accepts the union of their options, except `-mapfile`.
> More information: <https://netpbm.sourceforge.net/doc/pnmquant.html>.

- Generate an image using only `n_colors` or less colors as close as possible to the input image:

`pnmquant {{n_colors}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
