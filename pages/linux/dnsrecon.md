# DNSRecon

> DNS enumeration tool.
> More information: <https://github.com/darkoperator/dnsrecon>.

- Scan a domain and save the results to a SQLite database:

`dnsrecon --domain {{domain}} --db {{database}}`

- Scan a domain specifying the nameserver and performing a zone transfer:

`dnsrecon --domain {{domain}} --name_server {{nameserver}} --type axfr`

- Scan a domain using a dictionary of subdomains and hostnames for bruteforcing:

`dnsrecon --domain {{domain}} --dictionary {{dictionary}} --type brt`

- Scan a domain performing a reverse lookup of IP ranges from the SPF record and save the results to a JSON file:

`dnsrecon --domain {{domain}} -s --json`

- Scan a domain performing a Google enumeration and save the results to a CSV file:

`dnsrecon --domain {{domain}} -g --csv`

- Scan a domain performing DNS cache snooping:

`dnsrecon --domain {{domain}} --type snoop --name_server {{nameserver}} --dictionary {{dictionary}}`

- Scan a domain performing zone walking:

`dnsrecon --domain {{domain}} --type zonewalk`
