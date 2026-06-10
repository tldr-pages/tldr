# pnmtops

> Փոխարկել PNM պատկերը PostScript ֆայլի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmtops.html>:.

- Փոխարկել PNM պատկերը PS ֆայլի.:

`pnmtops {{path/to/file.pnm}} > {{path/to/file.ps}}`

- Նշեք ելքային պատկերի չափերը դյույմներով.:

`pnmtops {{[-imagew|-imagewidth]}} {{imagewidth}} {{[-imageh|-imageheight]}} {{imageheight}} {{path/to/file.pnm}} > {{path/to/file.ps}}`

- Նշեք էջի չափերը, որի վրա պատկերված է ելքային պատկերը դյույմներով.:

`pnmtops {{[-w|-width]}} {{width}} {{[-h|-height]}} {{height}} {{path/to/file.pnm}} > {{path/to/file.ps}}`
