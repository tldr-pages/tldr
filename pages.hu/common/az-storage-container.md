# az storage container

> Blob tárolókonténerek kezelése az Azure-ban. A `azure-cli` webhely része. További információ: <https://learn.microsoft.com/cli/azure/storage/container>.

- Konténer létrehozása egy tárolófiókban:

`az storage container create --account-name {{storage_account_name}} --name {{container_name}} --public-access {{access_level}} --fail-on-exist`

- Hozzon létre egy megosztott hozzáférési aláírást a tárolóhoz:

`az storage container generate-sas --account-name {{storage_account_name}} --name {{container_name}} --permissions {{sas_permissions}} --expiry {{expiry_date}} --https-only`

- Konténerek listázása egy tárolófiókban:

`az storage container list --account-name {{storage_account_name}} --prefix {{filter_prefix}}`

- A megadott konténer törlésre jelölése:

`az storage container delete --account-name {{storage_account_name}} --name {{container_name}} --fail-not-exist`
