# mv

> Fájlok és könyvtárak áthelyezése vagy átnevezése. További információ: <https://www.gnu.org/software/coreutils/mv>.

- Fájl vagy könyvtár átnevezése, ha a cél nem egy meglévő könyvtár:

`mv {{source}} {{target}}`

- Fájl vagy könyvtár áthelyezése egy meglévő könyvtárba:

`mv {{source}} {{existing_directory}}`

- Több fájl áthelyezése egy meglévő könyvtárba, a fájlnevek változatlanul hagyásával:

`mv {{source1}} {{source2}} {{source3}} {{existing_directory}}`

- A meglévő fájlok felülírása előtt ne kérjen megerősítést:

`mv -f {{source}} {{target}}`

- Megerősítés kérése a meglévő fájlok felülírása előtt, függetlenül a fájljogosultságoktól:

`mv -i {{source}} {{target}}`

- Ne írja felül a meglévő fájlokat a célponton:

`mv -n {{source}} {{target}}`

- Fájlok áthelyezése szóbeli üzemmódban, a fájlok megjelenítése a fájlok áthelyezése után:

`mv -v {{source}} {{target}}`
