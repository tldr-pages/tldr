# ip

> Mostra / manipola routing, dispositivi, criteri di routing e tunnel.
> Alcuni sottocomandi, come `ip address`, hanno una propria documentazione d'uso. Maggiori informazioni: <https://www.man7.org/linux/man-pages/man8/ip.8.html>

- Lista delle interfacce con informazioni dettagliate:

`ip address`

- Lista delle interfacce con informazioni brevi sul livello di rete:

`ip -brief address`

- Lista delle interfacce con informazioni brevi sul livello di collegamento:

`ip -brief link`

- Visualizza la tabella di routing:

`ip route`

- Mostra i vicini (tabella ARP):

`ip neighbour`

- Attiva/disattiva un'interfaccia:

`ip link set {{interfaccia}} up/down`

- Aggiungere/eliminare un indirizzo ip a un'interfaccia:

`ip addr add/del {{ip}}/{{mask}} dev {{interfaccia}}`

- Aggiungi una route predefinita:

`ip route add default via {{ip}} dev {{interfaccia}}`
