# az logicapp

> Gestisce le Logic Apps nei servizi cloud Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/logicapp>.

- Crea una logic app:

`az logicapp create {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-s|--storage-account]}} {{account_archiviazione}}`

- Elimina una logic app:

`az logicapp delete {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Elenca le logic app:

`az logicapp list {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Riavvia una logic app:

`az logicapp restart {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Avvia una logic app:

`az logicapp start {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Ferma una logic app:

`az logicapp stop {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`
