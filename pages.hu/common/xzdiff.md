# xzdiff

> A diff parancs meghívása xz, lzma, gzip, bzip2, lzop vagy zstd segítségével tömörített fájlokra. Minden megadott opciót közvetlenül a diff-nek ad át. További információ: https: [//manned.org/xzdiff](https://manned.org/xzdiff).

- Fájlok összehasonlítása:

`xzdiff {{path/to/file1}} {{path/to/file2}}`

- Fájlok összehasonlítása, a különbségek egymás melletti megjelenítése:

`xzdiff --side-by-side {{path/to/file1}} {{path/to/file2}}`

- Fájlok összehasonlítása, és csak azt jelenti, hogy különböznek (nincs részletezve, hogy miben különböznek):

`xzdiff --brief {{path/to/file1}} {{path/to/file2}}`

- Fájlok összehasonlítása és jelentés, ha a fájlok megegyeznek:

`xzdiff --report-identical-files {{path/to/file1}} {{path/to/file2}}`

- Fájlok összehasonlítása oldalszámozott eredményekkel:

`xzdiff --paginate {{path/to/file1}} {{path/to/file2}}`

- Könyvtárak rekurzív összehasonlítása (megmutatja az eltérő fájlok/könyvtárak nevét, valamint a fájlokban végrehajtott változtatásokat):

`diff --recursive {{path/to/file1}} {{path/to/file2}}`
