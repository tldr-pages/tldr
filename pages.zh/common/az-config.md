# az config

> 管理 Azure CLI 配置。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/config>.

- 打印所有配置：

`az config get`

- 打印特定部分的配置：

`az config get {{部分名称}}`

- 设置一个配置：

`az config set {{配置名称}}={{值}}`

- 取消设置一个配置：

`az config unset {{配置名称}}`
