# unison

> Kétirányú fájlszinkronizáló eszköz. További információ: <https://www.cis.upenn.edu/~bcpierce/unison/download/releases/stable/unison-manual.html>.

- Két könyvtár szinkronizálása (a két könyvtár szinkronizálásakor először naplót készít):

`unison {{path/to/directory_1}} {{path/to/directory_2}}`

- Automatikusan elfogadja az (egymással nem ütköző) alapértelmezéseket:

`unison {{path/to/directory_1}} {{path/to/directory_2}} -auto`

- Néhány fájl figyelmen kívül hagyása egy minta segítségével:

`unison {{path/to/directory_1}} {{path/to/directory_2}} -ignore {{pattern}}`

- Dokumentáció megjelenítése:

`unison -doc {{topics}}`
