# az pipelines

> Manage Azure Pipelines resources.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/pipelines>.

- Create a new Azure Pipeline (YAML based):

`az pipelines create {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}} --description {{description}} --repository {{repository_name}} --branch {{branch_name}}`

- Delete a specific pipeline:

`az pipelines delete {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --id {{pipeline_id}}`

- List pipelines:

`az pipelines list {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}}`

- Enqueue a specific pipeline to run:

`az pipelines run {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}}`

- Get the details of a specific pipeline:

`az pipelines show {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}}`

- Update a specific pipeline:

`az pipelines update {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}} --new-name {{pipeline_new_name}} --new-folder-path {{user1/production_pipelines}}`

- List all agents in a pool:

`az pipelines agent list {{[--org|--organization]}} {{organization_url}} --pool-id {{agent_pool}}`
