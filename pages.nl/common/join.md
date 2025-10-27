# join

> Voeg regels van twee gesorteerde bestanden samen op een gemeenschappelijk veld.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/join-invocation.html>.

- Voeg twee bestanden samen op het eerste (standaard) veld:

`join {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Voeg twee bestanden samen met een komma (in plaats van een spatie) als veldscheidingsteken:

`join -t ',' {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Voeg veld 3 van bestand 1 samen met veld 1 van bestand 2:

`join -1 {{3}} -2 {{1}} {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Produceer een regel voor elke niet-koppelbare regel van bestand 1:

`join -a {{1}} {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Voeg een bestand samen vanaf `stdin`:

`cat {{pad/naar/bestand1}} | join - {{pad/naar/bestand2}}`
