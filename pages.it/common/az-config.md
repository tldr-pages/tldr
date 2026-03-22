# az config

> Gestisce la configurazione di Azure CLI.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/config>.

- Stampa tutte le configurazioni:

`az config get`

- Stampa le configurazioni per una sezione specifica:

`az config get {{nome_sezione}}`

- Imposta una configurazione:

`az config set {{nome_configurazione}}={{valore}}`

- Rimuove una configurazione:

`az config unset {{nome_configurazione}}`
