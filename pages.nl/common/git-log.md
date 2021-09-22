# git log

> Geef de commit geschiedenis.
> Meer informatie: <https://git-scm.com/docs/git-log>.

- Geef de commit reeks startend bij de huidge, in omgekeerde volgerde:

`git log`

- Geef de geschiedenis van een specifieke bestand of map, inclusief de veranderingen:

`git log -p {{pad/naar/bestand_of_map}}`

- Geef een overzicht van welk(e) bestand(en) zijn veranderd in elke commit:

`git log --stat`

- Geef een grafiek van commits in de huidige branch, met enkel de eerste lijk van de commit weergegeven:

`git log --oneline --graph`

- Geef een grafiek van alle commits, tags en branches in the complete repository:

`git log --oneline --decorate --all --graph`

- Geef enkel commits aan met welke bericht een specifieke tekst bevat:

`git log -i --grep {{zoek-tekst}}`

- Geef de laatste N commits van een specifieke auteur:

`git log -n {{number}} --author={{author}}`

- Geef commits tussen twee data:

`git log --before={{datum}} --after={{datum}}`
