# az storage entity

> Manage Azure Table storage entities.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/storage/entity>.

- Insert an entity into a table:

`az storage entity insert --entity {{space_separated_key_value_pairs}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Delete an existing entity from a table:

`az storage entity delete --partition-key {{partition_key}} --row-key {{row_key}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Update an existing entity by merging its properties:

`az storage entity merge --entity {{space_separated_key_value_pairs}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- List entities which satisfy a query:

`az storage entity query --filter {{query_filter}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`

- Get an entity from the specified table:

`az storage entity show --partition-key {{partition_key}} --row-key {{row_key}} --table-name {{table_name}} --account-name {{storage_account_name}} --account-key {{storage_account_key}}`
