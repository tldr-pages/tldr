# az repos

> 管理 Azure DevOps 仓库。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/repos>.

- 列出特定项目中的所有仓库：

`az repos list {{[-p|--project]}} {{project_name}}`

- 在特定仓库的特定分支上添加策略，以限制基本的合并方式：

`az repos policy merge-strategy create --repository-id {{仓库列表中的仓库 ID}} --branch {{分支名称}} --blocking --enabled --allow-no-fast-forward false --allow-rebase true --allow-rebase-merge true --allow-squash true`

- 在特定仓库上添加构建验证，使用现有的构建管道，在源代码更新时自动触发：

`az repos policy build create --repository-id {{repository_id}} --build-definition-id {{构建管道 ID}} --branch main --blocking --enabled --queue-on-source-update-only true --display-name {{名称}} --valid-duration {{分钟}}`

- 列出特定项目中某个仓库的所有处于活动状态的拉取请求：

`az repos pr list {{[-p|--project]}} {{project_name}} {{[-r|--repository]}} {{repository_name}} --status active`
