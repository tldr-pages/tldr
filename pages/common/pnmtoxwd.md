# pnmtoxwd

> Convert a PNM file into an X11 window dump file.
> More information: <https://netpbm.sourceforge.net/doc/pnmtoxwd.html>.

- Convert a PNM image file to XWD:

`pnmtoxwd {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`

- Produce the output in the DirectColor format:

`pnmtoxwd -directcolor {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`

- Set the color depth of the output to b bits:

`pnmtoxwd -pseudodepth {{b}} {{path/to/input_file.pnm}} > {{path/to/output_file.xwd}}`
