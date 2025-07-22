# gitea

A command-line tool for administering Gitea, a lightweight Git hosting server.

Requires a configured `app.ini` file or environment variables.  
More information: https://docs.gitea.com/administration/command-line

- Show the available commands:
 `gitea help`

* Run the Gitea web server using the default configuration:

 `gitea web`

* Display the current Gitea version:

 `gitea --version`


* Create the necessary database schema and tables:

 `gitea migrate`

* Run built-in admin commands (like user management):

 `gitea admin user list`

* Show help for a specific subcommand:

 `gitea admin --help`