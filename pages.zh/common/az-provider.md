# az provider

> 管理资源提供者。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/provider>.

- 注册一个提供者：

`az provider register --namespace {{Microsoft.PolicyInsights}}`

- 注销一个提供者：

`az provider unregister --namespace {{Microsoft.Automation}}`

- 列出订阅的所有提供者：

`az provider list`

- 显示特定提供者的信息：

`az provider show --namespace {{Microsoft.Storage}}`

- 列出特定提供者的所有资源类型：

`az provider list --query "[?namespace=='{{Microsoft.Network}}'].resourceTypes[].resourceType"`
