# ip address

> IP Address management subcommand.

- List network interfaces and their associated IP addresses:

`ip address`

- Filter to show only active network interfaces:

`ip address show up`

- Display information about a specific network interface:

`ip address show dev {{network_interface}}`

- Add an IP address to a network interface:

`ip address add {{ip_address}} dev {{network_interface}}`

- Remove an IP address from a network interface:

`ip address delete {{ip_address}} dev {{network_interface}}`

- Delete all IP addresses in a given scope from a network interface:

`ip address flush dev {{network_interface}} scope {{global|host|link}}`
