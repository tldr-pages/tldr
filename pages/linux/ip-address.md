# ip address

> IP Address management subcommand.
> More information: <https://manned.org/ip-address>.

- List network interfaces and their associated IP addresses:

`ip {{[a|address]}}`

- Filter to show only active network interfaces:

`ip {{[a|address]}} show up`

- Display information about a specific network interface:

`ip {{[a|address]}} show dev {{eth0}}`

- Add an IP address to a network interface:

`ip {{[a|address]}} add {{ip_address}} dev {{eth0}}`

- Remove an IP address from a network interface:

`ip {{[a|address]}} delete {{ip_address}} dev {{eth0}}`

- Delete all IP addresses in a given scope from a network interface:

`ip {{[a|address]}} flush dev {{eth0}} scope {{global|host|link}}`
