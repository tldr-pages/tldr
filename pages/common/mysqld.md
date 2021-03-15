# mysqld

> Start the MariaDB database server.
> More information: <https://dev.mysql.com/doc/refman/8.0/en/mysqld.html>.

- Start the MariaDB database server:

`mysqld`

- Display error messages:

`mysqld --console`

- Specify the log file location:

`mysqld --log={{path/to/file}}`

- Print the default arguments and exit:

`mysqld --print-defaults`

- Use default arguments from a specified file:

`mysqld --defaults-file={{path/to/file}}`

- Specify the port number to use for connections:

`mysqld --port={{port}}`

- Show all help options:

`mysqld --verbose --help`
