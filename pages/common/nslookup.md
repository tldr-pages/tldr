# nslookup

> Query name server(s) for various domain records.

- Query your system's default name server for an IP address (A record) of the domain:

`nslookup {{example.com}}`

- Query non default name server (here Google DNS 8.8.8.8) for a NS record of the domain:

`nslookup -type=NS {{example.com}} 8.8.8.8`

- Query default name server for a reverse lookup (PTR record) of an IP address:

`nslookup -type=PTR 54.240.162.118`

- Query default name server for an IP address (A record) of the domain using TCP protocol (-vc option) instead of the default UDP:

`nslookup -vc {{example.com}}`

- Query default name server for a mail server (MX record) of the domain, showing details of the transaction:

`nslookup -type=MX -debug {{example.com}}`

- Query a given name server on a specific port number for a TXT record of the domain:

`nslookup -port={{port_number}} -type=TXT {{example.com}} {{name_server}}`
