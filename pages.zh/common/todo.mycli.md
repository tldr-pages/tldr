# mycli

> A command line client for MySQL that can do auto-completion and syntax highlighting.
> More information: <https://mycli.net>.

- Connect to a local database on port 3306, using the current user's username:

`mycli {{database_name}}`

- Connect to a database (user will be prompted for a password):

`mycli -u {{username}} {{database_name}}`

- Connect to a database on another host:

`mycli -h {{database_host}} -P {{port}} -u {{username}} {{database_name}}`
