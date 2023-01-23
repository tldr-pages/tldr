# az storage table

> NoSQL kulcs-érték tárolás kezelése az Azure-ban. A `azure-cli` része. További információ: <https://learn.microsoft.com/cli/azure/storage/table>.

- Hozzon létre egy új táblát a tárolási fiókban:

`az storage table create --account-name {{storage_account_name}} --name {{table_name}} --fail-on-exist`

- Hozzon létre egy megosztott hozzáférési aláírást a táblához:

`az storage table generate-sas --account-name {{storage_account_name}} --name {{table_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --https-only`

- Táblák listázása a tárolási fiókban:

`az storage table list --account-name {{storage_account_name}}`

- A megadott tábla és a benne lévő adatok törlése:

`az storage table delete --account-name {{storage_account_name}} --name {{table_name}} --fail-not-exist`
