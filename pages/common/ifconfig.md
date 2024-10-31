# ifconfig

> Network Interface Configurator.
> More information: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- View network settings of an Interface:

`ifconfig {{interface_name}}`

- Display details of all interfaces, including disabled interfaces:

`ifconfig -a`

- Disable interface:

`ifconfig {{interface_name}} down`

- Enable interface:

`ifconfig {{interface_name}} up`

- Assign IP address to interface:

`ifconfig {{interface_name}} {{ip_address}}`
