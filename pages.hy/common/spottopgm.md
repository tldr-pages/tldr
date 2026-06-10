# spottopgm

> Փոխարկեք SPOT արբանյակային պատկերը PGM ձևաչափի:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/spottopgm.html>:.

- Նշված SPOT պատկերը փոխարկեք PGM ձևաչափի.:

`spottopgm {{path/to/file.spot}} > {{path/to/output.pgm}}`

- Հանեք նշված գունային ալիքը.:

`spottopgm -{{1|2|3}} {{path/to/file.spot}} > {{path/to/output.pgm}}`

- Մուտքային պատկերից հանեք նշված ուղղանկյունը.:

`spottopgm {{first_col first_row last_col last_row}} {{path/to/file.spot}} > {{path/to/output.pgm}}`
