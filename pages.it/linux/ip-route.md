# ip route

> Sottocomando di gestione della tabella di routing IP.
> Vedi anche: `routel`.
> Maggiori informazioni: <https://manned.org/ip-route>.

- Mostra la tabella di routing `main`:

`ip {{[r|route]}}`

- Aggiunge una route predefinita usando l'inoltro gateway:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{ip_gateway}}`

- Aggiunge una route predefinita usando `ethX`:

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{ethX}}`

- Aggiunge una route statica:

`sudo ip {{[r|route]}} {{[a|add]}} {{ip_destinazione}} via {{ip_gateway}} dev {{ethX}}`

- Elimina una route statica:

`sudo ip {{[r|route]}} {{[d|delete]}} {{ip_destinazione}} dev {{ethX}}`

- Modifica o sostituisce una route statica:

`sudo ip {{[r|route]}} {{change|replace}} {{ip_destinazione}} via {{ip_gateway}} dev {{ethX}}`

- Mostra quale route verrà usata dal kernel per raggiungere un indirizzo IP:

`ip {{[r|route]}} {{[g|get]}} {{ip_destinazione}}`

- Mostra una tabella di routing specifica:

`ip {{[r|route]}} {{[l|list]}} {{[t|table]}} {{numero_table}}`
