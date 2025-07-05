# git branch

> Hoofd Git-commando voor het werken met branches.
> Meer informatie: <https://git-scm.com/docs/git-branch>.

- Toon alle branches (lokaal en extern; de huidige branch is aangegeven met `*`):

`git branch {{[-a|--all]}}`

- Toon welke branches een specifieke Git commit in hun geschiedenis hebben:

`git branch {{[-a|--all]}} --contains {{commit_hash}}`

- Toon de naam van de huidige branch:

`git branch --show-current`

- Creëer een nieuwe branch gebaseerd op de huidige commit:

`git branch {{branch_naam}}`

- Creëer een nieuwe branch gebaseerd op een specifieke commit:

`git branch {{branch_naam}} {{commit_hash}}`

- Hernoem een branch (je moet eerst wisselen naar een andere branch):

`git branch {{[-m|--move]}} {{oude_branch_naam}} {{nieuwe_branch_naam}}`

- Verwijder een lokale branch (je moet eerst wisselen naar een andere branch):

`git branch {{[-d|--delete]}} {{branch_naam}}`

- Verwijder een externe branch:

`git push {{externe_naam}} {{[-d|--delete]}} {{externe_branch_naam}}`
