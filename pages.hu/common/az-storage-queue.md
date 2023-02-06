# az storage queue

> Tárolási várólisták kezelése az Azure-ban. A `azure-cli` webhely része. További információ: <https://learn.microsoft.com/cli/azure/storage/queue>.

- Hozzon létre egy várólistát:

`az storage queue create --account-name {{storage_account_name}} --name {{queue_name}} --metadata {{queue_metadata}}`

- Hozzon létre egy megosztott hozzáférési aláírást a várólistához:

`az storage queue generate-sas --account-name {{storage_account_name}} --name {{queue_name}} --permissions {{queue_permissions}} --expiry {{expiry_date}} --https-only`

- Listázza a tárolási fiókban lévő várólistákat:

`az storage queue list --prefix {{filter_prefix}} --account-name {{storage_account_name}}`

- A megadott várólista és a benne lévő üzenetek törlése:

`az storage queue delete --account-name {{storage_account_name}} --name {{queue_name}} --fail-not-exist`
