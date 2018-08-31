# ipcalc

> Perform simple operations/calculations on IP addresses and networks.

- Show information about an address/network:

`ipcalc {{ip_address}} {{subnet_mask}}`

- Show information about an address/network in CIDR notation:

`ipcalc {{ip_address}}/{{masked_bits}}`

- Show broadcast address of an address/network:

`ipcalc -b {{ip_address}}/{{masked_bits}}`

- Show network address of provided IP address and netmask:

`ipcalc -n {{ip_address}}/{{masked_bits}}`

- Display geographic information of provided IP address:

`ipcalc -g {{ip_address}}`
