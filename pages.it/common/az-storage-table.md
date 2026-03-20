# az storage table

> Gestisce l'archiviazione NoSQL chiave-valore in Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/storage/table>.

- Crea una nuova tabella nell'account di archiviazione:

`az storage table create --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_tabella}} --fail-on-exist`

- Genera una firma di accesso condiviso per la tabella:

`az storage table generate-sas --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_tabella}} --permissions {{permessi_sas}} --expiry {{data_scadenza}} --https-only`

- Elenca le tabelle in un account di archiviazione:

`az storage table list --account-name {{nome_account_archiviazione}}`

- Elimina la tabella specificata e tutti i dati che contiene:

`az storage table delete --account-name {{nome_account_archiviazione}} {{[-n|--name]}} {{nome_tabella}} --fail-not-exist`
