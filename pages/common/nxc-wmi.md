# nxc wmi

> Pentest and exploit the Windows Management Instrumentation (WMI).
> More information: <https://www.netexec.wiki/wmi-protocol>.

- Search for valid credentials by trying out every combination in the specified lists of usernames and passwords:

`nxc wmi {{192.168.178.2}} {{[-u|--username]}} {{path/to/usernames.txt}} {{[-p|--password]}} {{path/to/passwords.txt}}`

- Authenticate via local authentication (as opposed to authenticating to the domain):

`nxc wmi {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --local-auth`

- Issue the specified WMI query:

`nxc wmi {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} --wmi {{wmi_query}}`

- Execute the specified command on the targeted host:

`nxc wmi {{192.168.178.2}} {{[-u|--username]}} {{username}} {{[-p|--password]}} {{password}} -x {{command}}`
