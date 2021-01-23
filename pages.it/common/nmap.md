# nmap

> Nmap è un tool per port scanning ed esplorazione di rete.
> Alcune funzionalità diventano attive solamente con privilegi d'amministratore.
> Maggiori informazioni: <https://nmap.org>.

- Controlla se un indirizzo IP è attivo, e indovina il suo sistema operativo:

`nmap -O {{ip_o_nome_host}}`

- Cerca di determinare se gli host specificati sono attivi e quali sono i loro nomi:

`nmap -sn {{ip_o_nome_host}} {{opzionale_altro_indirizzo}}`

- Come sopra, ma esegui una scansione della porta TCP predefinita 1000 se l'host sembra attivo:

`nmap {{ip_o_nome_host}} {{opzionale_altro_indirizzo}}`

- Attiva scripts, segnalazione di servizi, OS fingerprinting e traceroute:

`nmap -A {{indirizzo_o_indirizzi}}`

- Velocizza esecuzione dando per scontato una buona connessione di rete:

`nmap -T4 {{indirizzo_o_indirizzi}}`

- Scansiona una specifica lista di porte (usa -p- per tutte le porte 1-65535):

`nmap -p {{porta1,porta2,…,portaN}} {{indirizzo_o_indirizzi}}`

- Esegui scansione TCP e UDP (usa -sU per usare solo UDP, -sZ per SCTP, -sO per IP):

`nmap -sSU {{indirizzo_o_indirizzi}}`

- Esegui una scansione di cifratori TLS verso un host per individuarne i cifratori supportati e i protocolli SSL/TLS:

`nmap --script ssl-enum-ciphers {{indirizzo_o_indirizzi}} -p 443`

- Determina vulnerabilità e informazioni di un host eseguendo una scansione di tutte le porte, servizi e versioni con tutti gli script di default NSE attivi:

`nmap -sC -sV {{indirizzo_o_indirizzi}}`
