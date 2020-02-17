# sequelize

> Promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server.
> More information: <https://sequelize.org/>.

- Create a model and a migration file:

`sequelize model:generate --name {{table_name}}`

- Run the migration file:

`sequelize db:migrate`

- Revert all migrations:

`sequelize db:migrate:undo:all`

- Create a seed file with the specified name to populate the database:

`sequelize seed:generate --name {{seed_filename}}`

- Populate database using all seed files:

`sequelize db:seed:all`
