# 超时

> 以时间限制运行命令。
> 更多信息：<https://www.gnu.org/software/coreutils/timeout>。

- 运行 `sleep 10` 并在 3 秒后终止它：

`timeout 3s sleep 10`

- 在时间限制到期后向命令发送一个 [信号]（默认是 `TERM`，使用 `kill -l` 列出所有信号）：

`timeout --signal {{INT|HUP|KILL|...}} {{5s}} {{sleep 10}}`

- 将 [详细] 输出发送到 `stderr`，显示超时后发送的信号：

`timeout --verbose {{0.5s|1m|1h|1d|...}} {{command}}`

- 无论超时与否，保留命令的退出状态：

`timeout --preserve-status {{1s|1m|1h|1d|...}} {{command}}`

- 如果命令在超时后忽略初始信号，则在一定时间后发送强制的 `KILL` 信号：

`timeout --kill-after={{5m}} {{30s}} {{command}}`