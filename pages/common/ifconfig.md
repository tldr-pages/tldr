# ifconfig

> Network Interface Configurator.
> More information: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- View network settings of an interface:

`ifconfig {{interface_name}}`

- Display details of all interfaces, including disabled interfaces:

`ifconfig -a`

- Disable an interface:

`ifconfig {{interface_name}} down`

- Enable an interface:

`ifconfig {{interface_name}} up`

- Assign an IP address to an interface:

`ifconfig {{interface_name}} {{ip_address}}`
