# in2csv

> Converts various tabular data formats into CSV.
> Included in csvkit.

- Convert an XLS file to CSV:

`in2csv {{data.xls}}`

- Convert a DBF file to a CSV file:

`in2csv {{data.dbf}} > {{data.csv}}`

- Convert a specific sheet from an XLSX file to CSV:

`in2csv --sheet={{sheet_name}} {{data.xlsx}}`

- Fetch csvkit's open issues from GitHub's JSON API, and convert them to CSV:

`curl https://api.github.com/repos/onyxfish/csvkit/issues?state=open | in2csv -f json > issues.csv`
