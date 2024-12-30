# cupsctl

> 更新或查询服务器的 `cupsd.conf`。
> 更多信息：<https://openprinting.github.io/cups/doc/man-cupsctl.html>。

- 显示当前的配置值：

`cupsctl`

- 显示特定服务器的配置值：

`cupsctl -h {{server[:port]}}`

- 在与调度程序的连接中启用加密：

`cupsctl -E`

- 启用或禁用对 `error_log` 文件的调试日志记录：

`cupsctl {{--debug-logging|--no-debug-logging}}`

- 启用或禁用远程管理：

`cupsctl {{--remote-admin|--no-remote-admin}}`

- 解析当前的调试日志记录状态：

`cupsctl | grep '^_debug_logging' | awk -F= '{print $2}'`