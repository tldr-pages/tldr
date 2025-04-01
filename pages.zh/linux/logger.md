# logger

> 将消息添加到系统日志（/var/log/syslog）。
> 更多信息：<https://manned.org/logger>。

- 将消息记录到系统日志：

`logger {{message}}`

- 从 `stdin` 接收输入并记录到系统日志：

`echo {{log_entry}} | logger`

- 将输出发送到指定端口上的远程系统日志服务器。默认端口是 514：

`echo {{log_entry}} | logger {{[-n|--server]}} {{hostname}} {{[-P|--port]}} {{port}}`

- 为每行记录使用特定的标签。默认是当前登录用户的名称：

`echo {{log_entry}} | logger {{[-t|--tag]}} {{tag}}`

- 使用指定的优先级记录消息。默认优先级是 `user.notice`。所有优先级选项参见 `man logger`：

`echo {{log_entry}} | logger {{[-p|--priority]}} {{user.warning}}`