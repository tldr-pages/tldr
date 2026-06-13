# git worktree

> Gérer plusieurs arbres de travail attachés au même dépôt.
> Plus d'informations : <https://git-scm.com/docs/git-worktree>.

- Créer un nouvel arbre de travail avec une branche spécifiée :

`git worktree add {{chemin/vers/répertoire}} {{branche}}`

- Créer un nouvel arbre de travail avec une nouvelle branche :

`git worktree add {{chemin/vers/répertoire}} -b {{nouvelle_branche}}`

- Répertorier tous les arbres de travail attachés à ce dépôt :

`git worktree list`

- Supprimer les arbres de travail (après avoir supprimé les répertoires de travail) :

`git worktree prune`
