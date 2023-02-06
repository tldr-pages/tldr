# isosize

> Az ISO-fájl méretének megjelenítése. További információ: <https://manned.org/isosize>.

- Az ISO-fájl méretének megjelenítése:

`isosize {{path/to/file.iso}}`

- Az ISO-fájl blokkszámának és blokkméretének megjelenítése:

`isosize --sectors {{path/to/file.iso}}`

- Az ISO-fájl méretének megjelenítése egy adott számmal osztva (csak akkor használható, ha a --sectors nincs megadva):

`isosize --divisor={{number}} {{path/to/file.iso}}`
