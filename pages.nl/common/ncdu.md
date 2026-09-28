# ncdu

> Schijfgebruikanalyzer met een ncurses-interface.
> Zie ook: `duf`, `df`.
> Meer informatie: <https://dev.yorhel.nl/ncdu/man>.

- Analyseer de huidige werkmap:

`ncdu`

- Kleur de uitvoer:

`ncdu --color {{dark|off}}`

- Analyseer een gegeven map:

`ncdu {{pad/naar/map}}`

- Sla resultaten op in een bestand:

`ncdu -o {{pad/naar/bestand}}`

- Sluit bestanden uit die overeenkomen met een patroon (argument kan meerdere keren gegeven worden om meer patronen toe te voegen):

`ncdu --exclude '{{*.txt}}'`
