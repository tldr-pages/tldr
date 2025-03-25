# mariadb

> The mariadb client tool.
> More information: <https://mariadb.com/kb/en/mariadb-command-line-client/>.

- Connect to a specific MariaDB database:

`mariadb {{db_name}}`

- Connect to a specific MariaDB database using username and password:

`mariadb --user {{user_name}} --password {{your_password}} {{db_name}}`

- Show warnings after every statement in interactive and batch mode:

`mariadb --show-warning`

- Display less verbose outputs (can be used multiple times to produce less output):

`mariadb {{-s|-ss|-sss|--silent}}`

- Execute SQL statements from a script file:

`mariadb {{db_name}} < {{path/to/script.sql}} > {{path/to/output.tab}}`

- Check memory and open file usage at exit:

`mariadb --debug-check`

- Connect using a socket file for local connections:

`mariadb {{[-S|--socket]}} {{path/to/socket_name}}`

- Display help:

`mariadb {{[-?|--help]}}`
