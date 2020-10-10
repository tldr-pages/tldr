# git-grep

> Rechercher une occurence de texte nomport ou dans l historique d un repository.
> Comprends la plus-part des arguments que le `grep` classique.
> Plus d'informations: <https://git-scm.com/docs/git-grep>.

- Rechercher une occrence dans les fichiers suivis:

`git grep {{search_string}}`

- Rechercher une occrence dans les fichiers suivis d'appres un pattern de fichiers:

`git grep {{search_string}} -- {{file_glob_pattern}}`

- Rechercher une occrence dans les fichiers suivis et les sous-modules:

`git grep --recurse-submodules {{search_string}}`

- Rechercher une occurence à partir d un point spécifique dans l'historique:

`git grep {{search_string}} {{HEAD~2}}`

- Rechercher une occurence dans toutes les branches:

`git grep {{search_string}} $(git rev-list --all)`
