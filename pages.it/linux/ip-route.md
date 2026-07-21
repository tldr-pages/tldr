# ip route

> Sottocomando di gestione della tabella di routing IP.
> Vedi anche: `routel`.
> Maggiori informazioni: <https://manned.org/ip-route>.

- Mostra la tabella di routing `main`:

`ip {{[r|route]}}`

- Aggiunge una route predefinita usando l'inoltro gateway:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}}`

- Aggiunge una route predefinita usando `ethX`:

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{ethX}}`

- Aggiunge una route statica:

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} via {{gateway_ip}} dev {{ethX}}`

- Elimina una route statica:

`sudo ip {{[r|route]}} {{[d|delete]}} {{destination_ip}} dev {{ethX}}`

- Modifica o sostituisce una route statica:

`sudo ip {{[r|route]}} {{change|replace}} {{destination_ip}} via {{gateway_ip}} dev {{ethX}}`

- Mostra quale route verrà usata dal kernel per raggiungere un indirizzo IP:

`ip {{[r|route]}} {{[g|get]}} {{destination_ip}}`

- Mostra una tabella di routing specifica:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{table_number}}`
