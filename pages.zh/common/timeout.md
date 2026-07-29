# timeout

> 在时间限制内运行命令。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html>。

- 运行 `sleep 10` 并在 3 秒后终止：

`timeout 3s sleep 10`

- 在时间限制到期后向命令发送信号（默认为 `TERM`，使用 `kill -l` 列出所有信号）：

`timeout {{[-s|--signal]}} {{INT|HUP|KILL|...}} {{5s}} {{sleep 10}}`

- 将详细输出发送到 `stderr`，显示超时后发送的信号：

`timeout {{[-v|--verbose]}} {{0.5s|1m|1h|1d|...}} {{命令}}`

- 无论是否超时，保留命令的退出状态：

`timeout {{[-p|--preserve-status]}} {{1s|1m|1h|1d|...}} {{命令}}`

- 如果命令在超时后忽略初始信号，则在指定时间后发送强制 `KILL` 信号：

`timeout {{[-k|--kill-after]}} {{5m}} {{30s}} {{命令}}`
