# gt

> Függő kódmódosítások (stackek) sorozatainak létrehozása és kezelése a Git és a GitHub számára. További információ: <https://docs.graphite.dev>.

- A CLI hitelesítése a Graphite API-jával:

`gt auth --token {{graphite_cli_auth_token}}`

- A `gt` inicializálása az aktuális könyvtárban lévő adattárhoz:

`gt repo init`

- Új ág létrehozása az aktuális ág tetején halmozottan, és a halmozott változtatások átvitele:

`gt branch create {{branch_name}}`

- Hozzon létre egy új commitot és javítsa a felfelé halmozott ágakat:

`gt commit create -m {{commit_message}}`

- Az aktuális veremben lévő összes ág erőltetése a GitHub-ra, és PR-ok létrehozása vagy frissítése:

`gt stack submit`

- Naplózza az összes követett veremet:

`gt log short`

- Súgó nyomtatása egy megadott alparancshoz:

`gt {{subcommand}} --help`
