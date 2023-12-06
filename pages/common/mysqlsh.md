# mysqlsh

> Advanced command-line client for MySQL, supporting SQL, JavaScript, and Python.
> It offers features for managing InnoDB clusters and document store collections.
> More information: <https://dev.mysql.com/doc/mysql-shell/8.0/en/mysql-shell-commands.html>.

- Start MySQL Shell in interactive mode:

`mysqlsh`

- Connect to a MySQL server:

`mysqlsh --user {{username}} --host {{hostname}} --port {{port}}`

- Execute a SQL statement on the server and exit:

`mysqlsh --user {{username}} --execute '{{sql_statement}}'`

- Start MySQL Shell in JavaScript mode:

`mysqlsh --js`

- Start MySQL Shell in Python mode:

`mysqlsh --py`

- Import JSON documents into a MySQL collection:

`mysqlsh --import {{path/to/file.json}} --schema {{schema_name}} --collection {{collection_name}}`

- Enable verbose output:

`mysqlsh --verbose`
