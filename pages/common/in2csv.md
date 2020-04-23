# in2csv

> Converts various tabular data formats into CSV.
> Included in csvkit.
> More information: <https://csvkit.readthedocs.io/en/latest/scripts/in2csv.html>.

- Convert an XLS file to CSV:

`in2csv {{data.xls}}`

- Convert a DBF file to a CSV file:

`in2csv {{data.dbf}} > {{data.csv}}`

- Convert a specific sheet from an XLSX file to CSV:

`in2csv --sheet={{sheet_name}} {{data.xlsx}}`

- Pipe a JSON file to in2csv:

`cat {{data.json}} | in2csv -f json > {{data.csv}}`
