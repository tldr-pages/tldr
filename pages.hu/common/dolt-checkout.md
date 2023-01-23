# dolt checkout

> A munkafa vagy a táblázatok megtekintése egy adott ághoz vagy commithoz. További információ: <https://github.com/dolthub/dolt>.

- Egy ágra váltás:

`dolt checkout {{branch_name}}`

- Visszavonni egy táblázat még el nem végzett módosításait:

`dolt checkout {{table}}`

- Új ág létrehozása és váltás rá:

`dolt checkout -b {{branch_name}}`

- Új ág létrehozása egy megadott commit alapján és váltás rá:

`dolt checkout -b {{branch_name}} {{commit}}`
