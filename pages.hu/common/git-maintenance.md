# git-maintenance

> Feladatok futtatása a Git-repository adatok optimalizálására. További információ: <https://git-scm.com/docs/git-maintenance>.

- Regisztrálja az aktuális adattárat a felhasználó adattárak listáján, hogy naponta futtassa a karbantartást:

`git maintenance register`

- Karbantartás futtatásának elindítása az aktuális tárolóhelyen:

`git maintenance start`

- Állítsa le az aktuális tárolóhely háttérben futó karbantartási ütemezését:

`git maintenance stop`

- Az aktuális tároló eltávolítása a felhasználó karbantartási tárolólistájáról:

`git maintenance unregister`

- Egy adott karbantartási feladat futtatása az aktuális tárolón:

`git maintenance run --task={{commit-graph|gc|incremental-repack|loose-objects|pack-refs|prefetch}}`
