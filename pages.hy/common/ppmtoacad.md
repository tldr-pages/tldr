# ppmtoacad

> Փոխարկել PPM պատկերը AutoCAD տվյալների բազայի կամ սլայդի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmtoacad.html>:.

- Փոխակերպեք PPM պատկերը AutoCAD սլայդի.:

`ppmtoacad {{path/to/file.ppm}} > {{path/to/file.acad}}`

- Փոխակերպեք PPM պատկերը AutoCAD տվյալների բազայի երկուական ներմուծման ֆայլի.:

`ppmtoacad {{[-d|-dxb]}} {{path/to/file.ppm}} > {{path/to/file.dxb}}`

- Սահմանափակեք ելքի գույները 8 RGB երանգներով.:

`ppmtoacad -8 {{path/to/file.ppm}} > {{path/to/file.dxb}}`
