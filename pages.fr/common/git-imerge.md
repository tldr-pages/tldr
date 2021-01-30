# git-imerge

> Génerer un merge ou un rebase entre deux branches de maniére incrémentale.
> Les conflits entre les branches sont suivis en paires de commits individuels, pour simplifier la résolution des conflits.
> Plus d'informations : <https://github.com/mhagger/git-imerge>.

- Démarrer un i-merge rebase (se placer dans la branche a rebaser d'abord) :

`git imerge rebase {{branche_sur_laquelle_rebaser}}`

- Démarrer imerge merge (se placer dans la branche depuis laquelle merger d'abord) :

`git imerge merge {{branche_a_merger}}`

- Afficher le diagramme ASCII du merge ou rebase en cours :

`git imerge diagram`

- Continuer l opperation après une résolution de conflit (d'abord `git add` les fichiers en conflits) :

`git imerge continue --no-edit`

- Terminer l'opperation i-merge après la resolution de tout les conflits :

`git imerge finish`

- Annuler l'opperation et retourner à la branche précédante :

`git-imerge remove && git checkout {{previous_branch}}`
