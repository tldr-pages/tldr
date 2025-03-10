# killall

> 根据进程名称向所有实例发送终止信号（必须是精确的进程名称）。
> 除了 SIGKILL 和 SIGSTOP，所有信号都可以被进程拦截，从而实现正常退出。
> 更多信息：<https://manned.org/killall>.

- 使用默认的 SIGTERM（终止）信号结束进程：

`killall {{进程名称}}`

- 列出可用的信号名称（使用时无需加 `SIG` 前缀）：

`killall -l`

- 交互式地询问确认后再终止进程：

`killall -i {{进程名称}}`

- 使用 SIGINT（中断）信号终止进程，与按下 `<Ctrl c>` 发送的信号相同：

`killall -INT {{进程名称}}`

- 强制杀死一个进程：

`killall -KILL {{进程名称}}`
