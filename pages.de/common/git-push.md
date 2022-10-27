# git push

> Lade Commits in ein Remote-Repository hoch.
> Weitere Informationen: <https://git-scm.com/docs/git-push>.

- Sende lokale Änderungen des aktuellen Branches zu seinem entfernten Repository (Remote Branch):

`git push`

- Sende lokale Änderungen des angegebenen Branches zu seinem entfernten Repository:

`git push {{remote_name}} {{lokaler_branch}}`

- Lade den aktuellen Branch in ein entferntes Repository mit Angabe des Namens des entfernten Branches hoch:

`git push -u {{remote_name}} {{remote_branch}}`

- Lade Änderungen eines bestimmten lokalen Branches zu einem bestimmten entfernten Branch hoch:

`git push {{remote_name}} {{lokaler_branch}}:{{entfernter_branch}}`

- Lade Änderungen aller lokalen Branches zu ihrem entfernten Repository hoch:

`git push --all {{remote_name}}`

- Lösche einen Branch in einem entfernten Repository:

`git push {{remote_name}} --delete {{remote_branch}}`

- Entferne alle remote Branches, welche kein lokales Gegenstück besitzen:

`git push --prune {{remote_name}}`

- Veröffentliche Tags, welche noch nicht im entfernten Repository vorhanden sind:

`git push --tags`
