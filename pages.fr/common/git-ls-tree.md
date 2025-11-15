# git ls-tree

> Lister le contenu d'un arbre.
> Plus d'informations : <https://git-scm.com/docs/git-ls-tree>.

- Lister le contenu de l'arbre dans la branche :

`git ls-tree {{nom_de_branche}}`

- Lister le contenu de l'arbre dans le commit, récursif avec les sous-arbres :

`git ls-tree -r {{commit_hash}}`

- Lister uniquement les noms de fichiers de l'arbre dans un commit :

`git ls-tree --name-only {{commit_hash}}`
