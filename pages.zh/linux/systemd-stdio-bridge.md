# systemd-stdio-bridge

> 实现 `stdin`/`stdout` 和 D-Bus 之间的代理。
> 注意：启动时期望通过 `stdin`/`stdout` 接收一个打开的连接，并将创建一个与指定总线的新连接。
> 更多信息：<https://www.freedesktop.org/software/systemd/man/latest/systemd-stdio-bridge.html>.

- 将 `stdin`/`stdout` 转发到本地系统总线：

`systemd-stdio-bridge`

- 将 `stdin`/`stdout` 转发到特定用户的 D-Bus：

`systemd-stdio-bridge --{{user}}`

- 将 `stdin`/`stdout` 转发到特定容器中的本地系统总线：

`systemd-stdio-bridge --machine={{mycontainer}}`

- 将 `stdin`/`stdout` 转发到自定义的 D-Bus 地址：

`systemd-stdio-bridge --bus-path=unix:path={{/custom/dbus/socket}}`