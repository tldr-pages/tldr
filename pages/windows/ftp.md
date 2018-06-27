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

- Download multiple files (glob expression):

`mget {{*.png}}`

- Upload multiple files (glob expression):

`mput {{*.zip}}`

- Delete multiple files on the remote server:

`mdelete {{*.txt}}`

- Display detailed help:

`ftp --help`
