# mtr

> Matt's Traceroute: combined traceroute and ping tool.
> More information: <https://manned.org/mtr>.

- Traceroute to a host and continuously ping all intermediary hops:

`mtr {{example.com}}`

- Disable IP address and host name mapping:

`mtr {{[-n|--no-dns]}} {{example.com}}`

- Generate output after pinging each hop 10 times:

`mtr {{[-w|--report-wide]}} {{example.com}}`

- Force IP IPv4 or IPV6:

`mtr -4 {{example.com}}`

- Wait for a given time (in seconds) before sending another packet to the same hop:

`mtr {{[-i|--interval]}} {{10}} {{example.com}}`

- Display the Autonomous System Number (ASN) for each hop:

`mtr {{[-z|--aslookup]}} {{example.com}}`

- Display both IP address and reverse DNS name:

`mtr {{[-b|--show-ips]}} {{example.com}}`
