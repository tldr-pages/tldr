# az apim

> Gestisce i servizi Azure API Management.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/apim>.

- Elenca i servizi API Management all'interno di un gruppo di risorse:

`az apim list {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Crea un'istanza di servizio API Management:

`az apim create {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}} --publisher-email {{email}} --publisher-name {{nome}}`

- Elimina un servizio API Management:

`az apim delete {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Mostra i dettagli di un'istanza di servizio API Management:

`az apim show {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Aggiorna un'istanza di servizio API Management:

`az apim update {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`
