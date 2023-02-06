# pnpx

> Az npm csomagokból származó binárisok közvetlen futtatása a `pnpm` használatával a `npm` helyett. További információ: <https://pnpm.io/pnpx-cli>.

- Egy adott npm modul binárisának végrehajtása:

`pnpx {{module_name}}`

- Egy adott npm modulból egy adott bináris futtatása, amennyiben a modulnak több binárisa is van:

`pnpx --package {{package_name}} {{module_name}}`

- Súgó megjelenítése:

`pnpx --help`
