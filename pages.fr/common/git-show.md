# git show

> Affiche différents types d'objets Git (validations, étiquettes, etc.).
> Plus d'informations : <https://git-scm.com/docs/git-show>.

- Affiche des informations sur la dernière validation (hachage, message, modifications et autres métadonnées) :

`git show`

- Affiche les informations sur une validation, étiquette, ou branche spécifique (comme `HEAD` pour la validation la plus récente) :

`git show {{validation|étiquette|branche}}`

- Affiche uniquement la liste des fichiers ajoutés, renommés, ou supprimés :

`git show --summary {{validation}}`

- Ignore les espaces lors de la comparaison de lignes :

`git show {{[-w|--ignore-all-space]}}`

- Affiche le message d'une validation sur une seule ligne, en supprimant la sortie diff :

`git show --oneline {{[-s|--no-patch]}} {{validation}}`

- Affiche les statistiques du diff pour les fichiers modifiés (comme des lignes ajoutées ou supprimées) :

`git show --stat {{validation}}`

- Affiche une liste simplifiée de tous les fichiers modifiés dans une validation (modifiés, ajoutés, et supprimés) :

`git show --name-only {{validation}}`

- Affiche le contenu d'un fichier tel qu'il était à une révision donnée (par exemple, branche, tag ou validation) :

`git show {{revision}}:{{chemin/vers/fichier}}`
