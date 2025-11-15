# nxc ftp

> Pentest and exploit FTP servers.
> More information: <https://www.netexec.wiki/ftp-protocol>.

- Search for valid credentials by trying out every combination in the specified lists of usernames and passwords:

`nxc ftp {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Continue searching for valid credentials even after valid credentials have been found:

`nxc ftp {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}} --continue-on-success`

- Perform directory listings on each FTP server the supplied credentials are valid on:

`nxc ftp {{192.168.178.0/24}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --ls`

- Download the specified file from the target server:

`nxc ftp {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --get {{path/to/file}}`

- Upload the specified file to the target server at the specified location:

`nxc ftp {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --put {{path/to/local_file}} {{path/to/remote_location}}`
