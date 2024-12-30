# az 账户

> 管理 Azure 订阅信息。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/account>。

- 列出登录账户的所有订阅：

`az account list`

- 设置一个 `订阅` 为当前活动的订阅：

`az account set --subscription {{subscription_id}}`

- 列出当前活动订阅支持的区域：

`az account list-locations`

- 打印用于 `MS Graph API` 的访问令牌：

`az account get-access-token --resource-type {{ms-graph}}`

- 以特定格式打印当前活动订阅的详细信息：

`az account show --output {{json|tsv|table|yaml}}`