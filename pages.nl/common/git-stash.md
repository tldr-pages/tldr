# git stash

> Sla lokale Git-wijzigingen op in een tijdelijke locatie.
> Meer informatie: <https://git-scm.com/docs/git-stash>.

- Sla huidige veranderingen op met een bericht, behalve nieuwe (niet-bijgehouden) bestanden:

`git stash push {{[-m|--message]}} {{stash_message}}`

- Sla huidige veranderingen op, inclusief nieuwe niet-bijgehouden bestanden:

`git stash {{[-u|--include-untracked]}}`

- Selecteer interactief delen van gewijzigde bestanden om op te slaan:

`git stash {{[-p|--patch]}}`

- Toon alle stashes (toont stash-naam, gerelateerde branch en bericht):

`git stash list`

- Toon de wijzigingen als een patch tussen de stash (standaard is `stash@{0}`) en de commit van toen de stash voor het eerst werd aangemaakt:

`git stash show {{[-p|--patch]}} {{stash@{0}}}`

- Pas een stash toe (standaard is de recenste, genaamd `stash@{0}`):

`git stash apply {{facultatieve_stash_naam_of_commit}}`

- Verwijder of pas een stash toe (standaard is `stash@{0}`) en verwijder deze uit de stash-lijst als het toepassen geen conflicten veroorzaakt:

`git stash pop {{facultatieve_stash_naam}}`

- Verwijder alle stashes:

`git stash clear`
