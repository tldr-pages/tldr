# ip address

> IP Adressen Management Unterbefehl.
> Weitere Informationen: <https://manned.org/ip-address>.

- Zeige Netzwerk-Interfaces mit ihren Adressen:

`ip {{[a|address]}}`

- Zeige nur die aktiven Netzwerk-Interfaces:

`ip {{[a|address]}} show up`

- Zeige Informationen über ein bestimmtes Interface:

`ip {{[a|address]}} show dev {{eth0}}`

- Füge eine Adresse zu einem Interface hinzu:

`ip {{[a|address]}} add {{ip_adresse}} dev {{eth0}}`

- Entferne eine Adresse von einem Interface:

`ip {{[a|address]}} delete {{ip_adresse}} dev {{eth0}}`

- Entfernt alle IP Adressen in einem speziellen Bereich von einem Interface:

`ip {{[a|address]}} flush dev {{eth0}} scope {{global|host|link}}`
