# knotc

> Control knot DNS server.
> More information: <https://www.knot-dns.cz/docs/latest/html/man_knotc.html>.

- Start editing a zone:

`knotc zone-begin {{zone}}`

- Set an A record with TTL of 3600:

`knotc zone-set {{zone}} {{subdomain}} 3600 A {{ip_address}}`

- Finish editing the zone:

`knotc zone-commit {{zone}}`

- Get the current zone data:

`knotc zone-read {{zone}}`

- Get the current server configuration:

`knotc conf-read server`
