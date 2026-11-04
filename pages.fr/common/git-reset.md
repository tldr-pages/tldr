# git reset

> Enlève des validations ou des modifications en réinitialisant la tête Git à l'état spécifié.
> Si un chemin est passé en paramètre, Git reset fonctionne comme «unstage»; si un hash de validation ou une branche est passé en paramètre, Git reset fonctionne comme «uncommit».
> Plus d'informations : <https://git-scm.com/docs/git-reset>.

- Désindexe tout :

`git reset`

- Désindexe des fichiers spécifiques :

`git reset {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Désindexe certaines parties d'un fichier en mode interactif :

`git reset {{[-p|--patch]}} {{chemin/vers/fichier}}`

- Annule la dernière validation, mais garde les modifications effectuées (ainsi que toute autre modification non validée) dans le système de fichiers :

`git reset HEAD~`

- Défait les deux dernières validations, et ajoute leurs modifications à l'index (indexées pour validation) :

`git reset --soft HEAD~2`

- Enlève toutes les modifications qui n'ont pas été validées, qu'elles soient indexées ou non (pour enlever uniquement les modifications désindexées, utiliser `git checkout`) :

`git reset --hard`

- Réinitialise le dépôt à une validation spécifique en retirant les modifications validées, indexées, et désindexées depuis cette validation :

`git reset --hard {{validation}}`
