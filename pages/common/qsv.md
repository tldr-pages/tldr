# qsv

> CSV toolkit. Successor to the archived `xsv`.
> This page focuses on `qsv`-specific features. `qsvlite` covers more basic commands.
> More information: <https://github.com/dathere/qsv>.

- Convert Excel file sheet to CSV:

`qsv excel --sheet {{Sheet1}} {{path/to/file.xlsx}}`

- Page through CSV interactively:

`qsv lens {{path/to/file.csv}}`

- Uppercase every value in a column:

`qsv apply operations {{upper}} {{column}} {{path/to/file.csv}}`

- Trim then lowercase every value in a column:

`qsv apply operations {{trim,lower}} {{column}} {{path/to/file.csv}}`

- Sample 10 rows at random, then preview the shell command that would run for each row:

`qsv sample {{10}} {{path/to/file.csv}} | qsv foreach {{column}} '{{echo "Hello, {}!"}}'`

- Actually run it:

`qsv foreach {{column}} '{{echo "Hello, {}!"}}' --dry-run false`

- Fetch some JSON and append it to a new column:

`qsv fetch --url-template "{{https://api.zippopotam.us/us/90210}}" --new-column {{beverly_hills_json}} {{path/to/file.csv}}`
