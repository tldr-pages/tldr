# atool

> Különböző formátumú archívumok kezelése. További információ: <https://www.nongnu.org/atool/>.

- Fájlok listázása egy zip-archívumban:

`atool --list {{path/to/archive.zip}}`

- Egy tar.gz archívum kicsomagolása egy új alkönyvtárba (vagy az aktuális könyvtárba, ha csak egy fájlt tartalmaz):

`atool --extract {{path/to/archive.tar.gz}}`

- Új 7zip archívum létrehozása két fájlból:

`atool --add {{path/to/archive.7z}} {{path/to/file1 path/to/file2 ...}}`

- Az aktuális könyvtárban lévő összes zip és rar archívum kicsomagolása:

`atool --each --extract {{*.zip *.rar}}`
