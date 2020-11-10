# git clean

> Supprimer les fichiers non suivis du repertoire.
> Plus d'informations: <https://git-scm.com/docs/git-clean>.

- Supprimer les fichiers non suivis par git :

`git clean`

- Supprimer les fichiers non suivis par git de manière interactive :

`git clean -i`

- Affiche les fichiers non suivis qui peuvent étre suprimmés :

`git clean --dry-run`

- Nettoyage forcé des fichiers non suivis par git :

`git clean -f`

- Nettoyage forcé des repertoires non suivis par git :

`git clean -fd`

- Supprime tout les fichiers suivis, incluant ceux repertoriés par `.gitignore` et `.git/info/exclude` :

`git clean -x`
