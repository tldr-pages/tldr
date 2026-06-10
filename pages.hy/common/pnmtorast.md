# pnmtorast

> Փոխարկել PNM ֆայլը Sun rasterfile-ի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pnmtorast.html>:.

- Փոխակերպեք PNM պատկերը RAST պատկերի.:

`pnmtorast {{path/to/input.pnm}} > {{path/to/output.rast}}`

- Արդյունքի համար հարկադրել `RT_STANDARD` կամ `RT_BYTE_ENCODED` ձևը.:

`pnmtorast -{{standard|rle}} {{path/to/input.pnm}} > {{path/to/output.rast}}`
