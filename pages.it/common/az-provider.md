# az provider

> Gestisce i provider di risorse.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/provider>.

- Registra un provider:

`az provider register {{[-n|--namespace]}} {{Microsoft.PolicyInsights}}`

- Annulla la registrazione di un provider:

`az provider unregister {{[-n|--namespace]}} {{Microsoft.Automation}}`

- Elenca tutti i provider per una sottoscrizione:

`az provider list`

- Mostra informazioni su un provider specifico:

`az provider show {{[-n|--namespace]}} {{Microsoft.Storage}}`

- Elenca tutti i tipi di risorse per un provider specifico:

`az provider list --query "[?namespace=='{{Microsoft.Network}}'].resourceTypes[].resourceType"`
