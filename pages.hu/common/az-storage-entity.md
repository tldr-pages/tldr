# az storage entity

> Azure Table tárolási egységek kezelése. A `azure-cli` webhely része. További információ: <https://learn.microsoft.com/cli/azure/storage/entity>.

- Egy entitás beszúrása egy táblázatba:

`az storage entity insert --entity {{space_separated_key_value_pairs}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Meglévő entitás törlése egy táblából:

`az storage entity delete --partition-key {{partition_key}} --row-key {{row_key}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Meglévő entitás frissítése a tulajdonságainak összevonásával:

`az storage entity merge --entity {{space_separated_key_value_pairs}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Egy lekérdezésnek megfelelő entitások listázása:

`az storage entity query --filter {{query_filter}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Egy entitás kinyerése a megadott táblából:

`az storage entity show --partition-key {{partition_key}} --row-key {{row_key}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`
