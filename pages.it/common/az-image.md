# az image

> Gestisce le immagini personalizzate di Virtual Machine in Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/image>.

- Elenca le immagini personalizzate sotto un gruppo di risorse:

`az image list {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Crea un'immagine personalizzata da dischi gestiti o snapshot:

`az image create {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome}} --os-type {{windows|linux}} --source {{sorgente_disco_os}}`

- Elimina un'immagine personalizzata:

`az image delete {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Mostra i dettagli di un'immagine personalizzata:

`az image show {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Aggiorna le immagini personalizzate:

`az image update {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}} --set {{proprietà=valore}}`
