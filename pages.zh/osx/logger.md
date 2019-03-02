# logger

> 向系统日志增加记录 (/var/log/syslog).

- 向系统日志增加记录:

`logger {{消息内容}}`

- 从stdin获取输入并记录到系统日志syslog:

`echo {{记录内容}} | logger`

- 将输出发送到在给定端口上运行的远程系统日志服务器.默认端口为514:

`echo {{记录内容}} | logger -h {{服务器名}} -P {{端口}}`

- 对记录的每一行使用特定的标签.默认值是登录用户的名:

`echo {{记录内容}} | logger -t {{标签}}`

- 以给定的错误等级记录消息. 默认是 `user.notice`. 使用 `man logger` 查询所有可选等级:

`echo {{记录内容}} | logger -p {{user.warning}}`
