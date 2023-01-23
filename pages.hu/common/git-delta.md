# git delta

> A másik ágtól eltérő fájlok listázása. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-delta>.

- Az aktuálisan ellenőrzött ág azon fájljainak listázása, amelyek eltérnek a `main` ágtól:

`git delta {{main}}`

- Egy adott ágból származó fájlok listázása, amelyek eltérnek egy másik adott ágtól:

`git delta {{branch_1}} {{branch_2}}`
