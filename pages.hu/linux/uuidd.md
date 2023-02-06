# uuidd

> UUID-k generálására szolgáló démon. További információ: <https://manned.org/uuidd>.

- Véletlenszerű UUID generálása:

`uuidd --random`

- Tömeges számú véletlen UUID generálása:

`uuidd --random --uuids {{number_of_uuids}}`

- Időalapú UUID generálása az aktuális idő és a rendszer MAC-címe alapján:

`uuidd --time`
