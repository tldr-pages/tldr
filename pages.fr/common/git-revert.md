# git revert

> Créer un nouveau commit qui efface les changements du précédent.
> Plus d'informations : <https://git-scm.com/docs/git-revert>.

- Crée un commit qui annule les changements du dernier commit :

`git revert {{HEAD}}`

- Crée un commit qui annule les changements des 5 dernier commit :

`git revert HEAD~{{4}}`

- Crée un commit qui annule les changements de plusieurs commit :

`git revert {{master~5..master~2}}`

- Ne pas créer de nouveau commit, remplacer uniquement dans l'arbre courant :

`git revert -n {{0c01a9..9a1743}}`
