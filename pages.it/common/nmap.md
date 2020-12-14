# nmap

> Nmap è un tool per port scanning ed esplorazione di rete.
> Alcune funzionalità diventano attive solamente con privilegi d'amministratore.
> Ulteriori informazioni: <https://nmap.org>.

- Controlla se un indirizzo IP è attivo, e indovina il suo sistema operativo:

`nmap -O {{ip_or_hostname}}`

- Cerca di determinare se gli hosts specificati sono attivi e quali sono i loro nomi:

`nmap -sn {{ip_or_hostname}} {{optional_another_address}}`

- Come sopra, ma esegui una scansione default 1000-port TCP se l'host sembra attivo:

`nmap {{ip_or_hostname}} {{optional_another_address}}`

- Attiva scripts, segnalazione di servizi, OS fingerprinting e traceroute:

`nmap -A {{address_or_addresses}}`

- Velocizza esecuzione dando per scontato una buona connessione di rete:

`nmap -T4 {{address_or_addresses}}`

- Scansiona una specifica lista di porte (usa -p- per tutte le porte 1-65535):

`nmap -p {{port1,port2,…,portN}} {{address_or_addresses}}`

- Esegui scansione TCP e UDP (usa -sU per usare solo UDP, -sZ per SCTP, -sO per IP):

`nmap -sSU {{address_or_addresses}}`

- Esegui una scansione di cifratori TLS verso un host sul quale bisogna individuare i cifratori supportati e i protocolli SSL/TLS:

`nmap --script ssl-enum-ciphers {{address_or_addresses}} -p 443`

- Esegui scansione di tutte le porte, servizi e versioni con tutti gli script di default NSE attivi verso un host per determinarne vulnerabilità e informazioni:

`nmap -sC -sV {{address_or_addresses}}`
