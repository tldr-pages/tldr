# az advisor

> Gestisce le raccomandazioni e configurazioni Azure Advisor.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/advisor>.

- Elenca la configurazione Azure Advisor per l'intera sottoscrizione:

`az advisor configuration list`

- Mostra la configurazione Azure Advisor per la sottoscrizione o il gruppo di risorse specificato:

`az advisor configuration show {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Elenca le raccomandazioni Azure Advisor:

`az advisor recommendation list`

- Abilita le raccomandazioni Azure Advisor:

`az advisor recommendation enable {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Disabilita le raccomandazioni Azure Advisor:

`az advisor recommendation disable {{[-g|--resource-group]}} {{gruppo_risorse}}`
