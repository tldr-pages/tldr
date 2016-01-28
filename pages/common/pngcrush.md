# pngcrush

> PNG image compression utility.

- Compress a PNG file:

`pngcrush {{in.png}} {{out.png}}`

- Compress all PNGs and output to directory:

`pngcrush -d {{path/to/output}} *.png`

- Compress PNG file with best compression:

`pngcrush -rem allb -brute -reduce {{in.png}} {{out.png}}`
