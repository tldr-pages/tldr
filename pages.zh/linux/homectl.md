# homectl

> 使用 systemd-homed 服务创建、删除、修改或检查家目录。
> 更多信息：<https://manned.org/homectl>。

- 列出用户账户及其关联的家目录：

`homectl list`

- 创建一个用户账户及其关联的家目录：

`sudo homectl create {{用户名}}`

- 删除特定用户及其关联的家目录：

`sudo homectl remove {{用户名}}`

- 更改特定用户的密码：

`sudo homectl passwd {{用户名}}`

- 以特定家目录的访问权限运行 shell 或命令：

`sudo homectl with {{用户名}} -- {{命令}} {{命令参数}}`

- 锁定或解锁特定家目录：

`sudo homectl {{lock|unlock}} {{用户名}}`

- 将特定家目录分配的磁盘空间更改为 100 GiB：

`sudo homectl resize {{用户名}} {{100G}}`

- 显示帮助信息：

`homectl --help`