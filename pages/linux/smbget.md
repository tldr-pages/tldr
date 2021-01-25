# smbget

> Wget-like utility for downloading files from SMB servers.

- Download a file from a server:

`smbget {{smb://server/share/file}}`

- Download a share or directory recursively:

`smbget -R {{smb://server/share}}`

- Connect with a username and password:

`smbget {{smb://server/share/file}} --user {{username%password}}`

- Require encrypted transfers:

`smbget {{smb://server/share/file}} --encrypt`
