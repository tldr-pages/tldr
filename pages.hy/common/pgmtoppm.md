# pgmtoppm

> Գունավորեք PGM պատկերը:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pgmtoppm.html>:.

- Մուտքային պատկերի բոլոր մոխրագույն արժեքները քարտեզագրեք նշված երկու գույների միջև եղած բոլոր գույներին.:

`pgmtoppm {{[-b|-black]}} {{red}} {{[-w|-white]}} {{blue}} {{path/to/input.pgm}} > {{path/to/output.ppm}}`

- Մուտքագրված պատկերի մոխրագույն մասշտաբի բոլոր արժեքները գունավորեք ըստ նշված գունային քարտեզի.:

`pgmtoppm {{[-m|-map]}} {{path/to/colormap.ppm}} {{path/to/input.pgm}} > {{path/to/output.ppm}}`
