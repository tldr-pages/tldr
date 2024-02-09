# pbmtopgm

> Convert PBM image to PGM by averaging areas surounding individual pixels.
> See also: `pnmconvol`, `pamditherbw`.
> More information: <https://netpbm.sourceforge.net/doc/pbmtopgm.html>.

- Convert PBM image to PGM by averaging the `w`x`h`-sized area surrounding each pixel:

`pbmtopgm {{w}} {{h}} {{path/to/image.pbm}} > {{path/to/output.pgm}}`
