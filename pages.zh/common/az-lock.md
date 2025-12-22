# az lock

> 管理 Azure 锁。
> `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/lock>.

- 创建一个订阅级别的只读锁：

`az lock create {{[-n|--name]}} {{锁名称}} {{[-t|--lock-type]}} ReadOnly`

- 创建一个资源组级别的只读锁：

`az lock create {{[-n|--name]}} {{锁名称}} {{[-g|--resource-group]}} {{资源组名称}} {{[-t|--lock-type]}} ReadOnly`

- 删除一个订阅级别的锁：

`az lock delete {{[-n|--name]}} {{锁名称}}`

- 删除一个资源组级别的锁：

`az lock delete {{[-n|--name]}} {{锁名称}} {{[-g|--resource-group]}} {{资源组名称}}`

- 列出订阅级别的所有锁：

`az lock list`

- 显示具有特定名称的订阅级别锁：

`az lock show {{[-n|--name]}} {{锁名称}}`
