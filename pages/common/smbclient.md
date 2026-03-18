# smbclient

> FTP-like client to access SMB/CIFS resources on servers.
> More information: <https://manned.org/smbclient>.

- List available shares on a server:

`smbclient {{[-L|--list]}} {{server}}`

- Connect to a share (will prompt for a password):

`smbclient //{{server}}/{{share}}`

- Connect to a share as a specific user:

`smbclient {{[-U|--user]}} {{domain/username}} //{{server}}/{{share}}`

- Connect to a share as a specific user with inline password:

`smbclient {{[-U|--user]}} {{domain/username%password}} //{{server}}/{{share}}`

- Connect to a share using a specific workgroup:

`smbclient {{[-W|--workgroup]}} {{domain}} {{[-U|--user]}} {{username}} //{{server}}/{{share}}`

- Download a file from a specific directory on a share:

`smbclient {{[-U|--user]}} {{domain/username}} //{{server}}/{{share}} {{[-D|--directory]}} {{path/to/directory}} {{[-c|--command]}} 'get {{filename}}'`

- Upload a file to a specific directory on a share:

`smbclient {{[-U|--user]}} {{domain/username}} //{{server}}/{{share}} {{[-D|--directory]}} {{path/to/directory}} {{[-c|--command]}} 'put {{path/to/local_file}}'`
