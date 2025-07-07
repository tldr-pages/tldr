# git push

> Push commits naar een externe repository.
> Meer informatie: <https://git-scm.com/docs/git-push>.

- Stuur lokale aanpassingen in de huidige branch naar de standaard externe tegenhanger:

`git push`

- Stuur aanpassingen van een specifieke lokale branch naar zijn externe tegenhanger:

`git push {{externe_naam}} {{lokale_branch}}`

- Stuur veranderingen van een specifieke lokale branch naar naar zijn externe tegenhanger en stel de externe branch in als de standaard push/pull-doel voor de lokale branch:

`git push {{[-u|--set-upstream]}} {{externe_naam}} {{lokale_branch}}`

- Stuur veranderingen van een specifieke lokale branch naar een specifieke externe branch:

`git push {{externe_naam}} {{lokale_branch}}:{{externe_branch}}`

- Stuur aanpassingen op alle lokale branches naar hun tegenhangers in de opgegeven externe repository:

`git push --all {{externe_naam}}`

- Verwijder een branch in een externe repository:

`git push {{externe_naam}} {{[-d|--delete]}} {{externe_branch}}`

- Verwijder externe branches die geen lokale tegenhanger hebben:

`git push --prune {{externe_naam}}`

- Publiceer tags die nog niet in de externe repository staan:

`git push --tags`
