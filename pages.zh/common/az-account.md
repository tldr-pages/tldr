# az account

> 管理 Azure 订阅信息。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/account>。

- 列出登录帐户的所有订阅：

`az account list`

- 设置一个 `subscription` 为当前活动订阅：

`az account set --subscription {{subscription_id}}`

- 列出当前活动订阅支持的区域：

`az account list-locations`

- 打印用于 `MS Graph API` 的访问令牌：

`az account get-access-token --resource-type {{ms-graph}}`

- 以特定格式打印当前活动订阅的详细信息：

`az account show --output {{json|tsv|table|yaml}}`