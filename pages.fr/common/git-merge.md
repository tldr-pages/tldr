# git merge

> Merge branches.
> Plus d'informations : <https://git-scm.com/docs/git-merge>.

- Merge une branche dans votre branche courrante :

`git merge {{nom_de_branche}}`

- Editer le message de merge :

`git merge -e {{nom_de_branche}}`

- Merge une branche et créer un commit de merge :

`git merge --no-ff {{nom_de_branche}}`

- Annuler un merge en cas de conflit :

`git merge --abort`

- Continuer un merge apreés une résolution de conflit :

`git merge --continue`
