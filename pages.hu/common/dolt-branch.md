# dolt branch

> Dolt fiókok kezelése. További információ: <https://github.com/dolthub/dolt>.

- A helyi fiókok listája (az aktuális fiókot a `*` jelöli ki):

`dolt branch`

- Az összes helyi és távoli ág listázása:

`dolt branch --all`

- Új ág létrehozása az aktuális ág alapján:

`dolt branch {{branch_name}}`

- Új ág létrehozása a megadott commit-tal, mint a legfrissebbel:

`dolt branch {{branch_name}} {{commit}}`

- Ág átnevezése:

`dolt branch --move {{branch_name1}} {{branch_name2}}`

- Egy ág duplikálása:

`dolt branch --copy {{branch_name1}} {{branch_name2}}`

- ág törlése:

`dolt branch --delete {{branch_name}}`

- Az aktuális ág nevének megjelenítése:

`dolt branch --show-current`
