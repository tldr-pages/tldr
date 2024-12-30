# az 串行控制台

> 连接到虚拟机的串行控制台。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/serial-console>。

- 连接到串行控制台：

`az serial-console connect --resource-group {{资源组名称}} --name {{虚拟机名称}}`

- 终止连接：

`<Ctrl>-]`