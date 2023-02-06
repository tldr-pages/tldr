# typeorm

> Egy JavaScript ORM, amely Node.js, böngésző, Cordova, Ionic, React Native, NativeScript és Electron platformokon futtatható. További információ: <https://typeorm.io/>.

- Generáljon egy új kezdeti TypeORM projektstruktúrát:

`typeorm init`

- Hozzon létre egy üres migrációs fájlt:

`typeorm migration:create --name {{migration_name}}`

- Hozzon létre egy migrációs fájlt a séma frissítéséhez szükséges SQL utasításokkal:

`typeorm migration:generate --name {{migration_name}}`

- Futtassa le az összes függőben lévő migrációt:

`typeorm migration:run`

- Új entitásfájl létrehozása egy adott könyvtárban:

`typeorm entity:create --name {{entity}} --dir {{path/to/directory}}`

- A `typeorm schema:sync` által az alapértelmezett kapcsolaton végrehajtandó SQL utasítások megjelenítése:

`typeorm schema:log`

- Egy adott SQL-kijelentés végrehajtása az alapértelmezett kapcsolaton:

`typeorm query {{sql_sentence}}`

- Egy alparancs súgójának megjelenítése:

`typeorm {{subcommand}} --help`
