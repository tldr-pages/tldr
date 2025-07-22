# gitea

A command-line tool for administering Gitea, a lightweight Git hosting server.

> Requires a configured `app.ini` or environment variables.
> More information: <https://docs.gitea.com/administration/command-line>.

- Show the available commands:
  ```sh
  gitea help
    ````

* Run Gitea web server using the default configuration:

  ```sh
  gitea web
  ```

* Display current Gitea version:

  ```sh
  gitea --version
  ```

* Create the necessary database schema and tables:

  ```sh
  gitea migrate
  ```

* Run the built-in admin commands (like user management):

  ```sh
  gitea admin user list
  ```

* Run a specific subcommand with help output:

  ```sh
  gitea admin --help
  ```
