# pbmtoescp2

> Convert a PBM image to a ESC/P2 printer file.
> See also: `pbmtoepson`, `escp2topbm`.
> More information: <https://netpbm.sourceforge.net/doc/pbmtoescp2.html>.

- Convert a PBM image to a ESC/P2 printer file:

`pbmtoescp2 {{path/to/image.pbm}} > {{path/to/output.escp2}}`

- Specify the compression of the output:

`pbmtoescp2 -compression {{0|1}} {{path/to/image.pbm}} > {{path/to/output.escp2}}`

- Specify the horizontal and vertical resolution of the output in dots per inch:

`pbmtoescp2 -resolution {{180|360|720}} {{path/to/image.pbm}} > {{path/to/output.escp2}}`

- Place a formfeed command at the end of the output:

`pbmtoescp2 -formfeed {{path/to/image.pbm}} > {{path/to/output.escp2}}`
