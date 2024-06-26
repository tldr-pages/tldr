# paste

> Voeg regels van bestanden samen.
> Meer informatie: <https://www.gnu.org/software/coreutils/paste>.

- Voeg alle regels samen tot één enkele regel, met TAB als scheidingsteken:

`paste -s {{pad/naar/bestand}}`

- Voeg alle regels samen tot één enkele regel, met het opgegeven scheidingsteken:

`paste -s -d {{scheidingsteken}} {{pad/naar/bestand}}`

- Voeg twee bestanden zij aan zij samen, elk in zijn kolom, met TAB als scheidingsteken:

`paste {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Voeg twee bestanden zij aan zij samen, elk in zijn kolom, met het opgegeven scheidingsteken:

`paste -d {{scheidingsteken}} {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Voeg twee bestanden samen, met afwisselend toegevoegde regels:

`paste -d '\n' {{pad/naar/bestand1}} {{pad/naar/bestand2}}`
