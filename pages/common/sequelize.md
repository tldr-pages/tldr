# sequelize

> Promise-based Node.js ORM for Postgres, MySQL, MariaDB, SQLite and Microsoft SQL Server.

- Creating model and migration file:

`sequelize model:generate --name {{table_name}}`

- Run migration file:

`sequelize db:migrate`

- Revert all migration to initial state:

`sequelize db:migrate:undo:all`

- Create seed file to populate database:

`sequelize seed:generate --name {{example}}`

- Populate database using all seed file:

`sequelize db:seed:all`
