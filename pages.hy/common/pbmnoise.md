# pbm աղմուկ

> Ստեղծեք սպիտակ աղմուկ:.
> Լրացուցիչ տեղեկություններ. <https://netpbm.sourceforge.net/doc/pbmnoise.html>:.

- Ստեղծեք PGM պատկեր, որը պարունակում է սպիտակ աղմուկ.:

`pbmnoise {{width}} {{height}} > {{path/to/output.pbm}}`

- Նշեք կեղծ պատահական թվերի գեներատորի սերմը.:

`pbmnoise {{width}} {{height}} -randomseed {{value}} > {{path/to/output.pbm}}`

- Նշեք սպիտակից սև պիքսելների ցանկալի փոխարժեքը.:

`pbmnoise {{width}} {{height}} -ratio {{1/3}} > {{path/to/output.pbm}}`
