# git push

> Schiebe Commits zu einem Remote-Repository
> Mehr Informationen: <https://git-scm.com/docs/git-push>.

- Sende lokale Änderungen des aktuellen Branches zu seinem entfernten Gegenstück (Remote Branch):

`git push`

- Sende lokale Änderungen des angegebenen Branches zu seinem entfernten Gegenstück (Remote Branch):

`git push {{remote_name}} {{local_branch}}`

- Veröffentlichen des aktuellen Branches in einem entfernten Repository, mit Angabe des Namens des entfernten Branches:

`git push {{remote_name}} -u {{remote_branch}}`

- Sende Änderungen aller lokalen Branches zu ihren entfernten Gegenstücken (Remote Branches) eines bestimmten Repositories:

`git push --all {{remote_name}}`

- Löschen eines Branches in einem entfernten Repositories:

`git push {{remote_name}} --delete {{remote_branch}}`

- Entfernen aller entfernter Branches, welche kein lokales Gegenstück besitzen:

`git push --prune {{remote_name}}`

- Veröffentlichen von Tags, welche noch nicht im entfernten Repository vorhanden sind:

`git push --tags`
