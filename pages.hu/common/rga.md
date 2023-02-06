# rga

> Ripgrep wrapper gazdag fájltípus keresési lehetőségekkel. További információ: <https://github.com/phiresky/ripgrep-all>.

- Rekurzívan keres egy mintát az aktuális könyvtár összes fájljában:

`rga {{regular_expression}}`

- Az elérhető adapterek listája:

`rga --rga-list-adapters`

- Módosíthatja a használni kívánt adaptereket (pl. ffmpeg, pandoc, poppler stb.):

`rga --rga-adapters={{adapter1,adapter2}} {{regular_expression}}`

- Minta keresése a fájlkiterjesztés helyett a mime típus alapján (lassabb):

`rga --rga-accurate {{regular_expression}}`

- Részletes súgó megjelenítése:

`rga --help`
