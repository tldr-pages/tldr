# csv-diff

> View differences between two CSV, TSV or JSON files.
> More information: <https://github.com/simonw/csv-diff>.

- Show a human-readable summary of differences between files using a specific column as an unique identifier:

`csv-diff {{one.csv}} {{two.csv}} --key={{key}}`

- Show a human-readable summary of differences between files that includes unchanges values in rows that have at least one change:

`csv-diff {{one.csv}} {{two.csv}} --key={{key}} --show-unchanged`

- Show a machine-readable summary of differences between files, treating the column `key` as an unique identifier:

`csv-diff {{one.csv}} {{two.csv}} --key={{key}} --json`
