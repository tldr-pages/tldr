# az storage queue

> Manage storage queues in Azure.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/storage/queue>.

- Create a queue:

`az storage queue create --account-name {{storage_account_name}} --name {{queue_name}} --metadata {{queue_metadata}}`

- Generate a shared access signature for the queue:

`az storage queue generate-sas --account-name {{storage_account_name}} --name {{queue_name}} --permissions {{queue_permissions}} --expiry {{expiry_date}} --https-only`

- List queues in a storage account:

`az storage queue list --prefix {{filter_prefix}} --account-name {{storage_account_name}}`

- Delete the specified queue and any messages it contains:

`az storage queue delete --account-name {{storage_account_name}} --name {{queue_name}} --fail-not-exist`
