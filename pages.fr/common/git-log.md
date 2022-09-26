# git log

> Afficher un historique de commits.
> Plus d'informations : <https://git-scm.com/docs/git-log>.

- Afficher la séquence de commits à partir de l'actuel, dans l'ordre chronologique inverse du dépôt Git dans le répertoire de travail actuel :

`git log`

- Afficher l'historique de fichiers ou répertoires en particulier :

`git log -p {{chemin/vers/fichier_ou_repertoire}}`

- Afficher la liste des fichiers modifiés pour chaque commit :

`git log --stat`

- Afficher un graphique des commits dans la branche actuelle en utilisant uniquement la première ligne de chaque message de commit :

`git log --oneline --graph`

- Afficher un graphique de tout les commits, tags et branches dans le dépôt entier :

`git log --oneline --decorate --all --graph`

- Afficher uniquement les commits dont le message contient la chaine (non sensible à la casse) :

`git log -i --grep {{chaine_recherché}}`

- Afficher les N derniers commits d'un utilisateur :

`git log -n {{number}} --author={{author}}`

- Afficher les commits entre deux dates (yyyy-mm-dd):

`git log --before="{{2017-01-29}}" --after="{{2017-01-17}}"`
