# hsd-cli

> A Handshake blokklánc parancssori REST eszköze. További információ: <https://handshake.org>.

- Információk lekérése az aktuális szerverről:

`hsd-cli info`

- Helyi tranzakció közvetítése:

`hsd-cli broadcast {{transaction_hex}}`

- Egy mempool pillanatkép lekérdezése:

`hsd-cli mempool`

- Tranzakció megtekintése cím vagy hash alapján:

`hsd-cli tx {{address_or_hash}}`

- Egy érme megtekintése a hash indexe vagy címe alapján:

`hsd-cli coin {{hash_index_or_address}}`

- Blokkok megtekintése magasság vagy hash szerint:

`hsd-cli block {{height_or_hash}}`

- A lánc visszaállítása a megadott blokkra:

`hsd-cli reset {{height_or_hash}}`

- RPC-parancs végrehajtása:

`hsd-cli rpc {{command}} {{args}}`
