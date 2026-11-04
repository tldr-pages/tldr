# git show-branch

> Affiche les branches et leurs validations.
> Plus d'informations : <https://git-scm.com/docs/git-show-branch>.

- Affiche un résumé de la dernière validation dans la branche :

`git show-branch {{nom_branche|ref|validation}}`

- Compare des validations avec plusieurs validations ou branches :

`git show-branch {{nom_branche1|ref1|validation1 nom_branche2|ref2|validation2 ...}}`

- Compare toutes les branches de suivi distantes :

`git show-branch {{[-r|--remotes]}}`

- Compare les branches locales et les branches de suivi distantes :

`git show-branch {{[-a|--all]}}`

- Liste les dernières validations sur toutes les branches :

`git show-branch {{[-a|--all]}} --list`

- Compare une branche spécifique à la branche actuelle :

`git show-branch --current {{validation|nom_branche|ref}}`

- Affiche le nom de la validation au lieu du nom relatif :

`git show-branch --sha1-name --current {{actuel|nom_branche|ref}}`

- Continue l'affichage d'un certain nombre de validations au-delà de l'ancêtre commun :

`git show-branch --more {{5}} {{nom_branche1|ref1|validation1 nom_branche2|ref2|validation2 ...}}`
