# rails db

> Various database-related subcommands for Ruby on Rails.

- Create databases, load the schema, and initialize with seed data:

`rails db:setup`

- Access the database console:

`rails db`

- Create the databases defined in the current environment:

`rails db:create`

- Destroy the databases defined in the current environment:

`rails db:drop`

- Run pending migrations:

`rails db:migrate`

- View the status of each migration file:

`rails db:migrate:status`

- Rollback the last migration:

`rails db:rollback`

- Fill the current database with data defined in `db/seeds.rb`:

`rails db:seed`
