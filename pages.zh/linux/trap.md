# trap

> 在事件发生时执行命令。
> 更多信息：<https://www.gnu.org/software/bash/manual/bash.html#index-trap>.

- 列出可用的事件名称（例如 `SIGWINCH`）：

`trap -l`

- 列出预期事件的命令及其名称：

`trap`

- 当接收到信号时执行命令：

`trap 'echo "捕获信号 {{SIGHUP}}"' {{SIGHUP}}`

- 移除命令：

`trap - {{SIGHUP}} {{SIGINT}}`

- 忽略信号：

`trap '' {{SIGINT}}`
