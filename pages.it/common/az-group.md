# az group

> Gestisce i gruppi di risorse e le distribuzioni di template.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/group>.

- Crea un nuovo gruppo di risorse:

`az group create {{[-n|--name]}} {{nome}} {{[-l|--location]}} {{posizione}}`

- Verifica se un gruppo di risorse esiste:

`az group exists {{[-n|--name]}} {{nome}}`

- Elimina un gruppo di risorse:

`az group delete {{[-n|--name]}} {{nome}}`

- Aspetta fino a quando una condizione del gruppo di risorse è soddisfatta:

`az group wait {{[-n|--name]}} {{nome}} --{{created|deleted|exists|updated}}`
