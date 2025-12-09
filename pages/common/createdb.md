# createdb

> Create a PostgreSQL database.
> More information: <https://www.postgresql.org/docs/current/app-createdb.html>.

- Create a database owned by the current user:

`createdb {{database_name}}`

- Create a database owned by a specific user with a description:

`createdb {{[-O|--owner]}} {{username}} {{database_name}} '{{description}}'`

- Create a database from a template:

`createdb {{[-T|--template]}} {{template_name}} {{database_name}}`
