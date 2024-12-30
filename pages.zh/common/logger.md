# logger

> 将消息添加到syslog（/var/log/syslog）。
> 更多信息：<https://manned.org/logger>。

- 将消息记录到syslog：

`logger {{message}}`

- 从`stdin`获取输入并记录到syslog：

`echo {{log_entry}} | logger`

- 将输出发送到在给定端口上运行的远程syslog服务器。默认端口为514：

`echo {{log_entry}} | logger --server {{hostname}} --port {{port}}`

- 为每一行日志使用特定的标记。默认是登录用户的名称：

`echo {{log_entry}} | logger --tag {{tag}}`

- 以给定的优先级记录消息。默认是`user.notice`。有关所有优先级选项，请参见`man logger`：

`echo {{log_entry}} | logger --priority {{user.warning}}`