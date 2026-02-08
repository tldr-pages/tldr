# dig

> DNS-Lookup-Werkzeug.
> Weitere Informationen: <https://manned.org/dig>.

- Suche die IP(s) eines Hostnamens (A-Records):

`dig +short {{host}}`

- Erhalte eine detaillierte Antwort für eine Domäne (A-Records):

`dig +noall +answer {{host}}`

- Frage einen bestimmten DNS-Record-Typ für einen angegebenen Domainnamen ab:

`dig +short {{host}} {{A|MX|TXT|CNAME|NS}}`

- Spezifiziere einen alternativen DNS-Server, der abgefragt werden soll, und verwende optional DNS over TLS (DoT):

`dig {{+tls}} @{{1.1.1.1|8.8.8.8|9.9.9.9|...}} {{host}}`

- Führe einen umgekehrten DNS-Lookup auf einer IP-Adresse aus (PTR-Record):

`dig -x {{ip_adresse}}`

- Finde autoritative Nameserver für die Zone und zeige SOA-Records:

`dig +nssearch {{host}}`

- Führe iterative Abfragen aus und zeige den gesamten Trace-Pfad, um einen Domainnamen aufzulösen:

`dig +trace {{host}}`

- Frage einen DNS-Server über einen nicht-standardmäßigen [p]ort mit dem TCP-Protokoll ab:

`dig +tcp -p {{port}} @{{dns_server_ip}} {{host}}`
