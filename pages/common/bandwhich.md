# bandwhich

> Display the current network utilization by process, connection or remote IP/hostname.
> More information: <https://github.com/imsnif/bandwhich>.

- Show the remote addresses table only:

`bandwhich --addresses`

- Show DNS queries:

`bandwhich --show-dns`

- Show total (cumulative) usage:

`bandwhich --total-utilization`

- Show the network utilization for a specific network interface:

`bandwhich --interface {{eth0}}`

- Show DNS queries with a given DNS server:

`bandwhich --show-dns --dns-server {{dns_server_ip}}`
