# rletopnm

> Utah Raster Tools RLE պատկերի ֆայլը փոխարկեք PNM ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/rletopnm.html>:.

- Փոխակերպեք RLE պատկերը PNM ֆայլի.:

`rletopnm {{path/to/input.rle}} > {{path/to/output.pnm}}`

- Ստեղծեք PGM պատկեր, որը պարունակում է RLE ֆայլի ալֆա ալիքը.:

`rletopnm {{[--a|--alphaout]}} {{path/to/alpha_file.pgm}} {{path/to/input.rle}} > {{path/to/output.pnm}}`

- Գործեք բառացի ռեժիմով և տպեք RLE վերնագրի բովանդակությունը `stdout`-ում.:

`rletopnm {{[--verb|--verbose]}} {{path/to/input.rle}} > {{path/to/output.pnm}}`
