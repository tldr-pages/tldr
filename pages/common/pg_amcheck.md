# pg_amcheck

> Check for corruption in one or more PostgreSQL databases.
> More information: <https://www.postgresql.org/docs/current/app-pgamcheck.html>.

- Check a specific database:

`pg_amcheck {{database_name}}`

- Check all databases:

`pg_amcheck {{[-a|--all]}}`

- Check databases matching the specified pattern:

`pg_amcheck {{[-d|--database]}} {{pattern}}`

- Check specific tables within a database:

`pg_amcheck {{database_name}} {{[-t|--table]}} {{pattern}}`

- Check specific schemas within a database:

`pg_amcheck {{database_name}} {{[-s|--schema]}} {{pattern}}`

- Display help:

`pg_amcheck {{[-?|--help]}}`
