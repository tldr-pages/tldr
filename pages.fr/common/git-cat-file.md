# git cat-file

> Fournir des informations sur le contenu ou le type et la taille des objets du référentiel git.
> Plus d'informations: <https://git-scm.com/docs/git-cat-file>.

- Obtenir la taill [s] du commit HEAD en octets :

`git cat-file -s HEAD`

- Obtenir le type [t] (blob, tree, commit, tag) d'un objet git spécifié :

`git cat-file -t {{8c442dc3}}`

- Affiche le contenu [p] d'un objet git basé sur son type :

`git cat-file -p {{HEAD~2}}`
