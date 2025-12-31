# git clean

> Supprimer les fichiers non-suivis d'un dépôt Git.
> Plus d'informations : <https://git-scm.com/docs/git-clean>.

- Supprimer les fichiers non-suivis :

`git clean`

- Supprimer les fichiers non-suivis de manière interactive :

`git clean {{[-i|--interactive]}}`

- Affiche les fichiers non-suivis qui peuvent être supprimés :

`git clean {{[-n|--dry-run]}}`

- Nettoyage forcé des fichiers non-suivis :

`git clean {{[-f|--force]}}`

- Nettoyage forcé des répertoires non-suivis :

`git clean {{[-f|--force]}} -d`

- Supprime tous les fichiers suivis, incluant ceux répertoriés par `.gitignore` et `.git/info/exclude` :

`git clean -x`
