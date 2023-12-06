# acme.sh

> Shell-script dat het ACME-clientprotocol implementeert, een alternatief voor `certbot`.
> Zie ook `acme.sh dns`.
> Meer informatie: <https://github.com/acmesh-official/acme.sh>.

- Geef een certificaat uit met behulp van de webroot-modus:

`acme.sh --issue --domain {{voorbeeld.com}} --webroot {{/pad/naar/webroot}}`

- Geef een certificaat uit voor meerdere domeinen in de zelfstandige modus met poort 80:

`acme.sh --issue --standalone --domain {{voorbeeld.com}} --domain {{www.voorbeeld.com}}`

- Geef een certificaat uit met behulp van de zelfstandige TLS-modus met behulp van poort 443:

`acme.sh --issue --alpn --domain {{voorbeeld.com}}`

- Geef een certificaat uit met een werkende Nginx-configuratie:

`acme.sh --issue --nginx --domain {{voorbeeld.com}}`

- Geef een certificaat uit met een werkende Apache-configuratie:

`acme.sh --issue --apache --domain {{voorbeeld.com}}`

- Geef een wildcardcertificaat (\*) uit met behulp van een automatische DNS API-modus:

`acme.sh --issue --dns {{dns_cf}} --domain {{*.voorbeeld.com}}`

- Installeer certificaatbestanden op de opgegeven locaties (handig voor automatische certificaatvernieuwing):

`acme.sh --install-cert -d {{voorbeeld.com}} --key-file {{/pad/naar/voorbeeld.com.key}} --fullchain-file {{/pad/naar/voorbeeld.com.cer}} --reloadcmd {{"systemctl force-reload nginx"}}`
