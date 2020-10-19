# azcopy

> A file transfer tool for uploading to Azure Cloud Storage Accounts.
> More information: <https://docs.microsoft.com/azure/storage/common/storage-use-azcopy-v10>.

- Login to an Azure Tenant:

`azopy login`

- Upload a local file:

`azcopy copy '{{path/to/source/file}}' 'https://{{storage-account-name}}.blob.core.windows.net/{{container-name}}/{{blob-name}}'`

- Upload files with `.txt` and `.jpg` extensions:

`azcopy copy '{{path/to/source}}' 'https://{{storage-account-name}}.blob.core.windows.net/{{container-name}}' --include-pattern '{{*.txt;*.jpg}}'`

- Copy a container directly between two Azure storage accounts:

`azcopy copy 'https://{{source-storage-account-name}}.blob.core.windows.net/{{container-name}}' 'https://{{destination-storage-account-name}}.blob.core.windows.net/{{container-name}}'`

- Syncronise a local directory and delete files in the destination if they no longer exist in the source:

`azcopy sync '{{path/to/source}}' 'https://{{storage-account-name}}.blob.core.windows.net/{{container-name}}' --recursive --delete-destination=true`

- Display detailed usage information:

`azcopy --help`
