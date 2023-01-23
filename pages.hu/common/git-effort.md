# git effort

> Megjeleníti, hogy mennyi aktivitás volt egy fájlban, fájlonként mutatja a commitokat és az "aktív napokat", azaz a fájlhoz hozzájáruló napok számát. A `git-extras` része. További információ: <https://github.com/tj/git-extras/blob/master/Commands.md#git-effort>.

- A tároló minden egyes fájljának megjelenítése, a commitok és az aktív napok feltüntetésével:

`git effort`

- Meghatározott számú vagy több commit által módosított fájlok megjelenítése, a commitok és az aktív napok feltüntetésével:

`git effort --above {{5}}`

- Egy adott szerző által módosított fájlok megjelenítése, a commitok és az aktív napok feltüntetésével:

`git effort -- --author="{{username}}"`

- Meghatározott időpont/dátum óta módosított fájlok megjelenítése, a commitok és az aktív napok feltüntetésével:

`git effort -- --since="{{last month}}"`

- Csak a megadott fájlok vagy könyvtárak megjelenítése, commitok és aktív napok megjelenítése:

`git effort {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Egy adott könyvtár összes fájljának megjelenítése, a commitok és az aktív napok megjelenítése:

`git effort {{path/to/directory/*}}`
