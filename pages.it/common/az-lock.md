# az lock

> Gestisce i blocchi Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/lock>.

- Crea un blocco di livello sottoscrizione in sola lettura:

`az lock create {{[-n|--name]}} {{nome_blocco}} {{[-t|--lock-type]}} ReadOnly`

- Crea un blocco di livello gruppo di risorse in sola lettura:

`az lock create {{[-n|--name]}} {{nome_blocco}} {{[-g|--resource-group]}} {{nome_gruppo}} {{[-t|--lock-type]}} ReadOnly`

- Elimina un blocco di livello sottoscrizione:

`az lock delete {{[-n|--name]}} {{nome_blocco}}`

- Elimina un blocco di livello gruppo di risorse:

`az lock delete {{[-n|--name]}} {{nome_blocco}} {{[-g|--resource-group]}} {{nome_gruppo}}`

- Elenca tutti i blocchi a livello sottoscrizione:

`az lock list`

- Mostra un blocco di livello sottoscrizione con un nome specifico:

`az lock show {{[-n|--name]}} {{nome_blocco}}`
