# git-grep

> Rechercher une occurrence de texte n'importe où dans l'historique d'un dépôt git.
> Comprend la plupart des arguments du `grep` classique.
> Plus d'informations : <https://git-scm.com/docs/git-grep>.

- Rechercher une occurrence dans les fichiers suivis :

`git grep {{chaine_recherché}}`

- Rechercher une occurrence dans les fichiers suivis d'après un pattern de fichiers :

`git grep {{chaine_recherché}} -- {{file_glob_pattern}}`

- Rechercher une occurrence dans les fichiers suivis et les sous-modules :

`git grep --recurse-submodules {{chaine_recherché}}`

- Rechercher une occurrence à partir d'un point spécifique dans l'historique :

`git grep {{chaine_recherché}} {{HEAD~2}}`

- Rechercher une occurrence dans toutes les branches :

`git grep {{chaine_recherché}} $(git rev-list --all)`
