# ppmtobmp

> Փոխարկել PPM պատկերը BMP ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmtobmp.html>:.

- Փոխարկել PPM պատկերը BMP ֆայլի.:

`ppmtobmp {{path/to/file.ppm}} > {{path/to/file.bmp}}`

- Հստակորեն նշեք, թե արդյոք Windows BMP ֆայլը կամ OS/2 BMP ֆայլը պետք է ստեղծվի, թե ոչ.:

`ppmtobmp -{{windows|os2}} {{path/to/file.ppm}} > {{path/to/file.bmp}}`

- Յուրաքանչյուր պիքսելի համար օգտագործեք բիթերի որոշակի քանակ.:

`ppmtobmp {{[-b|-bbp]}} {{1|4|8|24}} {{path/to/file.ppm}} > {{path/to/file.bmp}}`
