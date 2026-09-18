# git reset

> Enlève des validations ou des changements en réinitialisant la tête Git à l'état spécifié.
> Si un chemin est passé en paramètre, Git reset fonctionne comme «unstage».
> Si un hash de validation est passé en paramètre, Git reset annule les validations jusqu'à ce dernier.
> Plus d'informations : <https://git-scm.com/docs/git-reset>.

- Enlève tout de la zone de stage :

`git reset`

- Enlève des fichiers spécifiques de la zone de stage :

`git reset {{chemin/vers/fichier(s)}}`

- Enlève, en mode interactif, des fichiers spécifiques de l’index :

`git reset {{[-p|--patch]}} {{chemin/vers/fichier}}`

- Annule la dernière validation, mais garde les changements effectués dans le système de fichiers :

`git reset HEAD~`

- Défait les deux dernières validations, et ajoute leurs changements à l'index (dans la zone de stage) :

`git reset --soft HEAD~2`

- Enlève tous les changements qui n'ont pas été validé, qu'ils soient dans la zone de stage ou non (pour enlever seulement les changements de la zone de stage, utiliser `git checkout`) :

`git reset --hard`

- Réinitialise le dépôt à une validation spécifique en retirant tous les changements (ceci inclut les changements dans des validations entre la tête et la validation spécifiée !) :

`git reset --hard {{validation}}`
