# date

> A rendszer dátumának beállítása vagy megjelenítése. További információ: <https://ss64.com/osx/date.html>.

- Az aktuális dátum megjelenítése az alapértelmezett területi formátummal:

`date +%c`

- Az aktuális dátum megjelenítése UTC és ISO 8601 formátumban:

`date -u +%Y-%m-%dT%H:%M:%SZ`

- Az aktuális dátum megjelenítése Unix időbélyegzőként (másodpercek a Unix epocha óta):

`date +%s`

- Egy adott dátum megjelenítése (Unix időbélyegként) az alapértelmezett formátumban:

`date -r 1473305798`
