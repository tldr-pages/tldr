# smbclient

> FTP-like client to access SMB/CIFS resources on servers.
> More information: <https://www.samba.org/samba/docs/current/man-html/smbclient.1.html>.

- List available shares on a server:

`smbclient --list={{server}}`

- Connect to a share (will prompt for a password):

`smbclient //{{server}}/{{share}}`

- Connect to a share as a specific user:

`smbclient --user={{domain/username}} //{{server}}/{{share}}`

- Connect to a share as a specific user with inline password:

`smbclient --user={{domain/username%password}} //{{server}}/{{share}}`

- Connect to a share using a specific workgroup:

`smbclient --workgroup={{domain}} --user={{username}} //{{server}}/{{share}}`

- Download a file from a specific directory on a share:

`smbclient --user={{domain/username}} //{{server}}/{{share}} --directory {{path/to/directory}} --command='get {{filename}}'`

- Upload a file to a specific directory on a share:

`smbclient --user={{domain/username}} //{{server}}/{{share}} --directory {{path/to/directory}} --command='put {{path/to/local_file}}'`
