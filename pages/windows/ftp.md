# ftp

> Interactively transfer files between a local and remote FTP server.

- Connect to a remote FTP server interactively:

`ftp {{host}}`

- Log in as an anonymous user:

`ftp -A {{host}}`

- Disable automatic login upon initial connection:

`ftp -n {{host}}`

- Run a file containing a list of FTP commands:

`ftp -s:{{path/to/file}} {{host}}`

- Display a list of available interactive commands (once connected):

`help`

- Display help for an interactive command (once connected):

`help {{command}}`

- Display detailed help:

`ftp --help`
