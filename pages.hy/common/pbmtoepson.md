# pbmtoepson

> Փոխարկեք PBM պատկերը Epson տպիչի գրաֆիկայի:.
> Տես նաև՝ `pbmtoescp2`:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmtoepson.html>:.

- Փոխարկել PBM պատկերը Epson տպիչի գրաֆիկայի.:

`pbmtoepson {{path/to/image.pbm}} > {{path/to/output.epson}}`

- Նշեք ելքի տպիչի արձանագրությունը.:

`pbmtoepson {{[-pr|-protocol]}} {{escp9|escp}} {{path/to/image.pbm}} > {{path/to/output.epson}}`

- Նշեք ելքի հորիզոնական DPI-ն.:

`pbmtoepson {{[-d|-dpi]}} {{60|72|80|90|120|144|240}} {{path/to/image.pbm}} > {{path/to/output.epson}}`
