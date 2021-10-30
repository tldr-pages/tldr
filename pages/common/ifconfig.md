# ifconfig

> Network Interface Configurator.
> More information: <https://net-tools.sourceforge.io/man/ifconfig.8.html>.

- View network settings of an Ethernet adapter:

`ifconfig eth0`

- Display details of all interfaces, including disabled interfaces:

`ifconfig -a`

- Disable eth0 interface:

`ifconfig eth0 down`

- Enable eth0 interface:

`ifconfig eth0 up`

- Assign IP address to eth0 interface:

`ifconfig eth0 {{ip_address}}`
