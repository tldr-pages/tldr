# arping

> Mit dem ARP Protokoll Hosts in einem Netzwerk entdecken und untersuchen.
> Nützlich für die Entdeckung von MAC-Adressen.
> Weitere Informationen: <https://github.com/ThomasHabets/arping>.

- Pinge einen Host mit ARP Request Paketen:

`arping {{host_adresse}`

- Pinge einen Host auf einem spezifizierten Interface:

`arping -I {{interface}} {{host_adresse}}`

- Einen Host pungen und nach der ersten Antwort aufhören:

`arping -f {{host_adresse}}`

- Einen Host für eine bestimmte Anzahl pingen:

`arping -c {{Anzahl}} {{host_adresse}}`

- ARP Request Packete broadcasten um die ARP Caches der Nachbarn zu aktualisieren:

`arping -U {{broadcast_adresse}}`

- ARP Requests mit einem 3 Sekunden Timeout senden um duplizierte IP-Adressen im Netzwerk zu erkennen.

`arping -D -w {{3}} {{adresse_zum_checken}}`
