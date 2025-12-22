# az tag

> 管理资源上的标记。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/tag>.

- 创建一个标记值：

`az tag add-value {{[-n|--name]}} {{标记名称}} --value {{标记值}}`

- 在订阅中创建一个标记：

`az tag create {{[-n|--name]}} {{标记名称}}`

- 从订阅中删除一个标记：

`az tag delete {{[-n|--name]}} {{标记名称}}`

- 列出订阅中的所有标记：

`az tag list --resource-id /subscriptions/{{订阅 ID}}`

- 为指定的标记名称删除一个标记值：

`az tag remove-value {{[-n|--name]}} {{标记名称}} --value {{标记值}}`
