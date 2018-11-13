# ipcalc

> Perform simple operations and calculations on IP addresses and networks.

- Show information about an address or network with a given subnet mask:

`ipcalc {{1.2.3.4}} {{255.255.255.0}}`

- Show information about an address or network in CIDR notation:

`ipcalc {{1.2.3.4}}/{{24}}`

- Show the broadcast address of an address or network:

`ipcalc -b {{1.2.3.4}}/{{30}}`

- Show the network address of provided IP address and netmask:

`ipcalc -n {{1.2.3.4}}/{{24}}`

- Display geographic information about a given IP address:

`ipcalc -g {{1.2.3.4}}`
