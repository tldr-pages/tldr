# ipcalc

> Perform simple operations and calculations on IP addresses and networks.

- Show information about an address or network:

`ipcalc {{ip_address}} {{subnet_mask}}`

- Show information about an address or network in CIDR notation:

`ipcalc {{ip_address}}/{{masked_bits}}`

- Show the broadcast address of an address or network:

`ipcalc -b {{ip_address}}/{{masked_bits}}`

- Show the network address of provided IP address and netmask:

`ipcalc -n {{ip_address}}/{{masked_bits}}`

- Display geographic information about a given IP address:

`ipcalc -g {{ip_address}}`
