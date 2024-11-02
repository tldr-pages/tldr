# nxc vnc

> Pentest and exploit VNC servers.
> More information: <https://www.netexec.wiki/>.

- Search for valid credentials by trying out every combination in the specified lists of [u]sernames and [p]asswords:

`nxc vnc {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- Avoid rate limiting through VNC-sleep:

`nxc vnc {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}} --vnc-sleep {{10}}`

- Take a screenshot on the remote system after waiting the specified amount of time:

`nxc vnc {{192.168.178.2}} -u {{username}} -p {{password}} --screenshot --screentime {{10}}`
