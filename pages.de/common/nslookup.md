# nslookup

> Frage Nameserver nach verschiedenen Domain-Records.
> Weitere Informationen: <https://manned.org/nslookup>.

- Frage den Standard-Nameserver des Systems nach einer IP-Adresse (A-Record) der Domain:

`nslookup {{domain}}`

- Frage einen bestimmten Nameserver nach einem NS-Record der Domain:

`nslookup -type=NS {{domain}} {{dns_server}}`

- Frage nach einem Reverse-Lookup (PTR-Record) einer IP-Adresse:

`nslookup -type=PTR {{ip_adresse}}`

- Frage nach allen verfügbaren Records mit TCP-Protokoll:

`nslookup -vc -type=ANY {{domain}}`

- Frage einen bestimmten Nameserver nach der gesamten Zone-Datei (Zone Transfer) der Domain mit TCP-Protokoll:

`nslookup -vc -type=AXFR {{domain}} {{name_server}}`

- Frage nach einem Mailserver (MX-Record) der Domain und zeige Details der Transaktion:

`nslookup -type=MX -debug {{domain}}`

- Frage einen bestimmten Nameserver auf einem bestimmten Port nach einem TXT-Record der Domain:

`nslookup -port={{port_nummer}} -type=TXT {{domain}} {{name_server}}`
