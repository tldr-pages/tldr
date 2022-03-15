# dog

> DNS lookup utility.
> It has colorful output, supports DNS-over-TLS and DNS-over-HTTPS protocols, and can emit JSON.
> More information: <https://dns.lookup.dog>.

- Lookup the IP(s) associated with a hostname (A records):

`dog {{example.com}}`

- Query MX records type associated with a given domain name:

`dog example.net MX`

- Query using a specific nameserver instead:

`dog example.net MX @1.1.1.1`

- Query using TCP rather than UDP:

`dog example.net MX @1.1.1.1 -T`

- As above, but using explicit arguments:

`dog -q example.net -t MX -n 1.1.1.1 -T`
