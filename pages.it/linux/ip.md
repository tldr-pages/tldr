# ip

> Mostra / manipola routing, dispositivi, criteri di routing e tunnel.
> Alcuni sottocomandi, come `ip {{[a|address]}}ess`, hanno una propria documentazione d'uso.
> Maggiori informazioni: <https://www.manned.org/ip.8>.

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

`ip {{[l|link]}} set {{interfaccia}} {{up|down}}`

- Aggiungi/elimina un indirizzo IP a/da un'interfaccia:

`ip {{[a|address]}} add/del {{ip}}/{{mask}} dev {{interfaccia}}`

- Aggiungi una route predefinita:

`ip {{[r|route]}} add default via {{ip}} dev {{interfaccia}}`
