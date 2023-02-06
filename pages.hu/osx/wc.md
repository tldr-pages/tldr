# wc

> Sorok, szavak vagy bájtok számolása. További információ: <https://ss64.com/osx/wc.html>.

- Sorok számolása a fájlban:

`wc -l {{path/to/file}}`

- Szavak számolása a fájlban:

`wc -w {{path/to/file}}`

- Karakterek (bájtok) számolása a fájlban:

`wc -c {{path/to/file}}`

- Karakterek számolása a fájlban (több bájtos karakterkészleteket figyelembe véve):

`wc -m {{path/to/file}}`

- A szabványos bemenet használatával a sorok, szavak és karakterek (bájtok) számolása ebben a sorrendben:

`{{find .}} | wc`
