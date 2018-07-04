# mycli

> A CLI for MySQL, MariaDB, and Percona with auto-completion and syntax highlighting.

- Connect to a database with the currently logged in user:

`mycli {{database_name}}`

- Connect to a database with the specified user:

`mycli -u {{user}} {{database_name}}`

- Connect to a database on the specified host with the specified user:

`mycli -u {{user}} -h {{host}} {{database_name}}`

- Connect to a database with URI:

`mycli mysql://{{user}}@{{host}}`

- Connect to a database with URI more directly:

`mycli mysql://{{user}}:{{password}}@{{host}}:{{port}}/{{database_name}}`
