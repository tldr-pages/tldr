# git subtree

> Outil pour gérer les dépendances de projet en tant que sous-projets.
> Plus d'informations: <https://manpages.debian.org/testing/git-man/git-subtree.1.en.html>.

- Ajout d'un dépot git en tant que sous arbre:

`git subtree add --prefix={{path/to/directory/}} --squash {{repository_url}} {{master}}`

- Metre a jour le sous arbre avec son dernier commit:

`git subtree pull --prefix={{path/to/directory/}} {{repository_url}} {{master}}`

- Merge le dépot d'un sous arbre dans la branche master:

`git subtree merge --prefix={{path/to/directory/}} --squash {{repository_url}} {{master}}`

- Pousser les commits vers le dépot d'un sous arbre:

`git subtree push --prefix={{path/to/directory/}} {{repository_url}} {{master}}`

- Extraire un nouvel historique de projet de l'historique d'un sous-arbre:

`git subtree split --prefix={{path/to/directory/}} {{repository_url}} -b {{branch_name}}`
