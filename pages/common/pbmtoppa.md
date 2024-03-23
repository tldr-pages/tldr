# pbmtoppa

> Convert a PBM image to HP Printer Performance Architecture format.
> More information: <https://netpbm.sourceforge.net/doc/pbmtoppa.html>.

- Convert a PBM image into a PPA file:

`pbmtoppa {{path/to/image.pbm}} > {{path/to/output.ppa}}`

- Specify the desired dots-per-inch and paper size:

`pbmtoppa -d {{300}} -s {{a4}} {{path/to/image.pbm}} > {{path/to/output.ppa}}`
