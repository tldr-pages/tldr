# git annex

> Fájlok kezelése Git-tel, a tartalmuk ellenőrzése nélkül. Amikor egy fájlt csatolunk, a tartalma egy kulcs-érték tárolóba kerül, és egy symlink készül, amely a tartalomra mutat. További információ: <https://git-annex.branchable.com>.

- Segítség:

`git annex help`

- Egy repo inicializálása Git annex segítségével:

`git annex init`

- Fájl hozzáadása:

`git annex add {{path/to/file_or_directory}}`

- Egy fájl vagy könyvtár aktuális állapotának megjelenítése:

`git annex status {{path/to/file_or_directory}}`

- Helyi tároló szinkronizálása egy távolival:

`git annex {{remote}}`

- Egy fájl vagy könyvtár lekérdezése:

`git annex get {{path/to/file_or_directory}}`
