# az storage blob

> Manage blob storage containers and objects in Azure.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/storage/blob>.

- Download a blob to a file path specifying a source container:

`az storage blob download --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{blob_name}} {{[-f|--file]}} {{path/to/file}}`

- Download blobs from a blob container recursively:

`az storage blob download-batch --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-s|--source]}} {{container_name}} --pattern {{filename_regex}} {{[-d|--destination]}} {{path/to/destination}}`

- Upload a local file to blob storage:

`az storage blob upload --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{blob_name}} {{[-f|--file]}} {{path/to/file}}`

- Delete a blob object:

`az storage blob delete --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{blob_name}}`

- Generate a shared access signature for a blob:

`az storage blob generate-sas --account-name {{storage_account_name}} --account-key {{storage_account_key}} {{[-c|--container-name]}} {{container_name}} {{[-n|--name]}} {{blob_name}} --permissions {{permission_set}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`
