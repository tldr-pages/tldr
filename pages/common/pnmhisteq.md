# pnmhisteq

> Histogram-equalize a PNM image.
> More information: <https://netpbm.sourceforge.net/doc/pnmhisteq.html>.

- Increase the contrast of a PNM image using histogram equalization:

`pnmhisteq {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Only modify grey pixels:

`pnmhisteq -grey {{path/to/input.pnm}} > {{path/to/output.pnm}}`

- Do not include black or white pixels in the histogram equalization:

`pnmhisteq -no{{black|white}} {{path/to/input.pnm}} > {{path/to/output.pnm}}`
