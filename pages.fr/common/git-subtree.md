# git subtree

> Fusionne des sous-arbres ou divise un dépôt en sous-arbres.
> Plus d'informations : <https://manned.org/git-subtree>.

- Ajoute un dépôt Git en tant que sous-arbre et fusionne les validations:

`git subtree add {{[-P|--prefix]}} {{chemin/vers/répertoire}} --squash {{url_dépôt}} {{nom_branche}}`

- Met à jour le sous-arbre avec son dernier commit :

`git subtree pull {{[-P|--prefix]}} {{chemin/vers/répertoire}} {{url_dépôt}} {{nom_branche}}`

- Fusionne les modifications récentes jusqu'au dernier commit du sous-arbre dans le sous-arbre :

`git subtree merge {{[-P|--prefix]}} {{chemin/vers/répertoire}} --squash {{url_dépôt}} {{nom_branche}}`

- Pousse les commits vers le dépôt d'un sous-arbre :

`git subtree push {{[-P|--prefix]}} {{chemin/vers/répertoire}} {{url_dépôt}} {{nom_branche}}`

- Extrait un nouvel historique de projet de l'historique d'un sous-arbre :

`git subtree split {{[-P|--prefix]}} {{chemin/vers/répertoire}} {{url_dépôt}} {{[-b|--branch]}} {{nom_branche}}`
