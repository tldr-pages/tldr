# f5fpc

> A proprietary commercial SSL VPN client by BIG-IP Edge.
> More information: <https://techdocs.f5.com/kb/en-us/products/big-ip_apm/manuals/product/apm-client-configuration-11-4-0/4.html>.

- Open a new VPN connection:

`sudo f5fpc --start`

- Open a new VPN connection to a specific host:

`sudo f5fpc --start --host {{host.example.com}}`

- Specify a username (user will be prompted for a password):

`sudo f5fpc --start --host {{host.example.com}} --username {{user}}`

- Show the current VPN status:

`sudo f5fpc --info`

- Shutdown the VPN connection:

`sudo f5fpc --stop`
