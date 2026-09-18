# ip maddress

> Gestisce gli indirizzi multicast.
> Maggiori informazioni: <https://manned.org/ip-maddress>.

- Elenca gli indirizzi multicast e quanti programmi vi sono iscritti:

`ip {{[m|maddress]}}`

- Elenca gli indirizzi specifici del dispositivo:

`ip {{[m|maddress]}} {{[s|show]}} dev {{ethX}}`

- Si unisce staticamente a un gruppo multicast:

`sudo ip {{[m|maddress]}} {{[a|add]}} {{33:33:00:00:00:02}} dev {{ethX}}`

- Abbandona un gruppo multicast statico:

`sudo ip {{[m|maddress]}} {{[d|delete]}} {{33:33:00:00:00:02}} dev {{ethX}}`

- Mostra aiuto:

`ip {{[m|maddress]}} {{[h|help]}}`
