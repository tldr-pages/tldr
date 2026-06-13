# git merge

> Voeg branches samen.
> Meer informatie: <https://git-scm.com/docs/git-merge>.

- Voeg een branch samen met de huidige branch:

`git merge {{branch_naam}}`

- Bewerk het samenvoegingsbericht:

`git merge {{[-e|--edit]}} {{branch_naam}}`

- Voeg een branch samen en maak een samenvoegingscommit:

`git merge --no-ff {{branch_naam}}`

- Kopieer de status van een branch naar de huidige working tree en voeg deze toe (Opmerking: gebruik `git commit` om de daadwerkelijke commit aan te maken):

`git merge --squash {{branch_naam}}`

- Breek een samenvoeging af in geval van conflicten:

`git merge --abort`

- Voeg samen met behulp van een specifieke strategie:

`git merge {{[-s|--strategy]}} {{strategie}} {{[-X|--strategy-option]}} {{strategie_keuze}} {{branch_naam}}`
