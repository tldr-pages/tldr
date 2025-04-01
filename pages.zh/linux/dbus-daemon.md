# dbus-daemon

> D-Bus 消息守护进程，允许多个程序交换消息。
> 更多信息：<https://www.freedesktop.org/wiki/Software/dbus/>.

- 使用配置文件运行守护进程：

`dbus-daemon --config-file {{path/to/file}}`

- 使用标准的每登录会话消息总线配置运行守护进程：

`dbus-daemon --session`

- 使用标准的系统级消息总线配置运行守护进程：

`dbus-daemon --system`

- 设置监听地址并覆盖配置文件中的值：

`dbus-daemon --address {{address}}`

- 将进程 ID 输出到 `stdout`：

`dbus-daemon --print-pid`

- 强制消息总线将消息写入系统日志：

`dbus-daemon --syslog`
