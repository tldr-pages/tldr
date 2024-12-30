# az repos

> 管理 Azure DevOps 仓库。
> 是 `azure-cli` 的一部分（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/repos>。

- 列出特定项目中的所有仓库：

`az repos list --project {{project_name}}`

- 在特定仓库的特定分支上添加策略以限制基本合并：

`az repos policy merge-strategy create --repository-id {{repository_id_in_repos_list}} --branch {{branch_name}} --blocking --enabled --allow-no-fast-forward false --allow-rebase true --allow-rebase-merge true --allow-squash true`

- 在特定仓库上添加构建验证，使用现有的构建管道，以便在源更新时自动触发：

`az repos policy build create --repository-id {{repository_id}} --build-definition-id {{build_pipeline_id}} --branch main --blocking --enabled --queue-on-source-update-only true --display-name {{name}} --valid-duration {{minutes}}`

- 列出特定项目中特定仓库的所有活动拉取请求：

`az repos pr list --project {{project_name}} --repository {{repository_name}} --status active`