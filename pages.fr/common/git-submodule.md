# git submodule

> Inspecter, mettre à jour et manager des sous-modules.
> Plus d'informations : <https://git-scm.com/docs/git-submodule>.

- Installer un sous-module depuis le dépôt courant :

`git submodule update --init --recursive`

- Ajout d'un dépôt Git en tant que sous-module :

`git submodule add {{repository_url}}`

- Ajout d'un dépôt Git en tant que sous-module à un répertoire donné :

`git submodule add {{repository_url}} {{chemin/vers/repertoire}}`

- Mettre à jour tout les sous-modules à leur dernier commit :

`git submodule foreach git pull`
