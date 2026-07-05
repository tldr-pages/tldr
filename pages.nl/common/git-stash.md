# git stash

> Sla lokale Git-wijzigingen op in een tijdelijke locatie.
> Meer informatie: <https://git-scm.com/docs/git-stash>.

- Sla de huidige niet-gecommitte veranderingen op:

`git stash`

- Sla huidige veranderingen op, inclusief nieuwe niet-bijgehouden bestanden:

`git stash {{[-u|--include-untracked]}}`

- Selecteer interactief delen van gewijzigde bestanden om op te slaan:

`git stash {{[-p|--patch]}}`

- Toon alle stashes (toont stash-naam, gerelateerde branch en bericht):

`git stash list`

- Toon de wijzigingen als een patch tussen de stash en de commit van toen de stash voor het eerst werd aangemaakt:

`git stash show {{[-p|--patch]}}`

- Pas een stash toe en verwijder deze van de stash-lijst als het toepassen niet tot conflicten lijdt:

`git stash pop`

- Verwijder de recenste stash:

`git stash drop`

- Verwijder alle stashes:

`git stash clear`
