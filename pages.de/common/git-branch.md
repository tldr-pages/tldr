# git branch

> Verwalte und Arbeite mit Git Branches.
> Weitere Informationen: <https://git-scm.com/docs/git-branch>.

- Liste alle Branches auf (Lokal und Remote). Der momentan aktive (ausgecheckte) Branch wird mit `*` markiert:

`git branch {{[-a|--all]}}`

- Liste alle Branches auf, welche einen spezifischen Git-Commit in ihrer Historie enthalten:

`git branch {{[-a|--all]}} --contains {{commit_hash}}`

- Zeige den Namen des aktuellen Branches:

`git branch --show-current`

- Erstelle einen neuen Branch auf Basis des letzten Commits:

`git branch {{branch_name}}`

- Erstelle einen neuen Branch auf Basis eines bestimmten Commits:

`git branch {{branch_name}} {{commit_hash}}`

- Benenne einen Branches um (der Branch muss nicht ausgecheckt sein):

`git branch {{[-m|--move]}} {{alter_branch_name}} {{neuer_branch_name}}`

- Lösche einen lokalen Branch (der Branch muss nicht ausgecheckt sein):

`git branch {{[-d|--delete]}} {{branch_name}}`

- Lösche einen remote-Branch:

`git push {{remote_name}} {{[-d|--delete]}} {{remote_branch_name}}`
