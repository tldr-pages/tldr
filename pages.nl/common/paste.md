# paste

> Voeg regels van bestanden samen.
> Meer informatie: <https://www.gnu.org/software/coreutils/manual/html_node/paste-invocation.html>.

- Voeg alle regels samen tot één enkele regel, met TAB als scheidingsteken:

`paste {{[-s|--serial]}} {{pad/naar/bestand}}`

- Voeg alle regels samen tot één enkele regel, met het opgegeven scheidingsteken:

`paste {{[-s|--serial]}} {{[-d|--delimiters]}} {{scheidingsteken}} {{pad/naar/bestand}}`

- Voeg twee bestanden zij aan zij samen, elk in zijn kolom, met TAB als scheidingsteken:

`paste {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Voeg twee bestanden zij aan zij samen, elk in zijn kolom, met het opgegeven scheidingsteken:

`paste {{[-d|--delimiters]}} {{scheidingsteken}} {{pad/naar/bestand1}} {{pad/naar/bestand2}}`

- Voeg twee bestanden samen, met afwisselend toegevoegde regels:

`paste {{[-d|--delimiters]}} '\n' {{pad/naar/bestand1}} {{pad/naar/bestand2}}`
