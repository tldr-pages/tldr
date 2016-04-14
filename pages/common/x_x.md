# x_x

> View Excel and CSV files from the command-line.

- View an XLSX or CSV file:

`x_x {{file.ext}}`

- View an XLSX or CSV file, using the first row as table headers:

`x_x -h {{0}} {{file.ext}}`

- View a CSV file with unconventional delimiters:

`x_x --delimiter={{';'}} --quotechar={{'|'}} {{file.csv}}`
