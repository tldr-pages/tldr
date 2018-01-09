# smbclient

> FTP-like client to access SMB/CIFS resources on servers.

- Connect to a share (`exit` to quit the session):

`smbclient {{//server/share}}`

- Connect with a username and password:

`smbclient {{//server/share}} --user {{username%password}}`

- Download a file from the server:

`smbclient {{//server/share}} --directory {{path/to/folder}} --command "get {{file.txt}}"`

- Upload a file to the server:

`smbclient {{//server/share}} --directory {{path/to/folder}} --command "put {{file.txt}}"`
