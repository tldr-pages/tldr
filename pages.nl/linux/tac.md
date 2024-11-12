# tac

> Toon en voeg bestanden samen met regels in omgekeerde volgorde.
> Bekijk ook: `cat`.
> Meer informatie: <https://www.gnu.org/software/coreutils/tac>.

- Voeg specifieke bestanden samen in omgekeerde volgorde:

`tac {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon `stdin` in omgekeerde volgorde:

`{{cat pad/naar/bestand}} | tac`

- Gebruik een specifiek scheidingsteken:

`tac --separator {{,}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Gebruik een specifieke regex als scheidingsteken:

`tac --regex --separator {{[,;]}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Gebruik een scheidingsteken vóór elk bestand:

`tac --before {{pad/naar/bestand1 pad/naar/bestand2 ...}}`
