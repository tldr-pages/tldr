# az webapp

> 管理托管在 Azure 云服务中的 Web 应用程序。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/webapp>.

- 列出 Web 应用程序可用的运行时：

`az webapp list-runtimes {{[-os|--os-type]}} {{windows|linux}}`

- 创建一个 Web 应用程序：

`az webapp up {{[-n|--name]}} {{name}} {{[-l|--location]}} {{location}} {{[-r|--runtime]}} {{runtime}}`

- 列出所有 Web 应用程序：

`az webapp list`

- 删除指定的 Web 应用程序：

`az webapp delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`
