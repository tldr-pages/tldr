# nxc vnc

> Pentest and exploit VNC servers.
> More information: <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>.

- Search for valid credentials by trying out every combination in the specified lists of usernames and passwords:

`nxc vnc {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Avoid rate limiting through VNC-sleep:

`nxc vnc {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}} --vnc-sleep {{10}}`

- Take a screenshot on the remote system after waiting the specified amount of time:

`nxc vnc {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --screenshot --screentime {{10}}`
