# npx

> A `npm` csomagokból származó bináris programok végrehajtása. További információ: <https://github.com/npm/npx>.

- Egy adott npm modul binárisának futtatása:

`npx {{module_name}} {{command_arguments}}`

- Ha egy csomagnak több binárisa van, adja meg a csomag nevét a bináris mellett:

`npx --package {{package_name}} {{module_name}}`

- Futtasson egy parancsot, ha az létezik az aktuális elérési útvonalban vagy a `node_modules/.bin`:

`npx --no-install {{command}} {{command_arguments}}`

- Egy adott npm modul binárisának végrehajtása, elnyomva magának a `npx` kimenetét:

`npx --quiet {{module_name}} {{command_arguments}}`

- Súgó megjelenítése:

`npx --help`
