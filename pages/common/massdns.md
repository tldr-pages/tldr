# massdns

> Resolve DNS records in bulk with high performance for reconnaissance.
> See also: `dig`, `dnsx`.
> More information: <https://github.com/blechschmidt/massdns#usage>.

- Resolve A records for domains in a file using specified resolvers:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{path/to/domains.txt}}`

- Resolve a specific record type and write results to a file:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-t|--type]}} {{A|AAAA|NS|MX|TXT}} {{[-w|--outfile]}} {{path/to/output.txt}} {{path/to/domains.txt}}`

- Resolve domains with simple text output format:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-o|--output]}} S {{path/to/domains.txt}}`

- Resolve domains with JSON output format:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-o|--output]}} J {{path/to/domains.txt}}`

- Resolve domains with a custom number of concurrent lookups:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-s|--hashmap-size]}} {{10000}} {{path/to/domains.txt}}`

- Resolve domains in quiet mode, suppressing status output:

`massdns {{[-r|--resolvers]}} {{path/to/resolvers.txt}} {{[-q|--quiet]}} {{path/to/domains.txt}}`
