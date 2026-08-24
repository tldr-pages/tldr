# arping

> Mit dem ARP Protokoll Hosts in einem Netzwerk entdecken und untersuchen.
> Nützlich für die Entdeckung von MAC-Adressen.
> Weitere Informationen: <https://manned.org/arping>.

- Pinge einen Host mit ARP Request Paketen:

`sudo arping {{host_adresse}}`

- Pinge einen Host auf einem spezifizierten Interface:

`sudo arping -I {{interface}} {{host_adresse}}`

- Pinge einen Host und höre nach der ersten Antwort auf:

`sudo arping -f {{host_adresse}}`

- Pinge einen Host für eine bestimmte Anzahl:

`sudo arping -c {{anzahl}} {{host_adresse}}`

- Broadcaste ARP Request Pakete um die ARP Caches der Nachbarn zu aktualisieren:

`sudo arping -U {{broadcast_adresse}}`

- Sende ARP Requests mit einem 3 Sekunden Timeout um duplizierte IP-Adressen im Netzwerk zu erkennen:

`sudo arping -D -w {{3}} {{adresse_zum_checken}}`
