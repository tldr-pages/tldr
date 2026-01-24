# tlsx

> Fast and configurable TLS grabber focused on TLS based data collection and analysis.
> More information: <https://github.com/projectdiscovery/tlsx#usage>.

- Display TLS version and cipher of one or more hosts:

`tlsx {{[-u|-host]}} {{host1,host2,...}} {{[-tv|-tls-version]}} -cipher`

- Enumerate and display supported TLS versions and ciphers of a host:

`tlsx {{[-u|-host]}} {{host}} {{[-ve|-version-enum]}} {{[-ce|-cipher-enum]}}`

- Scan a list of hosts from a file and mark hosts with expired/self-signed/mismatched/revoked/untrusted certificates:

`tlsx {{[-l|-list]}} {{path/to/hosts.txt}} {{[-ex|-expired]}} {{[-ss|-self-signed]}} {{[-mm|-mismatched]}} {{[-re|-revoked]}} {{[-un|-untrusted]}}`

- Adjust per host concurrency, timeout, retry and delay parameters when scanning a list of hosts for wildcard SSL certificates:

`tlsx {{[-l|-list]}} {{path/to/hosts.txt}} {{[-c|-concurrency]}} {{300}} -timeout {{5}} -retry {{3}} -delay {{200ms}} {{[-wc|-wildcard-cert]}}`

- Display unique hostname(s) from SSL certificate response:

`tlsx {{[-u|-host]}} {{host}} -dns`

- Display Subject Alternative Names (SANs) from the TLS certificate of a host, with JSON output written to a file:

`tlsx {{[-u|-host]}} {{host}} -san {{[-j|-json]}} {{[-o|-output]}} {{path/to/file.json}}`

- Perform a self health-check of `tlsx` itself:

`tlsx {{[-hc|-health-check]}}`
