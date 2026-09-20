# git log

> Affiche un historique de validations.
> Plus d'informations : <https://git-scm.com/docs/git-log>.

- Affiche la séquence de validations à partir de l'actuel, dans l'ordre chronologique inverse du dépôt Git dans le répertoire de travail actuel :

`git log`

- Affiche l'historique de fichiers ou répertoires en particulier :

`git log {{[-p|--patch]}} {{chemin/vers/fichier_ou_répertoire}}`

- Affiche la liste des fichiers modifiés pour chaque validation :

`git log --stat`

- Affiche un graphique des validations dans la branche actuelle en utilisant uniquement la première ligne de chaque message de validation :

`git log --oneline --graph`

- Affiche un graphique de tout les validations, étiquettes et branches dans le dépôt entier :

`git log --oneline --decorate --all --graph`

- Affiche uniquement les validations dont le message contient la chaine (insensible à la casse) :

`git log {{[-i|--regexp-ignore-case]}} --grep {{chaine_recherché}}`

- Affiche les N dernières validations d'un utilisateur :

`git log {{[-n|--max-count]}} {{number}} --author "{{author}}"`

- Affiche les validations entre deux dates (aaaa-mm-jj) :

`git log --before "{{2017-01-29}}" --after "{{2017-01-17}}"`
