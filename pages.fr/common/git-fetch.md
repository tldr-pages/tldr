# git fetch

> Cherche les objets et références depuis un dépôt distant.
> Plus d'informations : <https://git-scm.com/docs/git-fetch>.

- Cherche les dernières modifications du référentiel amont distant par défaut (si configuré) :

`git fetch`

- Cherche les nouvelles branches depuis un registre distant :

`git fetch {{nom_distant}}`

- Cherche les nouvelles branches depuis tous les registres distants :

`git fetch --all`

- Recherche également les tags depuis le registre courant :

`git fetch --tags`

- Supprime les références locales de branches ayant été supprimés du registre distant :

`git fetch --prune`
