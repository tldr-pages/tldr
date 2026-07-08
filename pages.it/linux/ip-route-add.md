# ip route add

> Aggiunge una nuova route di rete.
> Maggiori informazioni: <https://manned.org/ip-route>.

- Aggiunge una route predefinita usando l'inoltro gateway:

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}}`

- Aggiunge una route predefinita usando `ethX`:

`sudo ip {{[r|route]}} {{[a|add]}} default dev {{ethX}}`

- Aggiunge una route statica:

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} via {{gateway_ip}} dev {{ethX}}`

- Aggiunge una route a una tabella di routing specifica:

`sudo ip {{[r|route]}} {{[a|add]}} {{destination_ip}} dev {{ethX}} {{[t|table]}} {{ip_address}}`

- Forza il traffico internet attraverso un dispositivo specifico lasciando invariato il traffico locale (richiede anche la creazione di una regola):

`sudo ip {{[r|route]}} {{[a|add]}} default via {{gateway_ip}} dev {{ethX}} table {{table_id}}`
