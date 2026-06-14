# pbmtoepsi

> Փոխարկեք PBM պատկերը փակցված PostScript ոճի նախադիտման բիթքարտեզի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmtoepsi.html>:.

- Փոխակերպեք PBM պատկերը փակցված PostScript ոճի նախադիտման բիթքարտեզի.:

`pbmtoepsi {{path/to/image.pbm}} > {{path/to/output.bmp}}`

- Ստեղծեք քառակուսի ելքային պատկեր նշված լուծաչափով.:

`pbmtoepsi {{[-d|-dpi]}} {{144}} {{path/to/image.pbm}} > {{path/to/output.bmp}}`

- Ստեղծեք ելքային պատկեր նշված հորիզոնական և ուղղահայաց լուծաչափով.:

`pbmtoepsi {{[-d|-dpi]}} {{72x144}} {{path/to/image.pbm}} > {{path/to/output.bmp}}`

- Ստեղծեք միայն սահմանային տուփ.:

`pbmtoepsi {{[-b|-bbonly]}} {{path/to/image.pbm}} > {{path/to/output.bmp}}`
