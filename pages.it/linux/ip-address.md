# ip address

> Sottocomando di gestione degli indirizzi IP.
> Maggiori informazioni: <https://manned.org/ip-address>.

- Elenca le interfacce di rete e i loro indirizzi IP associati:

`ip {{[a|address]}}`

- Filtra per mostrare solo le interfacce di rete attive:

`ip {{[a|address]}} {{[s|show]}} up`

- Mostra informazioni su un'interfaccia di rete specifica:

`ip {{[a|address]}} {{[s|show]}} {{ethX}}`

- Aggiunge un indirizzo IP a un'interfaccia di rete:

`sudo ip {{[a|address]}} {{[a|add]}} {{ip_address}} dev {{ethX}}`

- Rimuove un indirizzo IP da un'interfaccia di rete:

`sudo ip {{[a|address]}} {{[d|delete]}} {{ip_address}} dev {{ethX}}`

- Elimina tutti gli indirizzi IP in un dato ambito da un'interfaccia di rete:

`sudo ip {{[a|address]}} {{[f|flush]}} {{ethX}} scope {{global|host|link}}`
