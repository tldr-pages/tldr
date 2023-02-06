# ffe

> A mezők kivonása egy sima adatbázis-fájlból és írása egy másik formátumba. A bemenet értelmezéséhez és a kimenet formázásához konfigurációs fájlra van szükség. További információ: <http://ff-extractor.sourceforge.net/ffe.html>.

- Az összes bemeneti adat megjelenítése a megadott adatkonfigurációval:

`ffe --configuration={{path/to/config.ffe}} {{path/to/input}}`

- Egy bemeneti fájl átalakítása egy új formátumú kimeneti fájlba:

`ffe --output={{path/to/output}} -c {{path/to/config.ffe}} {{path/to/input}}`

- A bemeneti struktúra és a nyomtatási formátum kiválasztása a `~/.fferc` konfigurációs fájlban található meghatározásokból:

`ffe --structure={{structure}} --print={{format}} {{path/to/input}}`

- Csak a kiválasztott mezők kiírása:

`ffe --field-list="{{FirstName,LastName,Age}}" -c {{path/to/config.ffe}} {{path/to/input}}`

- Csak a kifejezésnek megfelelő rekordok írása:

`ffe -e "{{LastName=Smith}}" -c {{path/to/config.ffe}} {{path/to/input}}`

- Súgó megjelenítése:

`ffe --help`
