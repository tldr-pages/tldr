# bandwhich

> Display the current network utilization by process, connection or remote IP/hostname.
> More information: <https://github.com/imsnif/bandwhich#usage>.

- Show the remote addresses table only:

`bandwhich {{[-a|--addresses]}}`

- Show DNS queries:

`bandwhich {{[-s|--show-dns]}}`

- Show total (cumulative) usage:

`bandwhich {{[-t|--total-utilization]}}`

- Show the network utilization for a specific network interface:

`bandwhich {{[-i|--interface]}} {{eth0}}`

- Show DNS queries with a given DNS server:

`bandwhich {{[-s|--show-dns]}} {{[-d|--dns-server]}} {{dns_server_ip}}`
