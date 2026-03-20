# az redis

> Gestisce le cache Redis.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/redis>.

- Crea una nuova istanza di cache Redis:

`az redis create --location {{posizione}} {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- Aggiorna una cache Redis:

`az redis update {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}} --sku {{Basic|Premium|Standard}} --vm-size {{c0|c1|c2|c3|c4|c5|c6|p1|p2|p3|p4|p5}}`

- Esporta i dati memorizzati in una cache Redis:

`az redis export --container {{container}} --file-format {{formato_file}} {{[-n|--name]}} {{nome}} --prefix {{prefisso}} {{[-g|--resource-group]}} {{gruppo_risorse}}`

- Elimina una cache Redis:

`az redis delete {{[-n|--name]}} {{nome}} {{[-g|--resource-group]}} {{gruppo_risorse}} {{[-y|--yes]}}`
