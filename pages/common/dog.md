# dog

> Dog is a command-line DNS client.  It has colourful output, supports the DNS-over-TLS and DNS-over-HTTPS protocols, and can emit JSON.
> More information: <https://dns.lookup.dog/>.

`dog example.net`

- Query the A record of a domain using default settings

`dog example.net MX`

- Look up MX records instead

`dog example.net MX @1.1.1.1`

- Query using a specific nameserver instead

`dog example.net MX @1.1.1.1 -T`

- Query using TCP rather than UDP

`dog -q example.net -t MX -n 1.1.1.1 -T`

- As above, but using explicit arguments

