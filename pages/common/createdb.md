# createdb

> Create a PostgreSQL database
> More information: <https://www.postgresql.org/docs/current/app-createdb.html>.

- Create a database owned by the current user:

`createdb {{database}}`

- Create a database owned by a specific user, with an optional description:

`createdb -O {{user}} {{database}} 'Description of the database'`

- Create a database from a template:

`createdb -T {{template_database}} {{database}}`
