# ifdata

> Display information about a network interface.
> More information: <https://manned.org/ifdata>.

- [p]rint the whole configuration of the specified interface:

`ifdata -p {{eth0}}`

- Indicate the [e]xistence of the specified interface via the exit code:

`ifdata -e {{eth0}}`

- [p]rint the IPv4 [a]dress and the [n]etmask of the specified interface:

`ifdata -pa -pn {{eth0}}`

- [p]rint the [N]etwork adress, the [b]roadcast adress, and the [m]TU of the specified interface:

`ifdata -pN -pb -pm {{eth0}}`

- Display help:

`ifdata`
