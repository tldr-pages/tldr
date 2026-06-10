# ppmtosixel

> Փոխարկել PPM պատկերը DEC sixel ձևաչափի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/ppmtosixel.html>:.

- Փոխակերպեք PPM պատկերը DEC sixel ձևաչափի.:

`ppmtosixel {{path/to/file.ppm}} > {{path/to/file.sixel}}`

- Ստեղծեք չսեղմված SIXEL ֆայլ, որը շատ ավելի դանդաղ է տպվում.:

`ppmtosixel {{[-r|-raw]}} {{path/to/file.ppm}} > {{path/to/file.sixel}}`

- Ավելացնել ձախ լուսանցք 1,5 դյույմ.:

`ppmtosixel {{[-m|-margin]}} {{path/to/file.ppm}} > {{path/to/file.sixel}}`

- Կոդավորեք կառավարման կոդերը ավելի շարժական (թեև ավելի քիչ տարածություն է պահանջում) եղանակով.:

`ppmtosixel -7bit {{path/to/file.ppm}} > {{path/to/file.sixel}}`
