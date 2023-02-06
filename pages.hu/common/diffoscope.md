# diffoscope

> Fájlok, archívumok és könyvtárak összehasonlítása. További információ: <https://diffoscope.org>.

- Két fájl összehasonlítása:

`diffoscope {{path/to/file1}} {{path/to/file2}}`

- Két fájl összehasonlítása haladásjelző megjelenítése nélkül:

`diffoscope --no-progress {{path/to/file1}} {{path/to/file2}}`

- Két fájl összehasonlítása és HTML-jelentés írása egy fájlba (használja a `-` címet a `stdout`):

`diffoscope --html {{path/to/outfile|-}} {{path/to/file1}} {{path/to/file2}}`

- Két könyvtár összehasonlítása a megadott mintának megfelelő nevű fájlok kizárásával:

`diffoscope --exclude {{pattern}} {{path/to/directory1}} {{path/to/directory2}}`

- Két könyvtár összehasonlítása és annak ellenőrzése, hogy a könyvtár metaadatait figyelembe vegye-e:

`diffoscope --exclude-directory-metadata {{auto|yes|no|recursive}} {{path/to/directory1}} {{path/to/directory2}}`
