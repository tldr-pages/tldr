# traceroute

> Gib die Route der Paketspur zu einem Netzwerk-Host aus.
> Siehe auch: `mtr`.
> Weitere Informationen: <https://manned.org/traceroute>.

- Führe einen Traceroute zu einem Host aus:

`traceroute {{host}}`

- Deaktiviere IP-Adresse und Hostname-Mapping:

`traceroute -n {{host}}`

- Spezifiziere die Wartezeit in Sekunden für die Antwort:

`traceroute {{[-w|--wait]}} {{0.5}} {{host}}`

- Spezifiziere die Anzahl der Anfragen pro Hop:

`traceroute {{[-q|--queries]}} {{5}} {{host}}`

- Spezifiziere die Größe in Bytes des Testpakets:

`traceroute {{host}} {{42}}`

- Ermittle die MTU zum Ziel:

`traceroute --mtu {{host}}`

- Verwende ICMP statt UDP für Tracerouting:

`traceroute {{[-I|--icmp]}} {{host}}`
