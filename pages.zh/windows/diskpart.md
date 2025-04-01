# diskpart

> 磁盘、卷和分区管理工具。
> 更多信息：<https://learn.microsoft.com/windows-server/administration/windows-commands/diskpart>。

- 以管理员身份运行命令提示符，通过运行 diskpart 进入其命令行界面：

`diskpart`

- 列出所有磁盘：

`list disk`

- 选择一个卷：

`select volume {{volume}}`

- 为选定的卷分配一个驱动器字母：

`assign letter {{letter}}`

- 创建一个新的主分区：

`create partition primary`

- 激活选定的卷：

`active`

- 退出 diskpart：

`exit`