# az 锁

> 管理 Azure 锁。
> 属于 `azure-cli`（也称为 `az`）。
> 更多信息：<https://learn.microsoft.com/cli/azure/lock>。

- 创建一个只读的订阅级别锁：

`az lock create --name {{lock_name}} --lock-type ReadOnly`

- 创建一个只读的资源组级别锁：

`az lock create --name {{lock_name}} --resource-group {{group_name}} --lock-type ReadOnly`

- 删除一个订阅级别锁：

`az lock delete --name {{lock_name}}`

- 删除一个资源组级别锁：

`az lock delete --name {{lock_name}} --resource-group {{group_name}}`

- 列出所有订阅级别的锁：

`az lock list`

- 显示具有特定 [n]ame 的订阅级别锁：

`az lock show -n {{lock_name}}`