# resolvconf

> 管理名称服务器信息。
> 充当提供名称服务器信息的程序与使用这些信息的应用程序之间的中介。
> 本页面记录了 Debian 对 `resolvconf` 的实现。
> 更多信息：<https://manned.org/resolvconf.8>。

- 添加或覆盖 IFACE.PROG 记录，并在启用更新的情况下运行更新脚本：

`resolvconf -a {{IFACE.PROG}}`

- 删除 IFACE.PROG 记录，并在启用更新的情况下运行更新脚本：

`resolvconf -d {{IFACE.PROG}}`

- 仅在启用更新的情况下运行更新脚本：

`resolvconf -u`

- 设置标志以指示在使用 `-a`、`-d` 或 `-u` 调用时是否应运行更新脚本：

`resolvconf --enable-updates`

- 清除标志以指示是否运行更新：

`resolvconf --disable-updates`

- 检查是否启用了更新：

`resolvconf --updates-are-enabled`