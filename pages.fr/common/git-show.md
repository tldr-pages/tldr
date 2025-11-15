# git show

> Affiche différents types d'objets Git (commits, tags, etc.).
> Plus d'informations : <https://git-scm.com/docs/git-show>.

- Afficher des informations sur le dernier commit (hachage, message, modifications et autres métadonnées) :

`git show`

- Affiche les informations du dernier commit :

`git show {{commit}}`

- Affiche les informations associés au tag spécifié :

`git show {{etiquette}}`

- Affiche les informations à propos du 3ème commit en partant du sommet de la branche :

`git show {{branche}}~{{3}}`

- Afficher le message d'un commit sur une seule ligne, en supprimant la sortie diff :

`git show --oneline -s {{commit}}`

- Affiche uniquement la liste des fichiers changés dans un commit :

`git show --stat {{commit}}`

- Afficher le contenu d'un fichier tel qu'il était à une révision donnée (par exemple, branche, tag ou commit) :

`git show {{revision}}:{{chemin/vers/fichier}}`
