# f5fpc

> A proprietry commercial SSL VPN client by BIG-IP Edge.

- Open a new VPN connection:

`f5fpc --start`

- Open a new VPN connection to a specific host:

`f5fpc --start --host {{host.example.com}}`

- Specify a username (user will be prompted for a password):

`f5fpc --start --host {{host.example.com}} --username {{user}}`

- Show the current VPN status:

`f5fpc --info`

- Shutdown the VPN connection:

`f5fpc --stop`
