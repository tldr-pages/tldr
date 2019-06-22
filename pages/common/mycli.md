# mycli

> A command line client for MySQL that can do auto-completion and syntax highlighting.

- Connect local database with port 3306 and current user's username:

`mycli {{database_name}}`

- Connect to a database (user will be prompted for a password):

`mycli -u {{username}} {{database_name}}`

- Connect to a database on other host:

`mycli -h {{database_host}} -P {{port}} -u {{username}} {{database_name}}`
