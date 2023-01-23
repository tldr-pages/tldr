# fselect

> Fájlok keresése SQL-szerű lekérdezésekkel. További információ: <https://github.com/jhspetersson/fselect>.

- Teljes elérési útvonal és méret kiválasztása egy adott könyvtárban lévő ideiglenes vagy konfigurációs fájlok közül:

`fselect size, path from {{path/to/directory}} where name = {{'*.cfg'}} or name = {{'*.tmp'}}`

- Négyzet alakú képek keresése:

`fselect path from {{path/to/directory}} where width = height`

- Old-school rap 320kbps MP3 fájlok keresése:

`fselect path from {{path/to/directory}} where genre = {{Rap}} and bitrate = {{320}} and mp3_year lt {{2000}}`

- Csak az első 5 találat kiválasztása és JSON-ként történő kimenet:

`fselect size, path from {{path/to/directory}} limit {{5}} into json`

- SQL összesítő függvények használata egy könyvtárban lévő fájlok minimális, maximális és átlagos méretének kiszámításához:

`fselect "{{MIN(size), MAX(size), AVG(size), SUM(size), COUNT(*)}} from {{path/to/directory}}"`
