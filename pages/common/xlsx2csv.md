# xlsx2csv

> Convert Excel (XLSX) files to CSV format.
> More information: <https://github.com/dilshod/xlsx2csv>.

- Convert a specific XLSX file to CSV:

`xlsx2csv path/to/input.xlsx path/to/output.csv`

- Convert a specific sheet by index (starting from 1):

`xlsx2csv -i 1 path/to/input.xlsx path/to/output.csv`

- Convert a specific sheet by name:

`xlsx2csv -n SheetName path/to/input.xlsx path/to/output.csv`

- Convert an entire workbook to a directory of CSV files:

`xlsx2csv -a path/to/input.xlsx path/to/output_directory`

- Specify the delimiter for the output CSV:

`xlsx2csv -d ',' path/to/input.xlsx path/to/output.csv`
