# sqlite-utils

> SQLite adatbázisok különböző módon történő manipulálására használt parancssori eszköz. További információ: <https://sqlite-utils.datasette.io/en/stable/cli.html>.

- Adatbázis létrehozása:

`sqlite-utils create-database {{path/to/database.db}}`

- Táblázat létrehozása:

`sqlite-utils create-table {{path/to/database.db}} {{table_name}} {{id integer name text height float photo blob --pk id}}`

- Táblák listázása:

`sqlite-utils tables {{path/to/database.db}}`

- Egy rekord felfelé történő beillesztése:

`{{echo '[ {"id": 1, "name": "Linus Torvalds"}, {"id": 2, "name": "Steve Wozniak"}, {"id": 3, "name": "Tony Hoare"} ]'}} | sqlite-utils upsert {{path/to/database.db}} {{table_name}} - {{--pk id}}`

- Rekordok kiválasztása:

`sqlite-utils rows {{path/to/database.db}} {{table_name}}`

- Rekord törlése:

`sqlite-utils query {{path/to/database.db}} "{{delete from table_name where name = 'Tony Hoare'}}"`

- Táblázat törlése:

`sqlite-utils drop-table {{path/to/database.db}} {{table_name}}`

- Súgóinformációk megjelenítése:

`sqlite-utils -h`
