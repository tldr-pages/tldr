# func

> Azure Functions alapvető eszközök: Azure Functions helyi fejlesztése és tesztelése. A helyi függvények csatlakozhatnak az Azure élő szolgáltatásaihoz, és egy függvényalkalmazást Azure-előfizetéshez telepíthetnek. További információ: <https://learn.microsoft.com/azure/azure-functions/functions-run-local>.

- Hozzon létre egy új functions projektet:

`func init {{project}}`

- Új függvény létrehozása:

`func new`

- Futtasson függvényeket helyben:

`func start`

- A kód közzététele egy Azure függvényalkalmazásban:

`func azure functionapp publish {{function}}`

- Minden beállítás letöltése egy meglévő függvényalkalmazásból:

`func azure functionapp fetch-app-settings {{function}}`

- Egy adott tárolófiókhoz tartozó kapcsolati karakterlánc lekérése:

`func azure storage fetch-connection-string {{storage_account}}`
