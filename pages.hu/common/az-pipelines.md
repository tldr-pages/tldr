# az pipelines

> Azure Pipelines erőforrások kezelése. A `azure-cli` webhely része. További információ: <https://learn.microsoft.com/cli/azure/pipelines>.

- Új Azure Pipeline létrehozása (YAML alapú):

`az pipelines create --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}} --description {{description}} --repository {{repository_name}} --branch {{branch_name}}`

- Egy adott csővezeték törlése:

`az pipelines delete --org {{organization_url}} --project {{project_name}} --id {{pipeline_id}}`

- Pipelines listázása:

`az pipelines list --org {{organization_url}} --project {{project_name}}`

- Egy adott csővezeték futtatásának sorba állítása:

`az pipelines run --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}}`

- Egy adott csővezeték részleteinek lekérdezése:

`az pipelines show --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}}`

- Egy adott csővezeték frissítése:

`az pipelines update --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}} --new-name {{pipeline_new_name}} --new-folder-path {{user1/production_pipelines}}`

- A csoportban lévő ügynökök listájának lekérdezése:

`az pipelines agent list --org {{organization_url}} --pool-id {{agent_pool}}`
