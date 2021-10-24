# git switch

> Basculez entre les branches Git. Nécessite la version 2.23+ de Git.
> Voir également `git checkout`.
> Plus d'informations : <https://git-scm.com/docs/git-switch>.

- Baculer sur une branche existante :

`git switch {{nom_de_branche}}`

- Créer une nouvelle branche et basculer dessus :

`git switch --create {{nom_de_branche}}`

- Créer une nouvelle branche en partant d'un commit donné et basculer dessus :

`git switch --create {{nom_de_branche}} {{commit}}`

- Basculer sur la branche précédente :

`git switch -`

- Basculer vers une branche et mettre à jour tous les sous-modules pour qu'ils correspondent :

`git switch --recurse-submodules {{nom_de_branche}}`

- Basculer vers une branche et fusionner automatiquement la branche actuelle et toutes les modifications non validées dedans :

`git switch --merge {{nom_de_branche}}`
