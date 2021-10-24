# arp

> Mostra e gestisci la cache ARP di sistema.
> Maggiori informazioni: <https://manned.org/arp>.

- Mostra la tabella ARP corrente:

`arp -a`

- Elimina l'intera cache:

`sudo arp -a -d`

- Elimina una specifica voce:

`arp -d {{indirizzo}}`

- Crea una nuova voce:

`arp -s {{indirizzo}} {{indirizzo_mac}}`
