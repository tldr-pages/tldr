# az storage blob

> Blob tárolókonténerek és objektumok kezelése az Azure-ban. A `azure-cli` webhely része. További információ: <https://learn.microsoft.com/cli/azure/storage/blob>.

- Blob letöltése egy fájl elérési útvonalára:

`az storage blob download --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} -f {{path/to/local_file}}`

- Blobok letöltése egy blobkonténerből rekurzívan:

`az storage blob download-batch --account-name {{storage_account_name}} --account-key {{storage_account_key}} -s {{container_name}} -d {{path/to/remote}} --pattern {{filename_regex}} --destination {{path/to/destination}}`

- Helyi fájl feltöltése blobtárolóba:

`az storage blob upload --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} -f {{path/to/local_file}}`

- Blobobjektum törlése:

`az storage blob delete --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}}`

- Megosztott hozzáférési aláírás generálása egy blobhoz:

`az storage blob generate-sas --account-name {{storage_account_name}} --account-key {{storage_account_key}} -c {{container_name}} -n {{path/to/blob}} --permissions {{permission_set}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`
