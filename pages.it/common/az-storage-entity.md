# az storage entity

> Gestisce le entità di archiviazione tabelle Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/storage/entity>.

- Inserisce un'entità in una tabella:

`az storage entity insert {{[-e|--entity]}} {{coppie_chiave_valore_separate_dallo_spazio}} {{[-t|--table-name]}} {{nome_tabella}} --account-name {{nome_account_archiviazione}} --account-key {{chiave_account_archiviazione}}`

- Elimina un'entità esistente da una tabella:

`az storage entity delete --partition-key {{chiave_partizione}} --row-key {{chiave_riga}} {{[-t|--table-name]}} {{nome_tabella}} --account-name {{nome_account_archiviazione}} --account-key {{chiave_account_archiviazione}}`

- Aggiorna un'entità esistente unendo le sue proprietà:

`az storage entity merge {{[-e|--entity]}} {{coppie_chiave_valore_separate_dallo_spazio}} {{[-t|--table-name]}} {{nome_tabella}} --account-name {{nome_account_archiviazione}} --account-key {{chiave_account_archiviazione}}`

- Elenca le entità che soddisfano una query:

`az storage entity query --filter {{filtro_query}} {{[-t|--table-name]}} {{nome_tabella}} --account-name {{nome_account_archiviazione}} --account-key {{chiave_account_archiviazione}}`

- Ottiene un'entità dalla tabella specificata:

`az storage entity show --partition-key {{chiave_partizione}} --row-key {{chiave_riga}} {{[-t|--table-name]}} {{nome_tabella}} --account-name {{nome_account_archiviazione}} --account-key {{chiave_account_archiviazione}}`
