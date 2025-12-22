# az provider

> 管理资源提供程序。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/provider>.

- 注册一个提供程序：

`az provider register {{[-n|--namespace]}} {{Microsoft.PolicyInsights}}`

- 取消注册一个提供程序：

`az provider unregister {{[-n|--namespace]}} {{Microsoft.Automation}}`

- 列出订阅中的所有提供程序：

`az provider list`

- 显示特定提供程序的信息：

`az provider show {{[-n|--namespace]}} {{Microsoft.Storage}}`

- 列出特定提供程序的所有资源类型：

`az provider list --query "[?namespace=='{{Microsoft.Network}}'].resourceTypes[].resourceType"`
