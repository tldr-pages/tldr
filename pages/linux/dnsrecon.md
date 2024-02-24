# dnsrecon

> DNS enumeration tool.
> More information: <https://github.com/darkoperator/dnsrecon>.

- Scan a domain and save the results to an SQLite database:

`dnsrecon --domain {{example.com}} --db {{path/to/database.sqlite}}`

- Scan a domain, specifying the nameserver and performing a zone transfer:

`dnsrecon --domain {{example.com}} --name_server {{nameserver.example.com}} --type axfr`

- Scan a domain, using a brute-force attack and a dictionary of subdomains and hostnames:

`dnsrecon --domain {{example.com}} --dictionary {{path/to/dictionary.txt}} --type brt`

- Scan a domain, performing a reverse lookup of IP ranges from the SPF record and saving the results to a JSON file:

`dnsrecon --domain {{example.com}} -s --json`

- Scan a domain, performing a Google enumeration and saving the results to a CSV file:

`dnsrecon --domain {{example.com}} -g --csv`

- Scan a domain, performing DNS cache snooping:

`dnsrecon --domain {{example.com}} --type snoop --name_server {{nameserver.example.com}} --dictionary {{path/to/dictionary.txt}}`

- Scan a domain, performing zone walking:

`dnsrecon --domain {{example.com}} --type zonewalk`
