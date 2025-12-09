# sqlx

> Utility for SQLx, the Rust SQL toolkit.
> More information: <https://github.com/launchbadge/sqlx/blob/main/sqlx-cli/README.md>.

- Create the database specified in the `$DATABASE_URL` environment variable:

`sqlx database create`

- Drop the specified database:

`sqlx database drop {{[-D|--database-url]}} {{database_url}}`

- Create a new pair of up and down migration files with the given description in the "migrations" directory:

`sqlx migrate add -r {{migration_description}}`

- Run all pending migrations for the specified database:

`sqlx migrate run {{[-D|--database-url]}} {{database_url}}`

- Revert the latest migration for the specified database:

`sqlx migrate revert {{[-D|--database-url]}} {{database_url}}`
