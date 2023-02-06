# git merge

> Ágak összevonása. További információ: <https://git-scm.com/docs/git-merge>.

- Egy ág beolvasztása az aktuális ágba:

`git merge {{branch_name}}`

- Szerkessze az egyesítési üzenetet:

`git merge -e {{branch_name}}`

- Egy ág összevonása és egy összevonási commit létrehozása:

`git merge --no-ff {{branch_name}}`

- Összefonódás megszakítása konfliktusok esetén:

`git merge --abort`
