# pnmtotiffcmyk

> Փոխակերպեք PNM պատկերը CMYK կոդավորված TIFF-ի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmtotiffcmyk.html>:.

- Փոխակերպեք PNM պատկերը CMYK կոդավորված TIFF-ի.:

`pnmtotiffcmyk {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`

- Նշեք TIFF սեղմման մեթոդը.:

`pnmtotiffcmyk -{{none|packbits|lzw}} {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`

- Վերահսկեք լրացման կարգը.:

`pnmtotiffcmyk -{{msb2lsb|lsb2msb}} {{path/to/input_file.pnm}} > {{path/to/output_file.tiff}}`
