# sipcalc

> Calculate IP subnet information for IPv4 and IPv6 addresses.
> See also: `ipcalc`.
> More information: <https://manned.org/sipcalc>.

- Display subnet information for an IPv4 CIDR address:

`sipcalc {{192.168.1.0/24}}`

- Display all available information for an address:

`sipcalc {{[-a|--all]}} {{192.168.1.0/24}}`

- Split an IPv4 network into subnets of a specified mask:

`sipcalc {{[-s|--v4split]}} {{255.255.255.128}} {{192.168.1.0/24}}`

- Display IPv6 reverse DNS information:

`sipcalc {{[-r|--v6rev]}} {{2001:db8::/32}}`

- Enable DNS name resolution:

`sipcalc {{[-d|--resolve]}} {{192.168.1.0/24}}`

- Display help:

`sipcalc {{[-h|--help]}}`
