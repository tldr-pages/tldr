# webstorm

> A JetBrains JavaScript IDE. További információ: <https://www.jetbrains.com/help/webstorm/working-with-the-ide-features-from-command-line.html>.

- Nyissa meg az aktuális könyvtárat a WebStormban:

`webstorm`

- Egy adott könyvtár megnyitása a WebStormban:

`webstorm {{path/to/directory}}`

- Meghatározott fájlok megnyitása LightEdit módban:

`webstorm -e {{path/to/file1 path/to/file2 ...}}`

- Megnyitás és várakozás egy adott fájl szerkesztésének befejezéséig a LightEdit módban:

`webstorm --wait -e {{path/to/file}}`

- Fájl megnyitása úgy, hogy a kurzor az adott soron áll:

`webstorm --line {{line_number}} {{path/to/file}}`

- Fájlok megnyitása és összehasonlítása (legfeljebb 3 fájl megnyitásáig támogatja):

`webstorm diff {{path/to/file1}} {{path/to/file2}}`

- Megnyitás és hármas egyesítés végrehajtása:

`webstorm merge {{path/to/left_file}} {{path/to/right_file}} {{path/to/target_file}}`
