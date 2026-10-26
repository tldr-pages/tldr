# x_x

> View Excel and CSV files.
> More information: <https://github.com/kristianperkins/x_x>.

- View an XLSX or CSV file:

`x_x {{file}}.{{xlsx|csv}}`

- View an XLSX or CSV file, using the first row as table headers:

`x_x {{[-h|--heading]}} {{0}} {{file}}.{{xlsx|csv}}`

- View a CSV file with unconventional delimiters:

`x_x {{[-d|--delimiter]}} '{{;}}' {{[-q|--quotechar]}} '{{|}}' {{file.csv}}`
