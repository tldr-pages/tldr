# journalctl

> 查询 systemd 日志。
> 更多信息：<https://manned.org/journalctl>。

- 显示本次 [b]oot 的所有优先级为 3（错误）的消息：

`journalctl -b --priority=3`

- 删除超过 2 天的日志：

`journalctl --vacuum-time=2d`

- 仅显示最后 N 行并 [f]ollow 新消息（类似于传统 syslog 的 `tail -f`）：

`journalctl --lines {{N}} --follow`

- 显示特定 [u]nit 的所有消息：

`journalctl --unit {{unit}}`

- 显示自上次启动以来的特定 unit 的日志：

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{unit}})`

- 在时间范围内过滤消息（可以是时间戳或诸如“昨天”的占位符）：

`journalctl --since {{now|today|yesterday|tomorrow}} --until "{{YYYY-MM-DD HH:MM:SS}}"`

- 显示特定进程的所有消息：

`journalctl _PID={{pid}}`

- 显示特定可执行文件的所有消息：

`journalctl {{path/to/executable}}`