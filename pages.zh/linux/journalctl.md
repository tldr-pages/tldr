# journalctl

> 查询 systemd 日志。
> 更多信息：<https://manned.org/journalctl>.

- 显示自本次启动以来所有优先级为 3（错误）的消息：

`journalctl {{[-b|--boot]}} {{[-p|--priority]}} 3`

- 删除超过 2 天的日志：

`journalctl --vacuum-time 2d`

- 只显示最后 `n` 行并跟踪新消息（类似 `tail -f` 对于传统 syslog）：

`journalctl {{[-n|--lines]}} {{n}} {{[-f|--follow]}}`

- 显示特定单元的所有消息：

`journalctl {{[-u|--unit]}} {{unit}}`

- 显示从特定单元上次启动以来的日志：

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{unit}})`

- 在指定时间范围内的消息过滤（时间戳或类似“昨天”的占位符）：

`journalctl {{[-S|--since]}} {{now|today|yesterday|tomorrow}} {{[-U|--until]}} "{{YYYY-MM-DD HH:MM:SS}}"`

- 显示特定进程的所有消息：

`journalctl _PID={{pid}}`

- 显示特定可执行文件的所有消息：

`journalctl {{path/to/executable}}`