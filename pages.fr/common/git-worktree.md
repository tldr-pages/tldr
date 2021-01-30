# git worktree

> Gérez plusieurs arborescences de travail attachées au même dépot.
> Plus d'informations : <https://git-scm.com/docs/git-worktree>.

- Créer un nouveau sous arbre avec la branche spécifiée extraite dedans :

`git worktree add {{chemin/vers/repertoire}} {{branche}}`

- Créer un nouveau sous arbre branche extraite dedans :

`git worktree add {{chemin/vers/repertoire}} -b {{nouvelle_branche}}`

- Répertoriez tous les sous arbres attachés à ce dépot :

`git worktree list`

- Suprime les sous arbres (apres avoir suprimé les repertoires de travail) :

`git worktree prune`
