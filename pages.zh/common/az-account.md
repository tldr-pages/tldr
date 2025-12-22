# az account

> 管理 Azure 订阅信息。
> 属于 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/account>.

- 列出当前已登录账户的所有订阅：

`az account list`

- 将某个 `subscription` 设置为当前活动的订阅：

`az account set {{[-s|--subscription]}} {{subscription_id}}`

- 列出当前活动订阅所支持的区域：

`az account list-locations`

- 打印一个可用于 `MS Graph API` 的访问令牌：

`az account get-access-token --resource-type {{ms-graph}}`

- 以指定格式打印当前活动订阅的详细信息：

`az account show {{[-o|--output]}} {{json|tsv|table|yaml}}`
