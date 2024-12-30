# apx 子系统

> 管理 `apx` 中的子系统。
> 子系统是可以基于现有堆栈创建的容器。
> 更多信息：<https://github.com/Vanilla-OS/apx>。

- 交互式创建一个新子系统：

`apx subsystems new`

- 列出所有可用的子系统：

`apx subsystems list`

- 将特定子系统重置为初始状态：

`apx subsystems reset --name {{string}}`

- [f]orce 重置特定子系统：

`apx subsystems reset --name {{string}} --force`

- 移除特定子系统：

`apx subsystems rm --name {{string}}`

- [f]orce 移除特定子系统：

`apx subsystems rm --name {{string}} --force`