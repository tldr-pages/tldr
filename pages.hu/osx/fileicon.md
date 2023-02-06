# fileicon

> Egy macOS CLI az egyéni fájl- és mappaikonok kezeléséhez. További információ: <https://github.com/mklement0/fileicon>.

- Egyéni ikon beállítása egy adott fájlhoz vagy könyvtárhoz:

`fileicon set {{path/to/file_or_directory}} {{path/to/icon.png}}`

- Egyéni ikon eltávolítása egy adott fájlról vagy könyvtárról:

`fileicon rm {{path/to/file_or_directory}}`

- Egy fájl vagy könyvtár egyéni ikonjának mentése `.icns` fájlként az aktuális könyvtárba:

`fileicon get {{path/to/file_or_directory}}`

- Annak tesztelése, hogy egy adott fájl vagy könyvtár rendelkezik-e egyéni ikonnal:

`fileicon test {{path/to/file_or_directory}}`
