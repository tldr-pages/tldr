# pcxtoppm

> Փոխակերպեք PCX ֆայլը PPM պատկերի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pcxtoppm.html>:.

- Փոխակերպեք PCX ֆայլը PPM պատկերի.:

`pcxtoppm {{path/to/file.pcx}} > {{path/to/file.ppm}}`

- Օգտագործեք նախապես սահմանված ստանդարտ գունապնակ, նույնիսկ եթե PCX ֆայլը տալիս է մեկը.:

`pcxtoppm {{[-s|-stdpalette]}} {{path/to/file.pcx}} > {{path/to/file.ppm}}`

- Տպեք տեղեկատվությունը PCX վերնագրի վրա `stdout`-ում:

`pcxtoppm {{[-verb|-verbose]}} {{path/to/file.pcx}} > {{path/to/file.ppm}}`
