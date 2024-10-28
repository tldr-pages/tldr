# nxc rdp

> Pentest and exploit RDP servers.
> More information: <https://www.netexec.wiki/rdp-protocol>.

- Search for valid credentials by trying out every combination in the specified lists of [u]sernames and [p]asswords:

`nxc rdp {{192.168.178.2}} -u {{path/to/usernames.txt}} -p {{path/to/passwords.txt}}`

- Take a screenshot after waiting the for specified number of seconds:

`nxc rdp {{192.168.178.2}} -u {{username}} -p {{password}} --screenshot --screentime {{10}}`

- Take a screenshot in the specified resolution:

`nxc rdp {{192.168.178.2}} -u {{username}} -p {{password}} --screenshot --res {{1024x768}}`

- Take a screenshot of the RDP login prompt if Network Level Authentication is disabled:

`nxc rdp {{192.168.178.2}} -u {{username}} -p {{password}} --nla-screenshot`
