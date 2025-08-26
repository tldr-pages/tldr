# git merge

> Voeg branches samen.
> Meer informatie: <https://git-scm.com/docs/git-merge>.

- Voeg een branch samen met de huidige branch:

`git merge {{branch_naam}}`

- Bewerk het samenvoegingsbericht:

`git merge {{[-e|--edit]}} {{branch_naam}}`

- Voeg een branch samen en maak een samenvoegingscommit:

`git merge --no-ff {{branch_naam}}`

- Breek een samenvoeging af in geval van conflicten:

`git merge --abort`

- Voeg samen met behulp van een specifieke strategie:

`git merge {{[-s|--strategy]}} {{strategie}} {{[-X|--strategy-option]}} {{strategie_keuze}} {{branch_naam}}`
