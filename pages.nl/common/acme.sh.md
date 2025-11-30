# acme.sh

> Shell-script dat het ACME-clientprotocol implementeert, een alternatief voor `certbot`.
> Zie ook: `acme.sh dns`.
> Meer informatie: <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>.

- Geef een certificaat uit met behulp van de webroot-modus:

`acme.sh --issue {{[-d|--domain]}} {{example.com}} {{[-w|--webroot]}} /{{pad/naar/webroot}}`

- Geef een certificaat uit voor meerdere domeinen in de zelfstandige modus met poort 80:

`acme.sh --issue --standalone {{[-d|--domain]}} {{example.com}} {{[-d|--domain]}} {{www.example.com}}`

- Geef een certificaat uit met behulp van de zelfstandige TLS-modus met behulp van poort 443:

`acme.sh --issue --alpn {{[-d|--domain]}} {{example.com}}`

- Geef een certificaat uit met een werkende Nginx-configuratie:

`acme.sh --issue --nginx {{[-d|--domain]}} {{example.com}}`

- Geef een certificaat uit met een werkende Apache-configuratie:

`acme.sh --issue --apache {{[-d|--domain]}} {{example.com}}`

- Geef een wildcardcertificaat (\*) uit met behulp van een automatische DNS API-modus:

`acme.sh --issue --dns {{dns_cf}} {{[-d|--domain]}} {{*.example.com}}`

- Installeer certificaatbestanden op de opgegeven locaties (handig voor automatische certificaatvernieuwing):

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{example.com}} --key-file /{{pad/naar/example.com.key}} --fullchain-file /{{pad/naar/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
