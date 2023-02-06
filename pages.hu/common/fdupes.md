# fdupes

> Duplikált fájlok keresése egy adott könyvtárkészletben. További információ: <https://github.com/adrianlopezroche/fdupes>.

- Egyetlen könyvtár keresése:

`fdupes {{path/to/directory}}`

- Több könyvtár keresése:

`fdupes {{directory1}} {{directory2}}`

- Rekurzívan kereshet egy könyvtárban:

`fdupes -r {{path/to/directory}}`

- Több könyvtárban keresés, egy rekurzívan:

`fdupes {{directory1}} -R {{directory2}}`

- Rekurzív keresés és a duplikátumok hardlinkekkel való helyettesítése:

`fdupes -rH {{path/to/directory}}`

- Rekurzív keresés duplikátumok után, és interaktív kérés megjelenítése, hogy melyiket tartsa meg, a többit törölje:

`fdupes -rd {{path/to/directory}}`

- Rekurzív keresés és a duplikátumok törlése felszólítás nélkül:

`fdupes -rdN {{path/to/directory}}`
