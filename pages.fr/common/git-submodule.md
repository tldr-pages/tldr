# git submodule

> Inspecter, metre a jour et manager des sous modules.
> Plus d'informations : <https://git-scm.com/docs/git-submodule>.

- Installer un submodule depuis le dépot courrant :

`git submodule update --init --recursive`

- Ajout d'un dépot Git en tant que sous module :

`git submodule add {{repository_url}}`

- Ajout d'un dépot Git en tant que sous module a répertoire donné :

`git submodule add {{repository_url}} {{chemin/vers/repertoire}}`

- Metre à jour tout les sous modules à leurs derniers commit :

`git submodule foreach git pull`
