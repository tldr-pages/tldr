# azcopy

> Copy data to and from Azure Storage.
> See also: `az storage`.
> More information: <https://learn.microsoft.com/en-us/azure/storage/common/storage-use-azcopy-v10#list-of-commands>.

- Log in to an Azure Tenant:

`azcopy login`

- Upload a local file:

`azcopy {{[c|copy]}} '{{path/to/source_file}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}/{{blob_name}}'`

- Upload files with `.txt` and `.jpg` extensions:

`azcopy {{[c|copy]}} '{{path/to/source_directory}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --include-pattern '*.txt;*.jpg'`

- Copy a container directly between two Azure storage accounts:

`azcopy {{[c|copy]}} 'https://{{source_storage_account_name}}.blob.core.windows.net/{{container_name}}' 'https://{{destination_storage_account_name}}.blob.core.windows.net/{{container_name}}'`

- Synchronize a local directory and delete files in the destination if they no longer exist in the source:

`azcopy {{[s|sync]}} '{{path/to/source_directory}}' 'https://{{storage_account_name}}.blob.core.windows.net/{{container_name}}' --delete-destination true`

- Display help:

`azcopy {{[-h|--help]}}`
