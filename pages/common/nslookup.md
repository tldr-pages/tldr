# nslookup

> Query name server(s) for various domain records.
> More information: <https://manned.org/nslookup>.

- Query your system's default name server for an IP address (A record) of the domain:

`nslookup {{example.com}}`

- Query a given name server for a NS record of the domain:

`nslookup -type=NS {{example.com}} {{8.8.8.8}}`

- Query for a reverse lookup (PTR record) of an IP address:

`nslookup -type=PTR {{54.240.162.118}}`

- Query for ANY available records using TCP protocol:

`nslookup -vc -type=ANY {{example.com}}`

- Query a given name server for the whole zone file (zone transfer) of the domain using TCP protocol:

`nslookup -vc -type=AXFR {{example.com}} {{name_server}}`

- Query for a mail server (MX record) of the domain, showing details of the transaction:

`nslookup -type=MX -debug {{example.com}}`

- Query a given name server on a specific port number for a TXT record of the domain:

`nslookup -port={{port_number}} -type=TXT {{example.com}} {{name_server}}`
