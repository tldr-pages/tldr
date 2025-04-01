# az devops

> 管理 Azure DevOps 组织。
> 属于 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/devops>.

- 设置个人访问令牌 (PAT) 以登录到特定组织：

`az devops login --organization {{organization_url}}`

- 在浏览器中打开项目：

`az devops project show --project {{project_name}} --open`

- 列出特定项目中特定团队的成员：

`az devops team list-member --project {{project_name}} --team {{team_name}}`

- 检查 Azure DevOps CLI 当前配置：

`az devops configure --list`

- 通过设置默认项目和默认组织来配置 Azure DevOps CLI 行为：

`az devops configure --defaults project={{project_name}} organization={{organization_url}}`
