# git fetch

> Cherche les objets et réferences depuis un registre distant.
> Plus d'informations : <https://git-scm.com/docs/git-fetch>.

- Cherche les dernières modifications du référentiel amont distant par défaut (si configuré) :

`git fetch`

- Cherche les nouvelles branches depuis un registre distant :

`git fetch {{nom_distant}}`

- Cherche les nouvelles branches depuis tout les registres distant :

`git fetch --all`

- Recherche egalement les tags depuis le registre courrant :

`git fetch --tags`

- Supprime les références locales de branches ayant été supprimés du registre distant :

`git fetch --prune`
