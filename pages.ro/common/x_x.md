# x_x

> Vizualizați fișiere Excel și CSV din linia de comandă.
> Mai multe informaţii: <https://github.com/kristianperkins/x_x>

- Vizualizaţi un fişier XLSX sau CSV:

`x_x {{file.xlsx|file.csv}}`

- Vizualizaţi un fişier XLSX sau CSV, utilizând primul rând ca anteturi de tabel:

`x_x -h {{0}} {{file.xlsx|file.csv}}`

- Vizualizaţi un fişier CSV cu delimitatori neconvenţionali:

`x_x --delimiter={{';'}} --quotechar={{'|'}} {{file.csv}}`
