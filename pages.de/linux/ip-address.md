# ip address

> IP Adressen Management Unterbefehl.
> Weitere Informationen: <https://manned.org/ip-address>.

- Zeige Netzwerk-Interfaces mit ihren Adressen:

`ip address`

- Zeige nur die aktiven Netzwerk-Interfaces:

`ip address show up`

- Zeige Informationen über ein bestimmtes Interface:

`ip address show dev {{eth0}}`

- Füge eine Adresse zu einem Interface hinzu:

`ip address add {{ip_adresse}} dev {{eth0}}`

- Entferne eine Adresse von einem Interface:

`ip address delete {{ip_adresse}} dev {{eth0}}`

- Entfernt alle IP Adressen in einem speziellen Bereich von einem Interface:

`ip address flush dev {{eth0}} scope {{global|host|link}}`
