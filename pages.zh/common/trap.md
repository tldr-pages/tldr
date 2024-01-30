# trap

> 在进程或操作系统接收到信号后自动执行命令。
> 可用于对用户中断或其他操作执行清理。
> 更多信息：<https://manned.org/trap.1posix>.

- 列出设置 trap 的可用信号：

`trap -l`

- 列出当前 shell 程序的活动 trap 程序：

`trap -p`

- 设置 trap 以在检测到一个或多个信号时执行命令：

`trap 'echo "检测到信号 {{SIGHUP}}"' {{SIGHUP}}`

- 移除活动 trap：

`trap - {{SIGHUP}} {{SIGINT}}`
