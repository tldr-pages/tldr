# git show-branch

> Affiche les branches et leurs commits.
> Plus d'informations : <https://git-scm.com/docs/git-show-branch>.

- Affiche un résumé du dernier commit dans la branche :

`git show-branch {{nom_de_branche|ref|commit}}`

- Comparer des commits avec plusieurs commits ou branches :

`git show-branch {{nom_de_branche|ref|commit}}`

- Comparer toutes les branches distantes :

`git show-branch --remotes`

- Comparer la branche locale avec la branche distante :

`git show-branch --all`

- Lister les derniers commits sur toutes les branches :

`git show-branch --all --list`

- Comparer une branche spécifique à la branche courante :

`git show-branch --current {{commit|nom_de_branche|ref}}`

- Afficher le nom du commit au lieu du nom relatif :

`git show-branch --sha1-name --current {{current|nom_de_branche|ref}}`

- Continuez l'affichage d'un certain nombre de commits au-delà de l'ancêtre commun :

`git show-branch --more {{5}} {{commit|nom_de_branche|ref}} {{commit|nom_de_branche|ref}} {{...}}`
