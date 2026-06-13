# clamscan

> Een command-line virus scanner.
> Meer informatie: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Scan een bestand op kwetsbaarheden:

`clamscan {{pad/naar/bestand}}`

- Scan alle bestanden recursief in een specifieke map:

`clamscan {{[-r|--recursive]}} {{pad/naar/map}}`

- Scan data van `stdin`:

`{{commando}} | clamscan -`

- Specificeer een virus database bestand of map van bestanden:

`clamscan {{[-d|--database]}} {{pad/naar/database_bestand_of_map}}`

- Scan de huidige map en toon alleen geïnfecteerde bestanden:

`clamscan {{[-i|--infected]}}`

- Sla het scan rapport op in een log bestand:

`clamscan {{[-l|--log]}} {{pad/naar/log_bestand}}`

- Verplaats geïnfecteerde bestanden naar een specifieke map:

`clamscan --move {{pad/naar/quarantine_map}}`

- Verwijder geïnfecteerde bestanden:

`clamscan --remove yes`
