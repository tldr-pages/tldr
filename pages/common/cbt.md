# cbt

> Utility for reading data from Google Cloud's Bigtable.
> More information: <https://cloud.google.com/bigtable/docs/cbt-reference>.

- List tables in current project:

`cbt ls`

- Return count of rows in table:

`cbt count {{table_name}}`

- Read single row from a table with only 1 (most recent) cell revision per column:

`cbt lookup {{table_name}} {{row_key}} cells-per-column={{1}}`

- Read single row with only specified column(s) (omit qualifier to return entire family):

`cbt lookup {{table_name}} {{row_key}} columns={{family1:qualifier1}},{{family2:qualifier2}},{{...}}`

- Read rows by regex pattern, return at most 5 rows:

`cbt read {{table_name}} regex="{{row_key_pattern}}" count={{5}}`

- Read range of rows and print only returned row keys:

`cbt read {{table_name}} start={{start_row_key}} end={{end_row_key}} keys-only=true`
