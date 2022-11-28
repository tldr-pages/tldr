# cbt

> Utility for reading data from Google Cloud's Bigtable.
> More information: <https://cloud.google.com/bigtable/docs/cbt-reference>.

- List tables in the current project:

`cbt ls`

- Print count of rows in a specific table in the current project:

`cbt count "{{table_name}}"`

- Display a single row from a specific table with only 1 (most recent) cell revision per column in the current project:

`cbt lookup "{{table_name}}" "{{row_key}}" cells-per-column={{1}}`

- Display a single row with only specific column(s) (omit qualifier to return entire family) in the current project:

`cbt lookup "{{table_name}}" "{{row_key}}" columns="{{family1:qualifier1,family2:qualifier2,...}}"`

- Search up to 5 rows in the current project by a specific regex pattern and print them:

`cbt read "{{table_name}}" regex="{{row_key_pattern}}" count={{5}}`

- Read a specific range of rows and print only returned row keys in the current project:

`cbt read {{table_name}} start={{start_row_key}} end={{end_row_key}} keys-only=true`
