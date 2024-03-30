# arping

> Mit dem ARP Protokoll Hosts in einem Netzwerk entdecken und untersuchen.
> Nützlich für die Entdeckung von MAC-Adressen.
> Weitere Informationen: <https://github.com/ThomasHabets/arping>.

- Pinge einen Host mit ARP Request Paketen:

`arping {{host_adresse}}`

- Pinge einen Host auf einem spezifizierten Interface:

`arping -I {{interface}} {{host_adresse}}`

- Pinge einen Host und höre nach der ersten Antwort auf:

`arping -f {{host_adresse}}`

- Pinge einen Host für eine bestimmte Anzahl:

`arping -c {{anzahl}} {{host_adresse}}`

- Broadcaste ARP Request Pakete um die ARP Caches der Nachbarn zu aktualisieren:

`arping -U {{broadcast_adresse}}`

- Sende ARP Requests mit einem 3 Sekunden Timeout um duplizierte IP-Adressen im Netzwerk zu erkennen:

`arping -D -w {{3}} {{adresse_zum_checken}}`
