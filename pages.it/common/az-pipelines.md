# az pipelines

> Gestisce le risorse Azure Pipelines.
> Parte di `azure-cli` (noto anche come `az`).
> Maggiori informazioni: <https://learn.microsoft.com/cli/azure/pipelines>.

- Crea una nuova pipeline Azure (basata su YAML):

`az pipelines create {{[--org|--organization]}} {{url_organizzazione}} {{[-p|--project]}} {{nome_progetto}} --name {{nome_pipeline}} --description {{descrizione}} --repository {{nome_repository}} --branch {{nome_branch}}`

- Elimina una pipeline specifica:

`az pipelines delete {{[--org|--organization]}} {{url_organizzazione}} {{[-p|--project]}} {{nome_progetto}} --id {{id_pipeline}}`

- Elenca le pipeline:

`az pipelines list {{[--org|--organization]}} {{url_organizzazione}} {{[-p|--project]}} {{nome_progetto}}`

- Metti in coda una pipeline specifica per l'esecuzione:

`az pipelines run {{[--org|--organization]}} {{url_organizzazione}} {{[-p|--project]}} {{nome_progetto}} --name {{nome_pipeline}}`

- Ottiene i dettagli di una pipeline specifica:

`az pipelines show {{[--org|--organization]}} {{url_organizzazione}} {{[-p|--project]}} {{nome_progetto}} --name {{nome_pipeline}}`

- Aggiorna una pipeline specifica:

`az pipelines update {{[--org|--organization]}} {{url_organizzazione}} {{[-p|--project]}} {{nome_progetto}} --name {{nome_pipeline}} --new-name {{nome_pipeline_nuovo}} --new-folder-path {{user1/production_pipelines}}`

- Elenca tutti gli agenti in un pool:

`az pipelines agent list {{[--org|--organization]}} {{url_organizzazione}} --pool-id {{pool_agenti}}`
