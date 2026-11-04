# lsof

> Toon open bestanden en de bijbehorende processen.
> Opmerking: rootrechten zijn vereist om bestanden te tonen die door anderen zijn geopend.
> Meer informatie: <https://manned.org/lsof>.

- Zoek de processen die een gegeven bestand open hebben staan:

`lsof {{pad/naar/bestand}}`

- Zoek het proces dat een lokale internetpoort heeft geopend:

`lsof -i :{{poort}}`

- Toon alleen het proces-ID (PID):

`lsof -t {{pad/naar/bestand}}`

- Toon bestanden geopend door de gegeven gebruiker:

`lsof -u {{gebruikersnaam}}`

- Toon bestanden geopend door het gegeven commando of proces:

`lsof -c {{proces_of_commando_naam}}`

- Toon bestanden geopend door een specifiek proces, gegeven zijn PID:

`lsof -p {{proces_id}}`

- Toon open bestanden in een map:

`lsof +D {{pad/naar/map}}`

- Zoek het proces dat luistert op een lokale IPv6 TCP-poort en converteer geen netwerk- of poortnummers:

`lsof -i6TCP:{{poort}} -sTCP:LISTEN -n -P`
