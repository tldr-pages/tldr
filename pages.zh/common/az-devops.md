# az devops

> 管理 Azure DevOps 组织。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/devops>.

- 设置个人访问令牌（PAT）以登录到指定的组织：

`az devops login {{[--org|--organization]}} {{组织_url}}`

- 在浏览器中打开一个项目：

`az devops project show {{[-p|--project]}} {{项目名称}} --open`

- 列出在特定项目中工作的某个团队的成员：

`az devops team list-member {{[-p|--project]}} {{项目名称}} --team {{团队名称}}`

- 查看 Azure DevOps CLI 的当前配置：

`az devops configure {{[-l|--list]}}`

- 通过设置默认项目和默认组织来配置 Azure DevOps CLI 的行为：

`az devops configure {{[-d|--defaults]}} project={{项目名称}} organization={{组织_url}}`
