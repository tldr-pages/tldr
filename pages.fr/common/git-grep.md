# git grep

> Recherche une occurrence de texte n'importe où dans l'historique d'un dépôt git.
> Comprend la plupart des arguments du `grep` classique.
> Plus d'informations : <https://git-scm.com/docs/git-grep>.

- Recherche une chaîne de caractères dans les fichiers du `HEAD` actuel :

`git grep "{{chaine_recherché}}"`

- Recherche une occurrence dans les fichiers suivis d'après un schéma d'expansion de fichier :

`git grep "{{chaine_recherché}}" -- "{{*.ext}}"`

- Recherche une occurrence dans les fichiers suivis et les sous-modules :

`git grep --recurse-submodules "{{chaine_recherché}}"`

- Recherche une occurrence à partir d'un point spécifique dans l'historique :

`git grep "{{chaine_recherché}}" {{HEAD~2}}`

- Recherche une occurrence dans toutes les branches :

`git grep "{{chaine_recherché}}" $(git rev-list --all)`
