# pfctl

> Control the packet filter device.
> More information: <https://man.freebsd.org/cgi/man.cgi?query=pfctl>.

- Enable the packet filter:

`sudo pfctl -e`

- Disable the packet filter:

`sudo pfctl -d`

- Load rules from a configuration file:

`sudo pfctl -f {{path/to/pf.conf}}`

- Show all active rules:

`pfctl -sr`

- Show packet filter status information:

`pfctl -s info`

- Flush all rules:

`sudo pfctl -F rules`
