# ip

> Mostra / manipola routing, dispositivi, criteri di routing e tunnel.
> Alcuni sottocomandi, come `ip address`, hanno una propria documentazione d'uso.
> Maggiori informazioni: <https://www.man7.org/linux/man-pages/man8/ip.8.html>.

- Elenca le interfacce con informazioni dettagliate:

`ip address`

- Elenca le interfacce con informazioni brevi sul livello di rete:

`ip -brief address`

- Elenca le interfacce con informazioni brevi sul livello di collegamento:

`ip -brief link`

- Visualizza la tabella di routing:

`ip route`

- Mostra i vicini (tabella ARP):

`ip neighbour`

- Attiva/disattiva un'interfaccia:

`ip link set {{interfaccia}} up/down`

- Aggiungi/elimina un indirizzo IP a/da un'interfaccia:

`ip addr add/del {{ip}}/{{mask}} dev {{interfaccia}}`

- Aggiungi una route predefinita:

`ip route add default via {{ip}} dev {{interfaccia}}`
