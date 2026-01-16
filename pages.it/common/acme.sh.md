# acme.sh

> Script shell che implementa il protocollo client ACME, alternativa a `certbot`.
> Vedi anche: `acme.sh dns`.
> Maggiori informazioni: <https://github.com/acmesh-official/acme.sh#2-just-issue-a-cert>.

- Emetti un certificato usando la modalità webroot:

`acme.sh --issue {{[-d|--domain]}} {{example.com}} {{[-w|--webroot]}} {{/percorso/alla/webroot}}`

- Emetti un certificato per più domini usando la modalità standalone sulla porta 80:

`acme.sh --issue --standalone {{[-d|--domain]}} {{example.com}} {{[-d|--domain]}} {{www.example.com}}`

- Emetti un certificato usando la modalità standalone TLS sulla porta 443:

`acme.sh --issue --alpn {{[-d|--domain]}} {{example.com}}`

- Emetti un certificato usando una configurazione `nginx` funzionante:

`acme.sh --issue --nginx {{[-d|--domain]}} {{example.com}}`

- Emetti un certificato usando una configurazione Apache funzionante:

`acme.sh --issue --apache {{[-d|--domain]}} {{example.com}}`

- Emetti un certificato wildcard (\*) usando una modalità DNS API automatica:

`acme.sh --issue --dns {{dns_cf}} {{[-d|--domain]}} {{*.example.com}}`

- Installa i file di certificato nelle posizioni specificate (utile per il rinnovo automatico):

`acme.sh {{[-i|--install-cert]}} {{[-d|--domain]}} {{example.com}} --key-file {{/percorso/a/example.com.key}} --fullchain-file {{/percorso/a/example.com.cer}} --reloadcmd "{{systemctl force-reload nginx}}"`
