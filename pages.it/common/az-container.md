# az container

> Gestisce le istanze Azure Container.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/container>.

- Crea un contenitore in un gruppo di contenitori:

`az container create {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome}} --image {{nome_immagine}} {{[-os|--os-type]}} {{windows|linux}} --cpu {{numero_core_cpu}} --memory {{memoria_GB}}`

- Esegue un comando da un contenitore in esecuzione di un gruppo di contenitori:

`az container exec {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome_gruppo_contenitori}} --exec-command "{{comando}}"`

- Esamina i log di un contenitore in un gruppo di contenitori:

`az container logs {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Ottiene i dettagli di un gruppo di contenitori:

`az container show {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Avvia tutti i contenitori in un gruppo di contenitori:

`az container start {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Ferma tutti i contenitori in un gruppo di contenitori:

`az container stop {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Elimina un gruppo di contenitori:

`az container delete {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}}`
