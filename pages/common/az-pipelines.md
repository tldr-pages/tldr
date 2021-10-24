# az pipelines

> Manage Azure Pipelines resources.
> Part of `azure-cli`.
> More information: <https://docs.microsoft.com/cli/azure/pipelines>.

- Queue (run) a pipeline:

`az pipelines run --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}}`

- Get a list of agents in a pool:

`az pipelines agent list --org {{organization_url}} --pool-id {{agent_pool}}`

- List build definitions:

`az pipelines build definition list --org {{organization_url}} --project {{project_name}}`
