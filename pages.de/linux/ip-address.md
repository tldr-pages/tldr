# ip address

> IP Adressen Management Sub-Befehl.

- Zeigt Netzwerk Interfaces mit ihren Adressen:

`ip address`

- Zeigt nur die aktiven Netzwerk Interfaces:

`ip address show up`

- Zeigt Informationen über ein spezielles Interface:

`ip address show dev {{eth0}}`

- Fügt eine Adresse zu einem Interface hinzu:

`ip address add {{ip_adresse}} dev {{eth0}}`

- Entfernt eine Adresse von einem Interface:

`ip address delete {{ip_adresse}} dev {{eth0}}`

- Entfernt alle IP Adressen in einem speziellen Bereich von einem Interface:

`ip address flush dev {{eth0}} scope {{global|host|link}}`
