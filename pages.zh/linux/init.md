# init

> Linux 运行级别管理器。
> 如果使用 systemd，则需要在编译时启用 SYSVINIT 选项。
> 更多信息：<https://manned.org/init.8>.

- 将系统设置为运行图形环境：

`sudo init 5`

- 将系统设置为运行多用户终端：

`sudo init 3`

- 关闭系统：

`init 0`

- 重启系统：

`init 6`

- 将系统设置为仅允许 root 用户且无网络的终端模式：

`sudo init 1`
