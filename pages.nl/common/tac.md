# tac

> Toon en voeg bestanden samen met regels in omgekeerde volgorde.
> Zie ook: `cat`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/tac-invocation.html>.

- Voeg specifieke bestanden samen in omgekeerde volgorde:

`tac {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Toon `stdin` in omgekeerde volgorde:

`{{cat pad/naar/bestand}} | tac`

- Gebruik een specifiek scheidingsteken:

`tac {{[-s|--separator]}} {{scheidingsteken}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Gebruik een specifieke regex als scheidingsteken:

`tac {{[-r|--regex]}} {{[-s|--separator]}} {{scheidingsteken}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`

- Gebruik een scheidingsteken vóór elk bestand:

`tac {{[-b|--before]}} {{pad/naar/bestand1 pad/naar/bestand2 ...}}`
