# gitea

> Administering Gitea, a lightweight Git hosting server.
> Requires a configured `app.ini` file or environment variables.
> More information: <https://docs.gitea.com/administration/command-line>.

- Run the Gitea web server using the default configuration:

`gitea web`

- Create the necessary database schema and tables:

`gitea migrate`

- Run built-in admin commands (like user management):

`gitea admin user list`

- Show help for a specific subcommand:

`gitea admin --help`

- Display the current Gitea version:

`gitea --version`

- Show the available commands:

`gitea help`
