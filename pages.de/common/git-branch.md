# git branch

> Befehl zum Arbeiten mit Branches.
> Mehr Informationen: <https://git-scm.com/docs/git-branch>.

- Auflisten der lokalen Branches. Der momentan aktive (ausgecheckte) Branch wird mit `*` markiert:

`git branch`

- Auflisten aller Branches (Lokal und Remote):

`git branch -a`

- Zeigt den Namen des aktuellen Branches:

`git branch --show-current`

- Erstellt einen neuen Branch auf Basis des letzten Commits:

`git branch {{branch_name}}`

- Erstellt einen neuen Branch auf Basis eines spezifischen Commits:

`git branch {{branch_name}} {{commit_hash}}`

- Umbenennen eines Branches (der Branch muss nicht ausgecheckt sein):

`git branch -m {{alter_branch_name}} {{neuer_branch_name}}`

- Löschen eines lokalen Branches (der Branch muss nicht ausgecheckt sein):

`git branch -d {{branch_name}}`

- Löschen eines remote Branches:

`git push {{remote_name}} --delete {{remote_branch_name}}`
