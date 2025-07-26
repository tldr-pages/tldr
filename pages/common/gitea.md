# gitea

> Administer Gitea, a lightweight Git hosting server.
> Requires a configured `app.ini` file or environment variables.
> More information: <https://docs.gitea.com/administration/command-line>.

- Run the Gitea web server using the default configuration:

`gitea web`

- Create the necessary database schema and tables:

`gitea migrate`

- Run administrative subcommands for user management or authentication management:

`gitea admin {{user list}}`

- Display help for a specific subcommand:

`gitea {{admin}} --help`

- Display help:

`gitea help`

- Display version:

`gitea --version`
