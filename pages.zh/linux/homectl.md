# homectl

> 使用 systemd-homed 服务创建、删除、更改或检查家目录。
> 更多信息：<https://manned.org/homectl>.

- 列出用户账户及其关联的家目录：

`homectl list`

- 创建用户账户及其关联的家目录：

`sudo homectl create {{username}}`

- 删除特定用户及其关联的家目录：

`sudo homectl remove {{username}}`

- 更改特定用户的密码：

`sudo homectl passwd {{username}}`

- 以特定家目录的访问权限运行 shell 或命令：

`sudo homectl with {{username}} -- {{command}} {{command_arguments}}`

- 锁定或解锁特定的家目录：

`sudo homectl {{lock|unlock}} {{username}}`

- 将特定家目录分配的磁盘空间更改为 100 GiB：

`sudo homectl resize {{username}} {{100G}}`

- 显示帮助：

`homectl --help`