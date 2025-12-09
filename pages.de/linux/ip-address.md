# ip address

> IP Adressen Management Unterbefehl.
> Weitere Informationen: <https://manned.org/ip-address>.

- Zeige Netzwerk-Interfaces mit ihren Adressen:

`ip {{[a|address]}}`

- Zeige nur die aktiven Netzwerk-Interfaces:

`ip {{[a|address]}} {{[s|show]}} up`

- Zeige Informationen über ein bestimmtes Interface:

`ip {{[a|address]}} {{[s|show]}} {{eth0}}`

- Füge eine Adresse zu einem Interface hinzu:

`sudo ip {{[a|address]}} {{[a|add]}} {{ip_adresse}} dev {{eth0}}`

- Entferne eine Adresse von einem Interface:

`sudo ip {{[a|address]}} {{[d|delete]}} {{ip_adresse}} dev {{eth0}}`

- Entfernt alle IP Adressen in einem speziellen Bereich von einem Interface:

`sudo ip {{[a|address]}} {{[f|flush]}} {{eth0}} scope {{global|host|link}}`
