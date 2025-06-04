# rcp

> Kopieer bestanden tussen lokale en externe systemen.
> Het imiteert het gedrag van het `cp`-commando, maar werkt tussen verschillende machines.
> Meer informatie: <https://www.gnu.org/software/inetutils/manual/html_node/rcp-invocation.html>.

- Kopieer een bestand naar een externe host:

`rcp {{pad/naar/local_file}} {{gebruikersnaam}}@{{remote_host}}:{{/pad/naar/bestemming/}}`

- Kopieer een directory recursief:

`rcp {{[-r|--recursive]}} {{pad/naar/local_directory}} {{gebruikersnaam}}@{{remote_host}}:{{/pad/naar/bestemming/}}`

- Behoud de bestandseigenschappen:

`rcp {{[-p|--preserve]}} {{pad/naar/local_file}} {{gebruikersnaam}}@{{remote_host}}:{{/pad/naar/bestemming/}}`

- Forceer kopiëren zonder bevestiging:

`rcp {{[-f|--from]}} {{pad/naar/local_file}} {{gebruikersnaam}}@{{remote_host}}:{{/pad/naar/bestemming/}}`
