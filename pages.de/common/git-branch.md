# git branch

> Verwalte und Arbeite mit Git Branches.
> Weitere Informationen: <https://git-scm.com/docs/git-branch>.

- Liste alle lokalen Branches auf. Der momentan aktive (ausgecheckte) Branch wird mit `*` markiert:

`git branch`

- Liste alle Branches auf (Lokal und Remote):

`git branch -a`

- Zeige den Namen des aktuellen Branches:

`git branch --show-current`

- Erstelle einen neuen Branch auf Basis des letzten Commits:

`git branch {{branch_name}}`

- Erstelle einen neuen Branch auf Basis eines bestimmten Commits:

`git branch {{branch_name}} {{commit_hash}}`

- Benenne einen Branches um (der Branch muss nicht ausgecheckt sein):

`git branch -m {{alter_branch_name}} {{neuer_branch_name}}`

- Lösche einen lokalen Branch (der Branch muss nicht ausgecheckt sein):

`git branch -d {{branch_name}}`

- Lösche einen remote-Branch:

`git push {{remote_name}} --delete {{remote_branch_name}}`
