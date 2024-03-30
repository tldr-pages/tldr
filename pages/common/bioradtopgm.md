# bioradtopgm

> Convert a Biorad confocal file into a PGM file.
> More information: <https://netpbm.sourceforge.net/doc/bioradtopgm.html>.

- Read a Biorad confocal file and store the n'th image contained in it to as a PGM file:

`bioradtopgm -{{n}} {{path/to/file.pic}} > {{path/to/file.pgm}}`

- Read a Biorad confocal file and print the number of images it contains:

`bioradtopgm {{path/to/file.pic}}`

- Display version:

`bioradtopgm -version`
