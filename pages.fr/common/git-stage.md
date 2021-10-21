# git stage

> Ajouter le contenu du fichier à la zone de préparation.
> Synonyme de `git add`.
> Plus d'informations : <https://git-scm.com/docs/git-stage>.

- Ajouter un fichier à l'index :

`git stage {{chemin/vers/fichier}}`

- Ajoute tous les fichiers à l'index (suivis et non-suivis) :

`git stage -A`

- Ajout uniquement des fichiers déjà suivis :

`git stage -u`

- Ajout également des fichiers ignorés :

`git stage -f`

- Ajout des fichiers par parties, interactivement :

`git stage -p`

- Ajout d'un fichier par parties, interactivement :

`git stage -p {{chemin/vers/fichier}}`

- Ajout d'un fichier, interactivement :

`git stage -i`
