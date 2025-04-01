# az tag

> 管理资源上的标签。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/tag>.

- 创建标签值：

`az tag add-value --name {{tag_name}} --value {{tag_value}}`

- 在订阅中创建标签：

`az tag create --name {{tag_name}}`

- 从订阅中删除标签：

`az tag delete --name {{tag_name}}`

- 列出订阅中的所有标签：

`az tag list --resource-id /subscriptions/{{subscription_id}}`

- 删除特定标签名称的标签值：

`az tag remove-value --name {{tag_name}} --value {{tag_value}}`