# mtr

> Matt's Traceroute: gecombineerde traceroute- en ping-tool.
> Zie ook: `traceroute`, `ping`.
> Meer informatie: <https://manned.org/mtr>.

- Traceroute naar een host en ping continu alle tussenliggende hops:

`mtr {{example.com}}`

- Schakel IP-adres en hostnaam mapping uit:

`mtr {{[-n|--no-dns]}} {{example.com}}`

- Genereer output na het pingen van elke hop 10 keer:

`mtr {{[-w|--report-wide]}} {{example.com}}`

- Forceer IPv4 of IPv6:

`mtr -4 {{example.com}}`

- Wacht een gegeven tijd (in seconden) voordat een volgend pakket naar dezelfde hop wordt verstuurd:

`mtr {{[-i|--interval]}} {{10}} {{example.com}}`

- Toon het Autonomous System Number (ASN) voor elke hop:

`mtr {{[-z|--aslookup]}} {{example.com}}`

- Toon zowel het IP-adres als de reverse DNS-naam:

`mtr {{[-b|--show-ips]}} {{example.com}}`
