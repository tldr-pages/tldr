# git stage

> Ajouter le contenu du fichier à la zone de préparation.
> Synonym of `git add`.
> Plus d'informations : <https://git-scm.com/docs/git-stage>.

- Ajouter un fichier à l'index :

`git stage {{chemin/vers/fichier}}`

- Ajoute tout les fichiers à l'index (suivis et non suivis) :

`git stage -A`

- Ajout uniquement des fichiers déja suivis :

`git stage -u`

- Ajout egalement des fichiers ignorés :

`git stage -f`

- Ajout des fichiers par parties, interactivement :

`git stage -p`

- Ajout d'un fichier par parties, interactivement :

`git stage -p {{chemin/vers/fichier}}`

- Ajout d'un fichier, interactivement :

`git stage -i`
