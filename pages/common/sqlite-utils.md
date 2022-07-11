# sqlite-utils

> Command-line tool used to manipulate SQLite databases in a number of different ways.
> More information: <https://sqlite-utils.datasette.io/en/stable/cli.html>.

- Create a database:

`sqlite-utils create-database {{path/to/database.db}}`

- Create a table:

`sqlite-utils create-table {{path/to/database.db}} {{table_name}} {{id integer name text height float photo blob --pk id}}`

- List tables:

`sqlite-utils tables {{path/to/database.db}}`

- Upsert a record:

`{{echo '[ {"id": 1, "name": "Linus Torvalds"}, {"id": 2, "name": "Steve Wozniak"}, {"id": 3, "name": "Tony Hoare"} ]'}} | sqlite-utils upsert {{path/to/database.db}} {{table_name}} - {{--pk id}}`

- Select records:

`sqlite-utils rows {{path/to/database.db}} {{table_name}}`

- Delete a record:

`sqlite-utils query {{path/to/database.db}} "{{delete from table_name where name = 'Tony Hoare'}}"`

- Drop a table:

`sqlite-utils drop-table {{path/to/database.db}} {{table_name}}`

- Show help information:

`sqlite-utils -h`
