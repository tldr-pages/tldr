# git sync

> Helyi ágak szinkronizálása távoli ágakkal. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-sync>.

- Az aktuális helyi ág szinkronizálása a távoli ággal:

`git sync`

- Az aktuális helyi ág szinkronizálása a távoli főággal:

`git sync origin main`

- Szinkronizálás a nem követett fájlok tisztítása nélkül:

`git sync -s {{remote_name}} {{branch_name}}`
