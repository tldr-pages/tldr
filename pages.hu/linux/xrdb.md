# xrdb

> Az X ablakszerver erőforrás-adatbázis segédprogramja Unix-szerű rendszerekhez. További információ: <https://www.x.org/releases/X11R7.7/doc/man/man1/xrdb.1.xhtml>.

- Indítsa el a `xrdb` oldalt interaktív módban:

`xrdb`

- Értékek (pl. stílusszabályok) betöltése egy erőforrásfájlból:

`xrdb -load {{~/.Xresources}}`

- Az erőforrás-adatbázis lekérdezése és az aktuálisan beállított értékek kinyomtatása:

`xrdb -query`
