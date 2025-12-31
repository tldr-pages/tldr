# git log

> Toon een geschiedenis van commits.
> Meer informatie: <https://git-scm.com/docs/git-log>.

- Toon de volgorde van commits, beginnend bij de huidige, in omgekeerd chronologische volgorde van de Git-repository in de huidige map:

`git log`

- Toon de geschiedenis van een bepaald bestand of map, inclusief verschillen:

`git log {{[-p|--patch]}} {{pad/naar/bestand_of_map}}`

- Toon een overzicht van welke bestand(en) zijn gewijzigd in elke commit:

`git log --stat`

- Toon een grafiek van de commits in de huidige branch met alleen de eerste regel van elk commitbericht:

`git log --oneline --graph`

- Toon een grafiek van alle commits, tags en branches in de hele repository:

`git log --oneline --decorate --all --graph`

- Toon alleen commits met berichten die een specifieke string bevatten, waarbij hoofdlettergebruik wordt genegeerd:

`git log {{[-i|--regexp-ignore-case]}} --grep {{zoekstring}}`

- Toon de laatste N commits van een bepaalde auteur:

`git log {{[-n|--max-count]}} {{nummer}} --author "{{auteur}}"`

- Toon commits tussen twee datums (yyyy-mm-dd):

`git log --before "{{2017-01-29}}" --after "{{2017-01-17}}"`
