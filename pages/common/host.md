# host

> Lookup Domain Name Server.

- Lookup A, AAAA, and MX records of a domain:

`host {{domain}}`

- Lookup a field (CNAME, TXT,...) of a domain:

`host -t {{field}} {{domain}}`

- Reverse lookup an IP:

`host {{ip_address}}`
