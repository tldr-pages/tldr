# mimetype

> Automatikusan meghatározza a fájl MIME típusát. További információ: <https://manned.org/mimetype>.

- Egy adott fájl MIME-típusának kinyomtatása:

`mimetype {{path/to/file}}`

- Csak a MIME-típust jeleníti meg, a fájlnevet nem:

`mimetype --brief {{path/to/file}}`

- A MIME típus leírásának megjelenítése:

`mimetype --describe {{path/to/file}}`

- A `stdin` MIME-típusának meghatározása (nem ellenőrzi a fájlnevet):

`{{some_command}} | mimetype --stdin`

- Hibakeresési információk megjelenítése a MIME típus meghatározásának módjáról:

`mimetype --debug {{path/to/file}}`

- Egy adott fájl összes lehetséges MIME-típusának megjelenítése bizalmi sorrendben:

`mimetype --all {{path/to/file}}`

- A kimenet kétbetűs nyelvi kódjának explicit megadása:

`mimetype --language {{path/to/file}}`
