# az disk

> Gestisce i dischi gestiti Azure.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/disk>.

- Crea un disco gestito:

`az disk create {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome_disco}} {{[-z|--size-gb]}} {{dimensione_gb}}`

- Elenca i dischi gestiti in un gruppo di risorse:

`az disk list {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Elimina un disco gestito:

`az disk delete {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome_disco}}`

- Concede accesso di lettura o scrittura a un disco gestito (per esportazione):

`az disk grant-access {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome_disco}} {{[--access|--access-level]}} {{Read|Write}} --duration-in-seconds {{secondi}}`

- Aggiorna la dimensione del disco:

`az disk update {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-n|--name]}} {{nome_disco}} {{[-z|--size-gb]}} {{nuova_dimensione_gb}}`
