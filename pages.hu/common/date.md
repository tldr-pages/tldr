# date

> A rendszer dátumának beállítása vagy megjelenítése. További információ: <https://www.gnu.org/software/coreutils/date>.

- Az aktuális dátum megjelenítése az alapértelmezett területi formátummal:

`date +%c`

- Az aktuális dátum megjelenítése UTC-ben, az ISO 8601 formátumot használva:

`date -u +%Y-%m-%dT%H:%M:%S%Z`

- Az aktuális dátum megjelenítése Unix időbélyegzőként (másodpercek a Unix epocha óta):

`date +%s`

- A Unix időbélyegként megadott dátum átalakítása az alapértelmezett formátumba:

`date -d @{{1473305798}}`

- Egy megadott dátum átalakítása Unix időbélyeg formátumba:

`date -d "{{2018-09-01 00:00}}" +%s --utc`

- Az aktuális dátum megjelenítése az RFC-3339 formátumban (`YYYY-MM-DD hh:mm:ss TZ`):

`date --rfc-3339=s`

- Az aktuális dátum beállítása a `MMDDhhmmYYYY.ss` formátummal (`YYYY` és `.ss` opcionális):

`date {{093023592021.59}}`

- Az aktuális ISO-hét számának megjelenítése:

`date +%V`
