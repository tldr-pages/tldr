# git branch

> Commande Git principale pour travailler avec des branches.
> Plus d'informations : <https://git-scm.com/docs/git-branch>.

- Liste toutes les branches (locale et distantes) :

`git branch {{[-a|--all]}}`

- Affiche le nom de la branche courante :

`git branch --show-current`

- Crée une nouvelle branche depuis le commit courant :

`git branch {{nom_de_branche}}`

- Crée une nouvelle branche depuis un commit en particulier :

`git branch {{nom_de_branche}} {{commit_hash}}`

- Renommer une branche (ne pas se trouver sur la branche pour le faire) :

`git branch {{[-m|--move]}} {{ancien_nom_de_branche}} {{nouveau_nom_de_branche}}`

- Supprimer un branche locale (ne pas se trouver sur la branche pour le faire) :

`git branch {{[-d|--delete]}} {{nom_de_branche}}`

- Supprimer une branche distante :

`git push {{nom_distant}} {{[-d|--delete]}} {{nom_de_branche_distante}}`
