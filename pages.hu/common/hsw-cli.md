# hsw-cli

> A Handshake tárca parancssori REST eszköze. További információ: <https://github.com/handshake-org/hs-client>.

- Az aktuális tárca feloldása (időkorlát másodpercben):

`hsw-cli unlock {{passphrase}} {{timeout}}`

- Az aktuális tárca zárolása:

`hsw-cli lock`

- Az aktuális tárca adatainak megtekintése:

`hsw-cli get`

- Az aktuális tárca egyenlegének megtekintése:

`hsw-cli balance`

- Az aktuális pénztárca tranzakciós előzményeinek megtekintése:

`hsw-cli history`

- Tranzakció küldése a megadott érmeösszeggel egy címre:

`hsw-cli send {{address}} {{1.05}}`

- Az aktuális pénztárca függőben lévő tranzakcióinak megtekintése:

`hsw-cli pending`

- Egy tranzakció részleteinek megtekintése:

`hsw-cli tx {{transaction_hash}}`
