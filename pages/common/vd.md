# vd

> Terminal spreadsheet multitool for exploring and arranging tabular data.
> Supports CSV, JSON, Excel, SQLite, and many other formats.
> More information: <https://www.visidata.org/man/>.

- Open a file for interactive exploration:

`vd {{path/to/file.csv}}`

- Open a SQLite database (lists all tables):

`vd {{path/to/database.db}}`

- Convert a file to a different format:

`vd {{path/to/input.csv}} {{[-b|--batch]}} {{[-o|--output]}} {{path/to/output.json}}`

- Read tabular data from `stdin`:

`cat {{path/to/file.csv}} | vd -`

- Open a file with a specific field delimiter:

`vd --csv-delimiter {{,}} {{path/to/file.csv}}`
