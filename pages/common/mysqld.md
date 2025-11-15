# mysqld

> Start the MySQL database server.
> More information: <https://dev.mysql.com/doc/refman/en/mysqld.html>.

- Start the MySQL database server:

`mysqld`

- Start the server, printing error messages to the console:

`mysqld --console`

- Start the server, saving logging output to a custom log file:

`mysqld --log={{path/to/file.log}}`

- Print the default arguments and their values and exit:

`mysqld --print-defaults`

- Start the server, reading arguments and values from a file:

`mysqld --defaults-file={{path/to/file}}`

- Start the server and listen on a custom port:

`mysqld --port={{port}}`

- Display help:

`mysqld --verbose --help`
