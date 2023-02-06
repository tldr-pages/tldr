# apt-file

> Fájlok keresése az apt csomagokban, beleértve a még nem telepítetteket is. További információ: <https://manpages.debian.org/latest/apt-file/apt-file.1.html>.

- A metaadatok adatbázisának frissítése:

`sudo apt update`

- A megadott fájlt vagy elérési utat tartalmazó csomagok keresése:

`apt-file {{search|find}} {{partial_path/to/file}}`

- Egy adott csomag tartalmának listázása:

`apt-file {{show|list}} {{package_name}}`

- Olyan csomagok keresése, amelyek megfelelnek a `regular_expression`:

`apt-file {{search|find}} --regexp {{regular_expression}}`
