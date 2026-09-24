# az tag

> Gestisce i tag su una risorsa.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/tag>.

- Crea un valore di tag:

`az tag add-value {{[-n|--name]}} {{nome_tag}} --value {{valore_tag}}`

- Crea un tag nella sottoscrizione:

`az tag create {{[-n|--name]}} {{nome_tag}}`

- Elimina un tag dalla sottoscrizione:

`az tag delete {{[-n|--name]}} {{nome_tag}}`

- Elenca tutti i tag su una sottoscrizione:

`az tag list --resource-id /subscriptions/{{id_sottoscrizione}}`

- Elimina un valore di tag per un nome di tag specifico:

`az tag remove-value {{[-n|--name]}} {{nome_tag}} --value {{valore_tag}}`
