# x_x

> Excel- és CSV-fájlok megtekintése a parancssorból. További információ: <https://github.com/kristianperkins/x_x>.

- XLSX vagy CSV fájl megtekintése:

`x_x {{file.xlsx|file.csv}}`

- XLSX- vagy CSV-fájl megtekintése, az első sort táblázatfejlécként használva:

`x_x -h {{0}} {{file.xlsx|file.csv}}`

- CSV-fájl megtekintése nem szokványos elválasztójelekkel:

`x_x --delimiter={{';'}} --quotechar={{'|'}} {{file.csv}}`
