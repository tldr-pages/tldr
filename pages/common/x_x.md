# x_x

> View Excel and CSV files from the command-line.
> More information: <https://github.com/kristianperkins/x_x>.

- View an XLSX or CSV file:

`x_x {{file.xlsx|file.csv}}`

- View an XLSX or CSV file, using the first row as table headers:

`x_x -h {{0}} {{file.xlsx|file.csv}}`

- View a CSV file with unconventional delimiters:

`x_x --delimiter={{';'}} --quotechar={{'|'}} {{file.csv}}`
