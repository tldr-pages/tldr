# pnmnorm

> Normalize the contrast in a PNM image.
> See also: `pnmhisteq`.
> More information: <https://netpbm.sourceforge.net/doc/pnmnorm.html>.

- Force the brightest pixels to be white, the darkest pixels to be black and spread out the ones in between linearly:

`pnmnorm {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Force the brightest pixels to be white, the darkest pixels to be black and spread out the ones in between quadratically such that pixels with a brightness of `n` become 50 % bright:

`pnmnorm -midvalue {{n}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Keep the pixels' hue, only modify the brightness:

`pnmnorm -keephues {{path/to/image.pnm}} > {{path/to/output.pnm}}`

- Specify a method to calculate a pixel's brightness:

`pnmnorm -{{luminosity|colorvalue|saturation}} {{path/to/image.pnm}} > {{path/to/output.pnm}}`
