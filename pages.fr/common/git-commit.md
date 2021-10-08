# git commit

> Enregistrer (`commit`) les fichiers dans le dépôt.
> Plus d'informations : <https://git-scm.com/docs/git-commit>.

- Commit les fichiers en stage dans le dépôt avec un message :

`git commit -m "{{message}}"`

- Commit tous les fichiers modifiés avec un message :

`git commit -am "{{message}}"`

- Met à jour le dernier commit avec les modifications en stage :

`git commit --amend`

- Commit seulement les fichiers spécifiés (qui sont déjà en stage) :

`git commit {{chemin/vers/mon/fichier1}} {{chemin/vers/mon/fichier2}}`
