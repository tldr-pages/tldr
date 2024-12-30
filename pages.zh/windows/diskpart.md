# diskpart

> 磁盘、卷和分区管理器。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>。

- 在管理员命令提示符下单独运行 diskpart 以进入其命令行：

`diskpart`

- 列出所有磁盘：

`list disk`

- 选择一个卷：

`select volume {{volume}}`

- 为选定的卷分配驱动器字母：

`assign letter {{letter}}`

- 创建一个新分区：

`create partition primary`

- 激活选定的卷：

`active`

- 退出 diskpart：

`exit`