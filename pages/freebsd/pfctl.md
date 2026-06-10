# pfctl

> Control the packet filter device.
> More information: <https://man.freebsd.org/cgi/man.cgi?query=pfctl>.

- Enable PF:

`pfctl -e`

- Disable PF:

`pfctl -d`

- Load rules from a configuration file:

`pfctl -f {{path/to/pf.conf}}`

- Show all active rules:

`pfctl -sr`

- Show PF status information:

`pfctl -s info`

- Flush all rules:

`pfctl -F rules`
