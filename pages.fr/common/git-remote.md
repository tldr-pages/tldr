# git remote

> Organisation des dépots suivis ("remotes").
> Plus d'informations : <https://git-scm.com/docs/git-remote>.

- Affiche les dépots existants, leur nom et url :

`git remote -v`

- Affiche les informations a propos d'un dépot :

`git remote show {{nom_distant}}`

- Ajoute un dépot :

`git remote add {{nom_distant}} {{url_distant}}`

- Change l'url d'un dépot (ajouter `--add` pour conserver l'url existante) :

`git remote set-url {{nom_distant}} {{new_url}}`

- Suprime un dṕot :

`git remote remove {{nom_distant}}`

- Renome un dépot :

`git remote rename {{old_name}} {{new_name}}`
