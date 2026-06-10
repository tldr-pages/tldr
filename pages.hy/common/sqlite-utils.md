# sqlite-utils

> Շահարկել SQLite տվյալների բազաները մի շարք տարբեր ձևերով:.
> Լրացուցիչ տեղեկություններ. <https://sqlite-utils.datasette.io/en/stable/cli.html>:.

- Ստեղծել տվյալների բազա.:

`sqlite-utils create-database {{path/to/database.db}}`

- Ստեղծեք աղյուսակ.:

`sqlite-utils create-table {{path/to/database.db}} {{table_name}} {{id integer name text height float photo blob --pk id}}`

- Ցուցակ աղյուսակներ.:

`sqlite-utils tables {{path/to/database.db}}`

- Տեղադրեք գրառում.:

`{{echo '[ {"id": 1, "name": "Linus Torvalds"}, {"id": 2, "name": "Steve Wozniak"}, {"id": 3, "name": "Tony Hoare"} ]'}} | sqlite-utils upsert {{path/to/database.db}} {{table_name}} - {{--pk id}}`

- Ընտրեք գրառումները.:

`sqlite-utils rows {{path/to/database.db}} {{table_name}}`

- Ջնջել գրառումը.:

`sqlite-utils query {{path/to/database.db}} "{{delete from table_name where name = 'Tony Hoare'}}"`

- Սեղան գցեք.:

`sqlite-utils drop-table {{path/to/database.db}} {{table_name}}`

- Ցուցադրել օգնությունը.:

`sqlite-utils {{[-h|--help]}}`
