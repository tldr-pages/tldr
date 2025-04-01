# timeout

> 带有时间限制地运行命令。
> 更多信息：<https://www.gnu.org/software/coreutils/manual/html_node/timeout-invocation.html>.

- 运行 `sleep 10` 并在 3 秒后终止它：

`timeout 3s sleep 10`

- 在超时时向命令发送信号（默认为 `TERM`，使用 `kill -l` 查看所有信号）：

`timeout {{[-s|--signal]}} {{INT|HUP|KILL|...}} {{5s}} {{sleep 10}}`

- 在超时后向 `stderr` 发送详细输出，显示发送的信号：

`timeout {{[-v|--verbose]}} {{0.5s|1m|1h|1d|...}} {{command}}`

- 无论是否超时，保留命令的退出状态：

`timeout {{[-p|--preserve-status]}} {{1s|1m|1h|1d|...}} {{command}}`

- 如果命令在初始信号后忽略超时，则在一定时间后发送强制的 `KILL` 信号：

`timeout {{[-k|--kill-after]}} {{5m}} {{30s}} {{command}}`
