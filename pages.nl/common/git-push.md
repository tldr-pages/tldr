# git push

> Push (upload) commits naar de remote repository.
> Meer informatie: <https://git-scm.com/docs/git-push>.

- Verstuur lokale commits in de huidge branch naar de standaard remote (b.v. origin):

`git push`

- Verstuur commits vanaf een specifieke lokale branch naar de bijhorende remote:

`git push {{remote_naam}} {{lokale_branch}}`

- Verstuur commits vanaf een specifieke branch naar de bijhorende remote, en stel deze remote in als standaard remote:

`git push -u {{remote_naam}} {{lokale_branch}}`

- Verstuur commits vanaf een specifieke lokale branch naar een specifieke remote branch:

`git push {{remote_naam}} {{lokale_branch}}:{{remote_branch}}`

- Verstuur commits van alle branches naar een gegeven remote repository:

`git push --all {{remote_naam}}`

- Verwijder een branch uit een remote repository:

`git push {{remote_naam}} --delete {{remote_branch}}`

- Haal remote branches weg die geen lokale soortgelijke hebben:

`git push --prune {{remote_naam}}`

- Publiceer tags (labels) die nog niet in de remote repository zitten:

`git push --tags`
