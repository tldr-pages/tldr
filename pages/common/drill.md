# drill

> Perform various DNS queries.

- Lookup the IP(s) associated with a hostname (A records):

`drill {{hostname.com}}`

- Lookup the mail server(s) associated with a given domain name (MX record):

`drill mx {{hostname.com}}`

- Get all types of records for a given domain name:

`drill any {{hostname.com}}`

- Specify an alternate DNS server to query:

`drill {{hostname.com}} @{{8.8.8.8}}`

- Perform a reverse DNS lookup on an IP address (PTR record):

`drill -x {{8.8.8.8}}`

- Perform DNSSEC trace from root servers down to a domain name:

`drill -TD {{hostname.com}}`

- Show DNSKEY record(s) for a domain name:

`drill -s dnskey {{hostname.com}}`
