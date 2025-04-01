# abroot

> 通过在两个根分区状态之间进行事务切换（A⟺B）来提供完整的不可变性和原子性。
> 使用 OCI 镜像进行更新，以确保系统始终处于一致状态。
> 更多信息：<https://github.com/Vanilla-OS/ABRoot>.

- 将软件包添加到本地镜像（注意：执行此命令后，您需要应用这些更改）：

`sudo abroot pkg add {{package}}`

- 从本地镜像中删除软件包（注意：执行此命令后，您需要应用这些更改）：

`sudo abroot pkg remove {{package}}`

- 列出本地镜像中的软件包：

`sudo abroot pkg list`

- 应用本地镜像中的更改（注意：您需要重启系统以应用这些更改）：

`sudo abroot pkg apply`

- 将系统回滚到上一个状态：

`sudo abroot rollback`

- 编辑/查看内核参数：

`sudo abroot kargs {{edit|show}}`

- 显示状态：

`sudo abroot status`

- 显示帮助：

`abroot --help`