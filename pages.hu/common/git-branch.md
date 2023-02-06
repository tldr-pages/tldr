# git branch

> A Git fő parancsa az ágakkal való munkához. További információ: <https://git-scm.com/docs/git-branch>.

- Az összes ág listázása (helyi és távoli ágak; az aktuális ágat kiemeli a `*`):

`git branch --all`

- Annak listázása, hogy mely ágak tartalmaznak egy adott Git commitot az előzmények között:

`git branch --all --contains {{commit_hash}}`

- Az aktuális ág nevének megjelenítése:

`git branch --show-current`

- Új ág létrehozása az aktuális commit alapján:

`git branch {{branch_name}}`

- Új ág létrehozása egy adott commit alapján:

`git branch {{branch_name}} {{commit_hash}}`

- Ág átnevezése (ehhez nem szabad, hogy ki legyen jelölve):

`git branch -m {{old_branch_name}} {{new_branch_name}}`

- Helyi ág törlése (ehhez nem szabad, hogy ki legyen jelölve):

`git branch -d {{branch_name}}`

- Távoli ág törlése:

`git push {{remote_name}} --delete {{remote_branch_name}}`
