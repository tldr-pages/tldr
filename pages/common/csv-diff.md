# csv-diff

> View differences between two CSV, TSV or JSON files.
> More information: <https://github.com/simonw/csv-diff>.

- Show a human-readable summary of differences between files using a specific column as an unique identifier:

`csv-diff {{one.csv}} {{two.csv}} --key={{column_name}}`

- Show a human-readable summary of differences between files that includes unchanges values in rows that have at least one change:

`csv-diff {{one.csv}} {{two.csv}} --key={{column_name}} --show-unchanged`

- Show a summary of differences between files in JSON format using a specific column as an unique identifier:

`csv-diff {{one.csv}} {{two.csv}} --key={{column_name}} --json`
