# git remote

> Organisation des dépots suivis ("remotes").
> Plus d'informations: <https://git-scm.com/docs/git-remote>.

- Affiche les dépots existants, leur nom et url:

`git remote -v`

- Affiche les informations a propos d'un dépot:

`git remote show {{remote_name}}`

- Ajoute un dépot:

`git remote add {{remote_name}} {{remote_url}}`

- Change l'url d'un dépot (ajouter `--add` pour conserver l'url existante):

`git remote set-url {{remote_name}} {{new_url}}`

- Suprime un dṕot:

`git remote remove {{remote_name}}`

- Renome un dépot:

`git remote rename {{old_name}} {{new_name}}`
