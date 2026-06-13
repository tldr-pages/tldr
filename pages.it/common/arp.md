# arp

> Visualizza e gestisce la cache ARP di sistema.
> Maggiori informazioni: <https://manned.org/arp.8>.

- Visualizza la tabella ARP corrente:

`arp`

- Mostra output in formato [a]lternativo stile BSD con colonne fisse:

`arp -a`

- Elimina una specifica voce:

`sudo arp -d {{indirizzo}}`

- Imposta/crea una nuova voce nella tabella ARP:

`sudo arp -s {{indirizzo}} {{indirizzo_mac}}`
