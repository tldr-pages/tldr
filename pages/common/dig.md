# dig

> DNS Lookup utility.
> More information: <https://manpages.debian.org/dnsutils/dig.1.html>.

- Lookup the IP(s) associated with a hostname (A records):

`dig +short {{example.com}}`

- Get a detailed answer for a given domain (A records):

`dig +noall +answer {{example.com}}`

- Query a specific DNS record type associated with a given domain name:

`dig +short {{example.com}} {{A|MX|TXT|CNAME|NS}}`

- Get all types of records for a given domain name:

`dig {{example.com}} ANY`

- Specify an alternate DNS server to query:

`dig @{{8.8.8.8}} {{example.com}}`

- Perform a reverse DNS lookup on an IP address (PTR record):

`dig -x {{8.8.8.8}}`

- Find authoritative name servers for the zone and display SOA records:

`dig +nssearch {{example.com}}`

- Perform iterative queries and display the entire trace path to resolve a domain name:

`dig +trace {{example.com}}`
