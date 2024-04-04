# az storage blob

> Manage blob storage containers and objects in Azure.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/storage/blob>.

- Download a blob to a [f]ile path specifying a [s]ource container:

`az storage blob download --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} -f {{path/to/local_file}}`

- [d]ownload blobs from a blob container recursively:

`az storage blob download-batch --account-name {{storage_account_name}} --account-key {{storage_account_key}} -s {{container_name}} -d {{path/to/remote}} --pattern {{filename_regex}} --destination {{path/to/destination}}`

- Upload a local file to blob storage:

`az storage blob upload --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} -f {{path/to/local_file}}`

- Delete a blob object:

`az storage blob delete --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}}`

- Generate a shared access signature for a blob:

`az storage blob generate-sas --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} --permissions {{permission_set}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`
