# az lock

> 管理 Azure 锁。
> 作为 `azure-cli`（也称为 `az`）的一部分。
> 更多信息：<https://learn.microsoft.com/cli/azure/lock>.

- 创建只读订阅级别锁：

`az lock create {{[-n|--name]}} {{lock_name}} {{[-t|--lock-type]}} ReadOnly`

- 创建只读资源组级别锁：

`az lock create {{[-n|--name]}} {{lock_name}} {{[-g|--resource-group]}} {{group_name}} {{[-t|--lock-type]}} ReadOnly`

- 删除订阅级别锁：

`az lock delete {{[-n|--name]}} {{lock_name}}`

- 删除资源组级别锁：

`az lock delete {{[-n|--name]}} {{lock_name}} {{[-g|--resource-group]}} {{group_name}}`

- 列出订阅级别的所有锁：

`az lock list`

- 显示具有特定 [n]ame 的订阅级别锁：

`az lock show {{[-n|--name]}} {{lock_name}}`