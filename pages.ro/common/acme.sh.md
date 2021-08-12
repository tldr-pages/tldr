# acme.sh

> Shell script de implementare a protocolului client ACME, o alternativă la certbot.
> A se vedea, de asemenea, `acme.sh dns`.
> Mai multe informaţii: <https://github.com/acmesh-official/acme.sh>

- Eliberați un certificat utilizând modul webroot:

`acme.sh --issue --domain {{example.com}} --webroot {{/path/to/webroot}}`

- Eliberați un certificat pentru mai multe domenii utilizând modul independent utilizând portul 80:

`acme.sh --issue --standalone --domain {{example.com}} --domain {{www.example.com}}`

- Eliberați un certificat utilizând modul TLS independent utilizând portul 443:

`acme.sh --issue --alpn --domain {{example.com}}`

- Eliberați un certificat utilizând o configurație Nginx de lucru:

`acme.sh --issue --nginx --domain {{example.com}}`

- Eliberați un certificat utilizând o configurație Apache de lucru:

`acme.sh --issue --apache --domain {{example.com}}`

- Eliberați un certificat wildcard (\ *) utilizând un mod API DNS automat:

`acme.sh --issue --dns {{dns_cf}} --domain {{*.example.com}}`

- Instalați fișierele de certificat în locațiile specificate (utile pentru reînnoirea automată a certificatului):

`acme.sh --install-cert -d {{example.com}} --key-file {{/path/to/example.com.key}} --fullchain-file {{/path/to/example.com.cer}} --reloadcmd {{"systemctl force-reload nginx"}}`
