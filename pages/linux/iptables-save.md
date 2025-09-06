# iptables-save

> Save the `iptables` IPv4 configuration.
> Use `ip6tables-save` to do the same for IPv6.
> More information: <https://manned.org/iptables-save>.

- Print the `iptables` configuration:

`sudo iptables-save`

- Print the `iptables` configuration of a specific table:

`sudo iptables-save {{[-t|--table]}} {{table}}`

- Save the `iptables` configuration to a file:

`sudo iptables-save {{[-f|--file]}} {{path/to/file}}`
