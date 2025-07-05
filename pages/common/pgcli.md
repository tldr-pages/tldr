# pgcli

> A modern PostgreSQL CLI with auto-completion and syntax highlighting.
> More information: <https://www.pgcli.com>.

- Connect to a PostgreSQL database using a connection string:

`pgcli postgresql://{{user}}@{{host}}/{{database}}`

- Connect to a database using flags:

`pgcli -h {{host}} -U {{user}} -d {{database}}`

- Enable Vim keybindings for this session:

`pgcli --vi`

- Display help:

`pgcli --help`
