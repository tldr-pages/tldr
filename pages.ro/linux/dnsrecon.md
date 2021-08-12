# dnsrecon

> Instrumentul de enumerare DNS.
> Mai multe informaţii: <https://github.com/darkoperator/dnsrecon>

- Scanați un domeniu și salvați rezultatele într-o bază de date SQLite:

`dnsrecon --domain {{example.com}} --db {{path/to/database.sqlite}}`

- Scanarea unui domeniu, specificarea serverului de nume și efectuarea unui transfer de zonă:

`dnsrecon --domain {{example.com}} --name_server {{nameserver.example.com}} --type axfr`

- Scanați un domeniu, folosind un atac brute-force și un dicționar de subdomenii și nume de gazdă:

`dnsrecon --domain {{example.com}} --dictionary {{path/to/dictionary.txt}} --type brt`

- Scanați un domeniu, efectuând o căutare inversă a intervalelor IP din înregistrarea SPF și salvând rezultatele într-un fișier JSON:

`dnsrecon --domain {{example.com}} -s --json`

- Scanarea unui domeniu, efectuarea unei enumerări Google și salvarea rezultatelor într-un fișier CSV:

`dnsrecon --domain {{example.com}} -g --csv`

- Scanați un domeniu, efectuând snooping cache DNS:

`dnsrecon --domain {{example.com}} --type snoop --name_server {{nameserver.example.com}} --dictionary {{path/to/dictionary.txt}}`

- Scanarea unui domeniu, efectuarea de mers pe jos zona:

`dnsrecon --domain {{example.com}} --type zonewalk`
