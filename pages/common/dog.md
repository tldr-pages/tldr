# dog

> DNS lookup utility.
> It has colorful output, supports DNS-over-TLS and DNS-over-HTTPS protocols, and can emit JSON.
> More information: <https://dns.lookup.dog>.

- Lookup the IP(s) associated with a hostname (A records):

`dog {{example.com}}`

- Query the MX records type associated with a given domain name:

`dog {{example.com}} MX`

- Specify a specific DNS server to query (e.g. Cloudflare):

`dog {{example.com}} MX @{{1.1.1.1}}`

- Query over TCP rather than UDP:

`dog {{example.com}} MX @{{1.1.1.1}} --tcp`

- Query the MX records type associated with a given domain name over TCP using explicit arguments:

`dog --query {{example.com}} --type MX --nameserver {{1.1.1.1}} --tcp`

- Lookup the IP(s) associated with a hostname (A records) using DNS over HTTPS (DoH):

`dog {{example.com}} --https @{{https://cloudflare-dns.com/dns-query}}`
