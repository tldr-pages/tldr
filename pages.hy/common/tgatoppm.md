# tgatoppm

> Փոխակերպեք TrueVision Targa ֆայլը Netpbm պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/tgatoppm.html>:.

- Փոխակերպեք TrueVision Targa ֆայլը PPM պատկերի.:

`tgatoppm {{path/to/file.tga}} > {{path/to/output.ppm}}`

- Թափել տեղեկատվությունը TGA վերնագրից `stdout`:

`tgatoppm {{[-h|-headerdump]}} {{path/to/file.tga}} > {{path/to/output.ppm}}`

- Նշված ֆայլում գրեք մուտքային պատկերի թափանցիկության ալիքի արժեքները.:

`tgatoppm {{[-a|-alphaout]}} {{path/to/transparency_file.pgm}} {{path/to/file.tga}} > {{path/to/output.ppm}}`

- Ցուցադրման տարբերակը:

`tgatoppm {{[-v|-version]}}`
