# ledger

> A Ledger egy nagy teljesítményű, kettős könyvelési rendszer, amely a UNIX parancssorból érhető el. További információ: <https://www.ledger-cli.org>.

- Nyomtasson ki egy egyenlegjelentést, amely az összegeket mutatja:

`ledger balance --file {{path/to/ledger.journal}}`

- Listázza ki a Költségek összes könyvelését összeg szerint rendezve:

`ledger register {{expenses}} --sorted {{amount}}`

- Nyomtassa ki az összes kiadást az Italok és ételek kivételével:

`ledger balance {{Expenses}} and not ({{Drinks}} or {{Food}})`

- Költségvetési jelentés nyomtatása:

`ledger budget`

- Összefoglaló információk nyomtatása az összes könyvelésről:

`ledger stats`
