# acme.sh --dns

> Gebruik een DNS-01 challenge om een TLS-certificaat uit te geven.
> Meer informatie: <https://github.com/acmesh-official/acme.sh/wiki>.

- Geef een certificaat uit met behulp van een automatische DNS API-modus:

`acme.sh --issue --dns {{gnd_gd}} --domain {{voorbeeld.com}}`

- Geef een wildcardcertificaat uit (aangegeven met een asterisk) met behulp van een automatische DNS API-modus:

`acme.sh --issue --dns {{dns_namesilo}} --domain {{voorbeeld.com}} --domain {{*.voorbeeld.com}}`

- Geef een certificaat uit met behulp van een DNS-aliasmodus:

`acme.sh --issue --dns {{dns_cf}} --domain {{voorbeeld.com}} --challenge-alias {{alias-voor-voorbeeld-validatie.com}}`

- Geef een certificaat uit terwijl u automatische Cloudflare / Google DNS-polling uitschakelt nadat het DNS-record is toegevoegd door een aangepaste wachttijd in seconden op te geven:

`acme.sh --issue --dns {{dns_namecheap}} --domain {{voorbeeld.com}} --dnssleep {{300}}`

- Geef een certificaat uit met behulp van een handmatige DNS-modus:

`acme.sh --issue --dns --domain {{voorbeeld.com}} --yes-I-know-dns-manual-mode-enough-go-ahead-please`
