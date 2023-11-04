# prstat

> Rapportering van de statistieken van actieve processen.
> Meer informatie: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Bekijken alle processen en rapporteer de statieken gestoord op basis van CPU gebruik:

`prstat`

- Bekijken alle processen en rapporteer de statieken gestoord op basis van geheugen gebruik:

`prstat -s rss`

- Bekijk het totaal gebruik voor elke gebruiker:

`prstat -t`

- Bekijk de microstate process accounting informatie:

`prstat -m`

- Print de 5 meest CPU intensieve processen elke seconde:

`prstat -c -n {{5}} -s cpu {{1}}`
