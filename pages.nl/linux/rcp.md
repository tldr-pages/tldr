# rcp

> Kopieer bestanden tussen lokale en externe systemen.
> Het imiteert het gedrag van het `cp`-commando, maar werkt tussen verschillende machines.
> Meer informatie: <https://www.gnu.org/software/inetutils/manual/inetutils.html#rcp-invocation>.

- Kopieer een bestand naar een externe host:

`rcp {{pad/naar/lokaal_bestand}} {{gebruikersnaam}}@{{remote_host}}:/{{pad/naar/bestemming}}/`

- Kopieer een directory recursief:

`rcp {{[-r|--recursive]}} {{pad/naar/lokale_map}} {{gebruikersnaam}}@{{remote_host}}:/{{pad/naar/bestemming}}/`

- Behoud de bestandseigenschappen:

`rcp {{[-p|--preserve]}} {{pad/naar/lokaal_bestand}} {{gebruikersnaam}}@{{remote_host}}:/{{pad/naar/bestemming}}/`

- Forceer kopiëren zonder bevestiging:

`rcp {{[-f|--from]}} {{pad/naar/lokaal_bestand}} {{gebruikersnaam}}@{{remote_host}}:/{{pad/naar/bestemming}}/`
