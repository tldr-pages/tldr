# prstat

> Rapporteer statistieken van actieve processen.
> Meer informatie: <https://www.unix.com/man-page/sunos/1m/prstat>.

- Bekijk alle processen en rapporteer de statistieken gesorteerd op basis van CPU-gebruik:

`prstat`

- Bekijk alle processen en rapporteer de statistieken gesorteerd op basis van geheugengebruik:

`prstat -s rss`

- Bekijk het totaal gebruik voor elke gebruiker:

`prstat -t`

- Bekijk de microstate process accounting informatie:

`prstat -m`

- Toon de 5 meest CPU intensieve processen elke seconde:

`prstat -c -n 5 -s cpu 1`
