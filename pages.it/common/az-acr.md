# az acr

> Gestisce i registri privati con Azure Container Registries.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/acr>.

- Crea un registro container gestito:

`az acr create {{[-n|--name]}} {{nome_registro}} {{[-g|--resource-group]}} {{gruppo_risorse}} --sku {{sku}}`

- Accedi a un registro:

`az acr login {{[-n|--name]}} {{nome_registro}}`

- Etichetta un'immagine locale per ACR:

`docker tag {{nome_immagine}} {{nome_registro}}.azurecr.io/{{nome_immagine}}:{{tag}}`

- Carica un'immagine su un registro:

`docker push {{nome_registro}}.azurecr.io/{{nome_immagine}}:{{tag}}`

- Scarica un'immagine da un registro:

`docker pull {{nome_registro}}.azurecr.io/{{nome_immagine}}:{{tag}}`

- Elimina un'immagine da un registro:

`az acr repository delete {{[-n|--name]}} {{nome_registro}} --repository {{nome_immagine}}:{{tag}}`

- Elimina un registro container gestito:

`az acr delete {{[-n|--name]}} {{nome_registro}} {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-y|--yes]}}`

- Elenca le immagini all'interno di un registro:

`az acr repository list {{[-n|--name]}} {{nome_registro}} --output table`
