# typeorm

> A JavaScript ORM that can run on Node.js, browser, Cordova, Ionic, React Native, NativeScript, and Electron platforms.
> More information: <https://typeorm.io/>.

- Generate a new initial TypeORM project structure:

`typeorm init`

- Create an empty migration file:

`typeorm migration:create --name {{migration_name}}`

- Create a migration file with the SQL sentences to update the schema:

`typeorm migration:generate --name {{migration_name}}`

- Run all pending migrations:

`typeorm migration:run`

- Create a new entity file in a specific directory:

`typeorm entity:create --name {{entity}} --dir {{path/to/directory}}`

- Display the SQL sentences to be executed by `typeorm schema:sync` on the default connection:

`typeorm schema:log`

- Execute a specific SQL sentence on the default connection:

`typeorm query {{sql_sentence}}`

- Display help for a subcommand:

`typeorm {{subcommand}} --help`
