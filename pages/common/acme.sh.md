# acme.sh

> An ACME Shell script, an acme client alternative to certbot.
> More information: <https://github.com/acmesh-official/acme.sh>.

- Issue a certificate using webroot mode:

`acme.sh --issue --domain {{domain.tld}} --webroot {{/path/to/webroot}}`

- Issue a certificate using standalone mode using port 80:

`acme.sh --issue --standalone --domain {{domain.tld}}`

- Issue a certificate using standalone TLS mode using port 443:

`acme.sh --issue --alpn --domain {{domain.tld}}`

- Issue a certificate using a working Nginx configuration:

`acme.sh --issue --nginx --domain {{domain.tld}}`

- Issue a certificate using a working Apache configuration:

`acme.sh --issue --apache --domain {{domain.tld}}`

- Issue a wildcard (\*) certificate using a manual DNS mode:

`acme.sh --issue --dns --domain {{*.domain.tld}}`

- Issue a certificate using an automatic DNS API mode:

`acme.sh --issue --dns {{dns_api}} --domain {{domain.tld}}`

- Install certificate file into location specified by its parameter (not displayed):

`acme.sh --install-cert --domain {{domain.tld}} --reloadcmd {{reload_commad}}`
