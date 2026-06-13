# amass intel

> Raccoglie informazioni open source su un’organizzazione, come domini radice e ASNs.
> Maggiori informazioni: <https://github.com/owasp-amass/amass/blob/master/doc/user_guide.md#the-intel-subcommand>.

- Trova i domini radice in un intervallo di indirizzi IP:

`amass intel -addr {{192.168.0.1-254}}`

- Usa metodi di ricognizione attiva:

`amass intel -active -addr {{192.168.0.1-254}}`

- Trova i domini radice associati a un [d]ominio:

`amass intel -whois -d {{nome_dom}}`

- Trova gli ASNs appartenenti a un’[org]anizzazione:

`amass intel -org {{nome_org}}`

- Trova i domini radice appartenenti a un dato Autonomous System Number:

`amass intel -asn {{asn}}`

- Salva i risultati in un file di testo:

`amass intel -o {{percorso/del/file_output}} -whois -d {{nome_dom}}`

- Elenca tutte le fonti dati disponibili:

`amass intel -list`
