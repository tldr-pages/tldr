# dnsrecon

> DNS enumeration tool.
> More information: <https://manned.org/dnsrecon>.

- Scan a domain and save the results to an SQLite database:

`dnsrecon {{[-d|--domain]}} {{example.com}} --db {{path/to/database.sqlite}}`

- Scan a domain, specifying the nameserver and performing a zone transfer:

`dnsrecon {{[-d|--domain]}} {{example.com}} {{[-n|--name_server]}} {{nameserver.example.com}} {{[-t|--type]}} axfr`

- Scan a domain, using a brute-force attack and a dictionary of subdomains and hostnames:

`dnsrecon {{[-d|--domain]}} {{example.com}} {{[-D|--dictionary]}} {{path/to/dictionary.txt}} {{[-t|--type]}} brt`

- Scan a domain, performing a reverse lookup of IP ranges from the SPF record and saving the results to a JSON file:

`dnsrecon {{[-d|--domain]}} {{example.com}} -s {{[-j|--json]}}`

- Scan a domain, performing a Google enumeration and saving the results to a CSV file:

`dnsrecon {{[-d|--domain]}} {{example.com}} -g {{[-c|--csv]}}`

- Scan a domain, performing DNS cache snooping:

`dnsrecon {{[-d|--domain]}} {{example.com}} {{[-t|--type]}} snoop {{[-n|--name_server]}} {{nameserver.example.com}} {{[-D|--dictionary]}} {{path/to/dictionary.txt}}`

- Scan a domain, performing zone walking:

`dnsrecon {{[-d|--domain]}} {{example.com}} {{[-t|--type]}} zonewalk`
