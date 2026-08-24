# az storage blob

> Gestisce i container e gli oggetti di archiviazione blob in Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/storage/blob>.

- Scarica un blob in un percorso file specificando un container sorgente:

`az storage blob download --account-name {{nome_account}} --account-key {{chiave_account}} {{[-c|--container-name]}} {{nome_container}} {{[-n|--name]}} {{nome_blob}} {{[-f|--file]}} {{percorso/del/file}}`

- Scarica blob da un container blob in modo ricorsivo:

`az storage blob download-batch --account-name {{nome_account}} --account-key {{chiave_account}} {{[-s|--source]}} {{nome_container}} --pattern {{regex_nome_file}} {{[-d|--destination]}} {{percorso/della/destinazione}}`

- Carica un file locale nell'archiviazione blob:

`az storage blob upload --account-name {{nome_account}} --account-key {{chiave_account}} {{[-c|--container-name]}} {{nome_container}} {{[-n|--name]}} {{nome_blob}} {{[-f|--file]}} {{percorso/del/file}}`

- Elimina un oggetto blob:

`az storage blob delete --account-name {{nome_account}} --account-key {{chiave_account}} {{[-c|--container-name]}} {{nome_container}} {{[-n|--name]}} {{nome_blob}}`

- Genera una firma di accesso condiviso per un blob:

`az storage blob generate-sas --account-name {{nome_account}} --account-key {{chiave_account}} {{[-c|--container-name]}} {{nome_container}} {{[-n|--name]}} {{nome_blob}} --permissions {{insieme_permessi}} --expiry {{Y-m-d'T'H:M'Z'}} --https-only`
