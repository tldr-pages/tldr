# git merge

> Pour fusionner des branches `git`.
> Plus d'informations : <https://git-scm.com/docs/git-merge>.

- Fusionne une branche dans votre branche courante :

`git merge {{nom_de_branche}}`

- Editer le message de fusion (`merge commit`) :

`git merge --edit {{nom_de_branche}}`

- Fusionner une branche et créer un commit de fusion (`merge commit`) :

`git merge --no-ff {{nom_de_branche}}`

- Annuler une fusion en cas de conflit :

`git merge --abort`
