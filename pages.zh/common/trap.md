# trap

> 在接收到事件时执行命令。
> 可用于对用户中断或其他操作执行清理。
> 更多信息：<https://manned.org/trap.1posix>.

- 列出命令和预期事件的名称：

`trap`

- 在接收到信号时执行命令：

`trap 'echo "捕获到信号 {{SIGHUP}}"' {{HUP}}`

- 移除命令：

`trap - {{HUP}} {{INT}}`
