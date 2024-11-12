# tac

> Toon en voeg bestanden samen met regels in omgekeerde volgorde.
> Bekijk ook: `cat`.
> Meer informatie: <https://www.gnu.org/software/coreutils/tac>.

- Voeg specifieke bestanden samen in omgekeerde volgorde:

`tac {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon `stdin` in omgekeerde volgorde:

`{{cat pad/naar/bestand}} | tac`

- Gebruik een specifiek [s]cheidingsteken:

`tac -s {{scheidingsteken}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Gebruik een specifieke [r]egex als [s]cheidingsteken:

`tac -r -s {{scheidingsteken}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Gebruik een scheidingsteken vóór ([b]) elk bestand:

`tac -b {{pad/naar/bestand1 pad/naar/bestand2 ...}}`
