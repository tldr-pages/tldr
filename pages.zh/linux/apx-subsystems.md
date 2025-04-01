# apx subsystems

> 管理 `apx` 中的子系统。
> 子系统是基于预先存在的堆栈创建的容器。
> 更多信息：<https://docs.vanillaos.org/docs/en/apx-manpage#subsystems>。

- 交互式创建新的子系统：

`apx subsystems new`

- 列出所有可用的子系统：

`apx subsystems list`

- 将特定子系统重置为其初始状态：

`apx subsystems reset {{[-n|--name]}} {{string}}`

- 强制重置特定子系统：

`apx subsystems reset {{[-n|--name]}} {{string}} {{[-f|--force]}}`

- 删除特定子系统：

`apx subsystems rm {{[-n|--name]}} {{string}}`

- 强制删除特定子系统：

`apx subsystems rm {{[-n|--name]}} {{string}} {{[-f|--force]}}`