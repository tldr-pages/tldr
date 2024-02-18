# fitstopnm

> Convert a Flexible Image Transport System (FITS) file into a PNM image.
> See also: `pamtofits`.
> More information: <https://netpbm.sourceforge.net/doc/fitstopnm.html>.

- Convert a FITS file into a PNM image:

`fitstopnm {{path/to/file.fits}} > {{path/to/output.pnm}}`

- Convert the image on the specified position of the third axis in the FITS file:

`fitstopnm -image {{n}} {{path/to/file.fits}} > {{path/to/output.pnm}}`
