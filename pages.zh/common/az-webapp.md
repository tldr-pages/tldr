# az webapp

> 管理托管在 Azure 云服务中的 Web 应用程序。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/webapp>。

- 列出可用于 Web 应用程序的运行时：

`az webapp list-runtimes --os-type {{windows|linux}}`

- 创建一个 Web 应用程序：

`az webapp up --name {{name}} --location {{location}} --runtime {{runtime}}`

- 列出所有 Web 应用程序：

`az webapp list`

- 删除特定的 Web 应用程序：

`az webapp delete --name {{name}} --resource-group {{resource_group}}`