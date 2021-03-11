# dig

> Domain Information Groper: queries and displays information from DNS nameservers.
> More information: <https://manpages.debian.org/buster/dnsutils/dig.1.en.html>.

- Lookup IP address(A records)  for a given domain. It displays technical details alongside the IP address:

`dig {{example.com}}`

- Get the IP addresses for a given domain only:

`dig {{example.com}} +short`

- Display the ANSWER SECTION for a given domain only:

`dig {{example.com}} +noall +answer`

- Query a specific DNS record type for a given domain:

`dig {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Fetch all DNS record types associated with the given domain:

`dig {{example.com}} any`
