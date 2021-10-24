# git remote

> Organisation des dépôts suivis ("remotes").
> Plus d'informations : <https://git-scm.com/docs/git-remote>.

- Affiche les dépôts existants, leur nom et URL :

`git remote -v`

- Affiche les informations à propos d'un dépôt :

`git remote show {{nom_distant}}`

- Ajoute un dépôt :

`git remote add {{nom_distant}} {{url_distant}}`

- Change l'URL d'un dépôt (ajouter `--add` pour conserver l'URL existante) :

`git remote set-url {{nom_distant}} {{new_url}}`

- Supprime un dépôt :

`git remote remove {{nom_distant}}`

- Renomme un dépôt :

`git remote rename {{old_name}} {{new_name}}`
