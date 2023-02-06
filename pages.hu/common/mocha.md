# mocha

> A Mocha JavaScript tesztfutó futtatása. További információ: <https://mochajs.org>.

- A tesztek futtatása alapértelmezett konfigurációval vagy a `mocha.opts` oldalon megadottak szerint:

`mocha`

- Egy adott helyen található tesztek futtatása:

`mocha {{directory/with/tests}}`

- Egy adott grep mintának megfelelő tesztek futtatása:

`mocha --grep {{regular_expression}}`

- Az aktuális könyvtárban lévő JavaScript-fájlok változásaira vonatkozó tesztek futtatása és egyszeri kezdeti futtatása:

`mocha --watch`

- Tesztek futtatása egy adott bejelentővel:

`mocha --reporter {{reporter}}`
