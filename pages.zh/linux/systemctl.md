# systemctl

> 控制 systemd 系统和服务管理器。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/systemctl.html>。

- 显示所有正在运行的服务：

`systemctl status`

- 列出失败的单元：

`systemctl --failed`

- 启动/停止/重启/重新加载/显示服务的状态：

`systemctl {{start|stop|restart|reload|status}} {{unit}}`

- 启用/禁用单元以便在启动时启动：

`systemctl {{enable|disable}} {{unit}}`

- 重新加载 systemd，扫描新的或更改的单元：

`systemctl daemon-reload`

- 检查单元是否处于活动/启用/失败状态：

`systemctl {{is-active|is-enabled|is-failed}} {{unit}}`

- 列出所有服务/套接字/自动挂载单元，并按运行/失败状态过滤：

`systemctl list-units --type={{service|socket|automount}} --state={{failed|running}}`

- 显示单元文件的内容和绝对路径：

`systemctl cat {{unit}}`