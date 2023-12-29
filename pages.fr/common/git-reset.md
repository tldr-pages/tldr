# git reset

> Enlève des commits ou des changements en réinitialisant la tête Git à l'état spécifié.
> Si un chemin est passé en paramètre, Git reset fonctionne comme «unstage».
> Si un hash de commit est passé en paramètre, Git reset annule les commits jusqu'à ce dernier.
> Plus d'informations : <https://git-scm.com/docs/git-reset>.

- Tout enlever de la zone de stage :

`git reset`

- Enlever des fichiers spécifiques de la zone de stage :

`git reset {{chemin/vers/fichier(s)}}`

- Enlever, en mode interactif, des fichiers spécifiques de l’index :

`git reset --patch {{chemin/vers/fichier}}`

- Annuler le dernier commit, mais garder les changements effectués dans votre système de fichiers :

`git reset HEAD~`

- Défaire les deux derniers commits, et ajouter leurs changements à l'index (dans la zone de stage) :

`git reset --soft HEAD~2`

- Enlever tout les changements qui n'ont pas été commit, qu'ils soient dans la zone de stage ou non (pour enlever seulement les changements de la zone de stage, utiliser `git checkout`) :

`git reset --hard`

- Réinitialiser le dépôt à un commit spécifique en retirant tout les changements (ceci inclus les changements dans des commits entre la tête et le commit spécifié !) :

`git reset --hard {{commit}}`
