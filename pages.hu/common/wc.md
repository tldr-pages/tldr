# wc

> Sorok, szavak és bájtok számolása. További információ: <https://www.gnu.org/software/coreutils/wc>.

- Egy fájl összes sorának megszámlálása:

`wc --lines {{path/to/file}}`

- Számolja az összes szót egy fájlban:

`wc --words {{path/to/file}}`

- Számolja az összes bájtot egy fájlban:

`wc --bytes {{path/to/file}}`

- Az összes karakter megszámlálása egy fájlban (a több bájtos karakterek figyelembevételével):

`wc --chars {{path/to/file}}`

- Az összes sor, szó és bájt megszámlálása a `stdin` oldalról:

`{{find .}} | wc`

- Számolja meg a leghosszabb sor hosszát karakterekben:

`wc --max-line-length {{path/to/file}}`
