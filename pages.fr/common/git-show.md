# git show

> Affiche différents types d'objets Git (validations, tags, etc.).
> Plus d'informations : <https://git-scm.com/docs/git-show>.

- Affiche des informations sur la dernière validation (hachage, message, modifications et autres métadonnées) :

`git show`

- Affiche les informations de la dernière validation :

`git show {{validation}}`

- Affiche les informations associés au tag spécifié :

`git show {{etiquette}}`

- Affiche les informations à propos de la 3ème validation en partant du sommet de la branche :

`git show {{branche}}~{{3}}`

- Afficher le message d'une validation sur une seule ligne, en supprimant la sortie diff :

`git show --oneline -s {{validation}}`

- Affiche uniquement la liste des fichiers changés dans une validation :

`git show --stat {{validation}}`

- Affiche le contenu d'un fichier tel qu'il était à une révision donnée (par exemple, branche, tag ou validation) :

`git show {{revision}}:{{chemin/vers/fichier}}`
