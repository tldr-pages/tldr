# nxc winrm

> Pentest and exploit Windows Remote Management (winrm).
> More information: <https://www.netexec.wiki/winrm-protocol>.

- Search for valid credentials by trying out every combination in the specified lists of [u]sernames and [p]asswords:

`nxc winrm {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- Specify the domain to authenticate to (avoids an initial SMB connection):

`nxc winrm {{192.168.178.2}} -u {{username}} -p {{password}} -d {{domain_name}}`

- Execute the specified command on the host:

`nxc winrm {{192.168.178.2}} -u {{username}} -p {{password}} -x {{whoami}}`

- Execute the specified PowerShell command on the host as administrator using LAPS:

`nxc winrm {{192.168.178.2}} -u {{username}} -p {{password}} --laps -X {{whoami}}`
