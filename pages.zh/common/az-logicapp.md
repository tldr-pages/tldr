# az logicapp

> 在 Azure 云服务中管理逻辑应用。
> 是 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/logicapp>.

- 创建一个逻辑应用：

`az logicapp create {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}} {{[-s|--storage-account]}} {{存储账户}}`

- 删除一个逻辑应用：

`az logicapp delete {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}}`

- 列出逻辑应用：

`az logicapp list {{[-g|--resource-group]}} {{资源组}}`

- 重启一个逻辑应用：

`az logicapp restart {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}}`

- 启动一个逻辑应用：

`az logicapp start {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}}`

- 停止一个逻辑应用：

`az logicapp stop {{[-n|--name]}} {{名称}} {{[-g|--resource-group]}} {{资源组}}`
