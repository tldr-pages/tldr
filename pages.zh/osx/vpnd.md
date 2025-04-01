# vpnd

> 监听传入的 VPN 连接。
> 不应手动调用。
> 更多信息：<https://keith.github.io/xcode-man-pages/vpnd.8.html>。

- 启动守护进程：

`vpnd`

- 在前台运行守护进程：

`vpnd -x`

- 在前台运行守护进程并将日志打印到终端：

`vpnd -d`

- 在前台运行守护进程，将日志打印到终端，并在验证参数后退出：

`vpnd -n`

- 为特定的服务器配置运行守护进程：

`vpnd -i {{server_id}}`

- 显示帮助：

`vpnd -h`
