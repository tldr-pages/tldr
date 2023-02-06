# swagger-codegen

> Generálja a REST api kódját és dokumentációját egy OpenAPI/swagger definícióból. További információ: <https://github.com/swagger-api/swagger-codegen>.

- Dokumentáció és kód generálása egy OpenAPI/swagger fájlból:

`swagger-codegen generate -i {{swagger_file}} -l {{language}}`

- Java kód generálása a retrofit2 könyvtár és a useRxJava2 opció használatával:

`swagger-codegen generate -i {{http://petstore.swagger.io/v2/swagger.json}} -l {{java}} --library {{retrofit2}} -D{{useRxJava2}}={{true}}`

- Az elérhető nyelvek listája:

`swagger-codegen langs`

- A generate parancshoz tartozó súgóopciók megjelenítése:

`swagger-codegen help {{generate}}`
