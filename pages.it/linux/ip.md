# ip

> Mostra / manipola routing, dispositivi, criteri di routing e tunnel.
> Alcuni sottocomandi, come `address`, hanno una propria documentazione d'uso.
> Maggiori informazioni: <https://manned.org/ip.8>.

- Elenca le interfacce con informazioni dettagliate:

`ip {{[a|address]}}`

- Elenca le interfacce con informazioni brevi sul livello di rete:

`ip {{[-br a|-brief address]}}`

- Elenca le interfacce con informazioni brevi sul livello di collegamento:

`ip {{[-br l|-brief link]}}`

- Visualizza la tabella di routing:

`ip {{[r|route]}}`

- Mostra i vicini (tabella ARP):

`ip {{[n|neighbour]}}`

- Attiva/disattiva un'interfaccia:

`sudo ip {{[l|link]}} {{[s|set]}} {{interfaccia}} {{up|down}}`

- Aggiungi/elimina un indirizzo IP a/da un'interfaccia:

`sudo ip {{[a|address]}} {{add|delete}} {{ip}}/{{mask}} dev {{interfaccia}}`

- Aggiungi una route predefinita:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip}} dev {{interfaccia}}`
