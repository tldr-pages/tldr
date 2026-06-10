# tifftopnm

> Փոխակերպեք TIFF պատկերը PNM պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/tifftopnm.html>:.

- Փոխակերպեք TIFF-ը PNM ֆայլի.:

`tifftopnm {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`

- Ստեղծեք PGM ֆայլ, որը պարունակում է մուտքային պատկերի ալֆա ալիքը.:

`tifftopnm {{[-a|-alphaout]}} {{path/to/alpha_file.pgm}} {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`

- Հարգեք `fillorder` պիտակը մուտքագրված TIFF պատկերում.:

`tifftopnm {{[-r|-respectfillorder]}} {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`

- Տպել TIFF վերնագրի տեղեկությունները `stderr`-ում:

`tifftopnm {{[-h|-headerdump]}} {{path/to/input_file.tiff}} > {{path/to/output_file.pnm}}`
