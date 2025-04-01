# az pipelines

> 管理 Azure Pipelines 资源。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/pipelines>.

- 创建一个新的 Azure Pipeline（基于 YAML）：

`az pipelines create --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}} --description {{description}} --repository {{repository_name}} --branch {{branch_name}}`

- 删除特定的 pipeline：

`az pipelines delete --org {{organization_url}} --project {{project_name}} --id {{pipeline_id}}`

- 列出 pipelines：

`az pipelines list --org {{organization_url}} --project {{project_name}}`

- 将特定的 pipeline 排队执行：

`az pipelines run --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}}`

- 获取特定 pipeline 的详细信息：

`az pipelines show --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}}`

- 更新特定的 pipeline：

`az pipelines update --org {{organization_url}} --project {{project_name}} --name {{pipeline_name}} --new-name {{pipeline_new_name}} --new-folder-path {{user1/production_pipelines}}`

- 列出池中的所有代理：

`az pipelines agent list --org {{organization_url}} --pool-id {{agent_pool}}`
