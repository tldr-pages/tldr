# clamdscan

> Een command-line virus scanner die gebruik maakt van de ClamAV Daemon.
> Meer informatie: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- Scan een bestand of map op kwetsbaarheden:

`clamdscan {{pad/naar/bestand_of_map}}`

- Scan data van `stdin`:

`{{commando}} | clamdscan -`

- Scan de huidige map en toon alleen geïnfecteerde bestanden:

`clamdscan --infected`

- Sla het scan rapport op in een log bestand:

`clamdscan --log {{pad/naar/log_bestand}}`

- Verplaats geïnfecteerde bestanden naar een specifieke map:

`clamdscan --move {{pad/naar/quarantaine_map}}`

- Verwijder geïnfecteerde bestanden:

`clamdscan --remove`

- Gebruik meerdere threads voor het scannen van een map:

`clamdscan --multiscan`

- Geef de bestandsdescriptor door in plaats van het bestand naar de daemon:

`clamdscan --fdpass`
