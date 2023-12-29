# nmap

> Nmap è un tool per port scanning ed esplorazione di rete.
> Alcune funzionalità diventano attive solamente con privilegi d'amministratore.
> Maggiori informazioni: <https://nmap.org>.

- Controlla se un indirizzo IP è attivo, e indovina il suo sistema operativo:

`nmap -O {{ip_o_nome_host}}`

- Cerca di determinare se gli host specificati sono attivi e quali sono i loro nomi:

`sudo nmap -sn {{ip_o_nome_host}} {{opzionale_altro_indirizzo}}`

- Attiva scripts, segnalazione di servizi, OS fingerprinting e traceroute:

`nmap -A {{indirizzo_o_indirizzi}}`

- Scansiona una specifica lista di porte (usa `-p-` per tutte le porte `1-65535`):

`nmap -p {{porta1,porta2,…,portaN}} {{indirizzo_o_indirizzi}}`

- Determina vulnerabilità e informazioni di un host eseguendo una scansione di tutte le porte, servizi e versioni con tutti gli script di default NSE attivi:

`nmap -sC -sV {{indirizzo_o_indirizzi}}`
