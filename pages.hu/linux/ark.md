# ark

> A KDE archiváló eszköze. További információ: <https://docs.kde.org/stable5/en/ark/ark/>.

- Egy adott archívum kicsomagolása az aktuális könyvtárba:

`ark --batch {{path/to/archive}}`

- Egy archívum kibontása egy adott könyvtárba:

`ark --batch --destination {{path/to/directory}} {{path/to/archive}}`

- Létrehoz egy archívumot, ha az nem létezik, és hozzáad bizonyos fájlokat:

`ark --add-to {{path/to/archive}} {{path/to/file1 path/to/file2 ...}}`
