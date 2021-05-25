# smbget

> `wget`-like utility for downloading files from SMB servers.
> More information: <https://www.samba.org/samba/docs/current/man-html/smbget.1.html>.

- Download a file from a server:

`smbget {{smb://server/share/file}}`

- Download a share or directory recursively:

`smbget --recursive {{smb://server/share}}`

- Connect with a username and password:

`smbget {{smb://server/share/file}} --user {{username%password}}`

- Require encrypted transfers:

`smbget {{smb://server/share/file}} --encrypt`
