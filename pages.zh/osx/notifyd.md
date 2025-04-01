# notifyd

> 通知服务器。
> 不应手动调用。
> 更多信息：<https://keith.github.io/xcode-man-pages/notifyd.8.html>.

- 启动守护进程：

`notifyd`

- 将调试信息记录到默认日志文件（`/var/log/notifyd.log`）：

`notifyd -d`

- 将调试信息记录到其他日志文件：

`notifyd -d -log_file {{path/to/log_file}}`