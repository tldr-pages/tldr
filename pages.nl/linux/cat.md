# cat

> Print en concateneer bestanden.
> Zie ook: `bat`.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- Print de inhoud van een bestand naar `stdout`:

`cat {{pad/naar/bestand}}`

- Concateneer meerdere bestanden in een uitvoerbestand:

`cat {{pad/naar/bestand1 pad/naar/bestand2 ...}} > {{pad/naar/uitvoerbestand}}`

- Voeg meerdere bestanden toe aan een uitvoerbestand:

`cat {{pad/naar/bestand1 pad/naar/bestand2 ...}} >> {{pad/naar/uitvoerbestand}}`

- Schrijf interactief naar een bestand:

`cat > {{pad/naar/bestand}}`

- Nummer alle uitvoerregels:

`cat {{[-n|--number]}} {{pad/naar/bestand}}`

- Toon alle tekens, inclusief tabtekens, regeleindes en niet-afdrukbare tekens:

`cat {{[-A|--show-all]}} {{pad/naar/bestand}}`

- Sla herhaalde lege regels over:

`cat {{[-s|--squeeze-blank]}} {{pad/naar/bestand}}`

- Geef de inhoud van een bestand door aan een ander programma via `stdin`:

`cat {{pad/naar/bestand}} | {{programma}}`
