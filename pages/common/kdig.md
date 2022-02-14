# kdig

> Advanced DNS lookup utility.
> More information: https://manned.org/kdig.
- Get A records for example.com:

`kdig {{example.com}}`

- Specify an DNS server to query(e.g. google DNS):

`kdig {{example.com}} @{{8.8.8.8}}`

- Query a specific DNS record type associated with a given domain name:

`kdig {{example.com}} {{A|AAAA|NS|SOA|DNSKEY|ANY}}`

- Get A record for example.com use TLS(DoT):

`kdig -d @{{8.8.8.8}} +tls-ca +tls-host={{dns.google}} example.com`

- Get A record for example.com use HTTPS(DoH):

`kdig -d @{{8.8.8.8}} +https +tls-hostname={{dns.google}} example.com`
