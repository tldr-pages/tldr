# git imerge

> Génére un `git merge` ou un `git rebase` entre deux branches de manière incrémentale.
> Les conflits entre les branches sont suivis en paires de commits individuels, pour simplifier la résolution des conflits.
> Plus d'informations : <https://github.com/mhagger/git-imerge>.

- Démarre un imerge rebase (se place dans la branche à rebaser d'abord) :

`git imerge rebase {{branche_sur_laquelle_rebaser}}`

- Démarre imerge merge (se place dans la branche depuis laquelle merger d'abord) :

`git imerge merge {{branche_a_merger}}`

- Affiche le diagramme ASCII du merge ou rebase en cours :

`git imerge diagram`

- Continue l'opération après une résolution de conflit (d'abord `git add` les fichiers en conflits) :

`git imerge continue --no-edit`

- Termine l'opération i-merge après la résolution de tous les conflits :

`git imerge finish`

- Annule l'opération et retourner à la branche précédente :

`git imerge remove && git checkout {{previous_branch}}`
