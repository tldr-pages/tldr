# git cherry-pick

> Appliquer les modifications introduites par les commits existants à la branche actuelle.
> Pour appliquer les changements a une autre branche, utiliser d'abord `git checkout` pour basculer sur la branche désirée.
> Plus d'informations : <https://git-scm.com/docs/git-cherry-pick>.

- Applique un commit à la branche courante :

`git cherry-pick {{commit}}`

- Appliquer une plage de commits à la branche courante (voir aussi `git rebase --onto`) :

`git cherry-pick {{start_commit}}~..{{end_commit}}`

- Appliquer plusieurs commits non séquentiels à la branche courante :

`git cherry-pick {{commit_1}} {{commit_2}}`

- Appliquer les changements d'un commit à la branche courante sans créer de commit :

`git cherry-pick -n {{commit}}`
