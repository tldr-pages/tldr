# init

> Linux 运行级别管理器。
> 如果使用 systemd，要求启用 SYSVINIT 编译时选项。
> 更多信息：<https://manned.org/man/init.8>。

- 设置系统运行图形环境：

`sudo init 5`

- 设置系统运行多用户终端：

`sudo init 3`

- 关闭系统：

`init 0`

- 重启系统：

`init 6`

- 设置系统运行仅允许 root 用户且没有网络的终端：

`sudo init 1`