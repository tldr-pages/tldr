# pbmtoepson

> Convert a PBM image to an Epson printer graphic.
> See also: `pbmtoescp2`.
> More information: <https://netpbm.sourceforge.net/doc/pbmtoepson.html>.

- Convert a PBM image to an Epson printer graphic:

`pbmtoepson {{path/to/image.pbm}} > {{path/to/output.epson}}`

- Specify the printer protocol of the output:

`pbmtoepson -protocol {{escp9|escp}} {{path/to/image.pbm}} > {{path/to/output.epson}}`

- Specify the horizontal DPI of the output:

`pbmtoepson -dpi {{60|72|80|90|120|144|240}} {{path/to/image.pbm}} > {{path/to/output.epson}}`
