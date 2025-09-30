# nxc winrm

> Pentest and exploit Windows Remote Management (winrm).
> More information: <https://www.netexec.wiki/winrm-protocol>.

- Search for valid credentials by trying out every combination in the specified lists of usernames and passwords:

`nxc winrm {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Specify the domain to authenticate to (avoids an initial SMB connection):

`nxc winrm {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -d {{domain_name}}`

- Execute the specified command on the host:

`nxc winrm {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -x {{whoami}}`

- Execute the specified PowerShell command on the host as administrator using LAPS:

`nxc winrm {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --laps -X {{whoami}}`
