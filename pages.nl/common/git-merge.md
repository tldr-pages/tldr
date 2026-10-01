# git merge

> Voeg branches samen.
> Meer informatie: <https://git-scm.com/docs/git-merge>.

- Voeg branches samen met de huidige branch:

`git merge {{branch_naam1 branch_naam2 ...}}`

- Bewerk het samenvoegingsbericht:

`git merge {{[-e|--edit]}} {{branch_naam}}`

- Voeg een branch samen en maak een samenvoegingscommit:

`git merge --no-ff {{branch_naam}}`

- Voeg het resultaat van het samenvoegen van een branch toe zonder een commit aan te maken:

`git merge --squash {{branch_naam}}`

- Breek een samenvoeging af in geval van conflicten:

`git merge --abort`

- Voeg samen met behulp van een specifieke strategie:

`git merge {{[-s|--strategy]}} {{strategie}} {{[-X|--strategy-option]}} {{strategie_keuze}} {{branch_naam}}`
