# git switch

> Basculez entre les branches git. Nécessite la version 2.23+ de git.
> Voir egalement `git checkout`.
> Plus d'informations: <https://git-scm.com/docs/git-switch/>.

- Baculer sur une branche existante:

`git switch {{branch_name}}`

- Créer une nouvelle branche et basculer dessus:

`git switch --create {{branch_name}}`

- Créer une nouvelle branche en partant d'un commit donné et basculer dessus:

`git switch --create {{branch_name}} {{commit}}`

- Basculer sur la branche précedante:

`git switch -`

- Basculer vers une branche et mettre à jour tous les sous-modules pour qu'ils correspondent:

`git switch --recurse-submodules {{branch_name}}`

- Basculer vers une branche et fusionner automatiquement la branche actuelle et toutes les modifications non validées dedans:

`git switch --merge {{branch_name}}`
