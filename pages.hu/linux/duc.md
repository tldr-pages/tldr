# duc

> A Duc egy eszközgyűjtemény a lemezhasználat indexeléséhez, vizsgálatához és megjelenítéséhez. A Duc egy adatbázist tart fenn a fájlrendszer könyvtárainak felhalmozott méreteiről, lehetővé téve az adatbázis lekérdezését, vagy díszes grafikonok létrehozását az adatok helyének bemutatására. További információ: <https://duc.zevv.nl/>.

- Indexelje az /usr könyvtárat, az alapértelmezett adatbázis helyére ~/.duc.db írva:

`duc index {{/usr}}`

- Az /usr/local alatt található összes fájl és könyvtár listázása, a relatív fájlméretek \[g\]rafban való feltüntetésével:

`duc ls --classify --graph {{/usr/local}}`

- Az /usr/local alatt található összes fájl és könyvtár listázása rekurzívan a treeview segítségével:

`duc ls --classify --graph --recursive {{/usr/local}}`

- A grafikus felület elindítása a fájlrendszer felfedezéséhez sunburst grafikonok segítségével:

`duc gui {{/usr}}`

- Az ncurses konzolos felület futtatása a fájlrendszer felfedezéséhez:

`duc ui {{/usr}}`

- Adatbázis-információk kiürítése:

`duc info`
