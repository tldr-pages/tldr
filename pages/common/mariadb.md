# mariadb

> The mariadb Command-Line Client tool.
> More information: <https://mariadb.com/kb/en/mariadb-command-line-client/>.

- Connect to a specific MariaDB database:

`mariadb {{db_name}}`

- Connects to a specific MariaDB database {{db_name}} using {{user_name}} and {{your_password}}:

`mariadb --user={{user_name}} --password={{your_password}} {{db_name}}`

- Display help and exit:

`mariadb -?, --help`

- Show warnings after every statement in interactive and batch mode:

`mariadb --show-warning`

- Be more silent. Can be used multiple times to produce less output:

`mariadb -s, --silent`

- Execute SQL statements in a script file (batch file):

`mariadb {{db_name}} < {{/path/to/script.sql}} > {{/path/to/output.tab}}`

- Check memory and open file usage at exit:

`mariadb --debug-check`

- For connections to local host , Unix socket file to use, or on Windows, the name of the named pipe to use:

`mariadb -S, --socket={{/path/to/socket_name}}`
