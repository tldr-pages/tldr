# az appconfig

> Gestisce le configurazioni App su Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/appconfig>.

- Crea una configurazione App:

`az appconfig create {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{nome_gruppo}} {{[-l|--location]}} {{posizione}}`

- Elimina una configurazione App specifica:

`az appconfig delete {{[-g|--resource-group]}} {{nome_rg}} {{[-n|--name]}} {{nome_appconfig}}`

- Elenca tutte le configurazioni App sotto la sottoscrizione corrente:

`az appconfig list`

- Elenca tutte le configurazioni App sotto un gruppo di risorse specifico:

`az appconfig list {{[-g|--resource-group]}} {{nome_rg}}`

- Mostra le proprietà di una configurazione App:

`az appconfig show {{[-n|--name]}} {{nome_appconfig}}`

- Aggiorna una configurazione App specifica:

`az appconfig update {{[-g|--resource-group]}} {{nome_rg}} {{[-n|--name]}} {{nome_appconfig}}`
