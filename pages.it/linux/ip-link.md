# ip link

> Gestisce le interfacce di rete.
> Maggiori informazioni: <https://manned.org/ip-link>.

- Mostra informazioni su tutte le interfacce di rete:

`ip {{[l|link]}}`

- Mostra informazioni su un'interfaccia di rete specifica:

`ip {{[l|link]}} {{[sh|show]}} {{ethX}}`

- Attiva o disattiva un'interfaccia di rete:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{up|down}}`

- Assegna un nome significativo a un'interfaccia di rete:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{[al|alias]}} "{{LAN Interface}}"`

- Cambia l'indirizzo MAC di un'interfaccia di rete:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} {{[a|address]}} {{ff:ff:ff:ff:ff:ff}}`

- Cambia la dimensione MTU per un'interfaccia di rete per usare jumbo frame:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} mtu {{9000}}`

- Imposta lo stato della modalità promiscua di un dispositivo:

`sudo ip {{[l|link]}} {{[s|set]}} {{ethX}} promisc {{on|off}}`

- Elimina un dispositivo:

`sudo ip {{[l|link]}} {{[d|delete]}} {{ethX}}`
