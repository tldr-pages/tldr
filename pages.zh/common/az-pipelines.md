# az pipelines

> 管理 Azure Pipelines 资源。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/pipelines>.

- 创建一个新的 Azure Pipeline（基于 YAML）：

`az pipelines create {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}} --description {{description}} --repository {{repository_name}} --branch {{branch_name}}`

- 删除指定的 Pipeline：

`az pipelines delete {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --id {{pipeline_id}}`

- 列出所有 Pipeline：

`az pipelines list {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}}`

- 将指定的 Pipeline 加入队列以运行：

`az pipelines run {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}}`

- 获取指定 Pipeline 的详细信息：

`az pipelines show {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}}`

- 更新指定的 Pipeline：

`az pipelines update {{[--org|--organization]}} {{organization_url}} {{[-p|--project]}} {{project_name}} --name {{pipeline_name}} --new-name {{pipeline_new_name}} --new-folder-path {{user1/production_pipelines}}`

- 列出某个池中的所有代理：

`az pipelines agent list {{[--org|--organization]}} {{organization_url}} --pool-id {{agent_pool}}`
