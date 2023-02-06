# acme.sh

> Az ACME kliens protokollt megvalósító Shell szkript, a certbot alternatívája. Lásd még: `acme.sh dns`. További információ: <https://github.com/acmesh-official/acme.sh>.

- Tanúsítvány kiállítása webroot módban:

`acme.sh --issue --domain {{example.com}} --webroot {{/path/to/webroot}}`

- Tanúsítvány kiállítása több tartományhoz önálló módban, a 80-as porton keresztül:

`acme.sh --issue --standalone --domain {{example.com}} --domain {{www.example.com}}`

- Tanúsítvány kiállítása önálló TLS módban, a 443-as portot használva:

`acme.sh --issue --alpn --domain {{example.com}}`

- Tanúsítvány kiállítása működő Nginx konfigurációval:

`acme.sh --issue --nginx --domain {{example.com}}`

- Tanúsítvány kiállítása működő Apache konfigurációval:

`acme.sh --issue --apache --domain {{example.com}}`

- Automatikus DNS API módban kiállított helyettesítő (\*) tanúsítvány:

`acme.sh --issue --dns {{dns_cf}} --domain {{*.example.com}}`

- Tanúsítványfájlok telepítése a megadott helyekre (hasznos a tanúsítvány automatikus megújításához):

`acme.sh --install-cert -d {{example.com}} --key-file {{/path/to/example.com.key}} --fullchain-file {{/path/to/example.com.cer}} --reloadcmd {{"systemctl force-reload nginx"}}`
