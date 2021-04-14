# bandwhich

> A CLI utility for displaying current network utilization by process, connection and remote IP/hostname.
> More information: <https://github.com/imsnif/bandwhich>.

- Show remote addresses table only:

`bandwhich --addresses`

- Show DNS queries:

`bandwhich --show-dns`

- Show total (cumulative) usages:

`bandwhich --total-utilization`

- Show network utilization for given interface (eg. {{eth0}}):

`bandwhich --interface {{interface}}`

- Show DNS queries with a given DNS server:

`bandwhich --show-dns --dns-server {{dns-server}}`
