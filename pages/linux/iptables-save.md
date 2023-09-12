# iptables-save

> Save the `iptables` IPv4 configuration.
> Use `ip6tables-save` to to the same for IPv6.
> More information: <https://manned.org/iptables-save>.

- Print the `iptables` configuration:

`sudo iptables-save`

- Print the `iptables` configuration of a specific [t]able:

`sudo iptables-save --table {{table}}`

- Save the `iptables` configuration to a [f]ile:

`sudo iptables-save --file {{path/to/file}}`
