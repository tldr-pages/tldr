# kill

> 发送信号到一个进程，通常与停止进程相关。
> 除了 SIGKILL 和 SIGSTOP 之外，所有信号都可以被进程拦截以执行干净退出。
> 更多信息：<https://manned.org/kill.1posix>。

- 使用默认的 SIGTERM（终止）信号终止程序：

`kill {{process_id}}`

- 列出可用的信号名称（使用时不带 `SIG` 前缀）：

`kill -l`

- 使用 SIGHUP（挂起）信号终止程序。许多守护进程会重新加载而不是终止：

`kill -{{1|HUP}} {{process_id}}`

- 使用 SIGINT（中断）信号终止程序。这通常是由用户按 `Ctrl + C` 发起的：

`kill -{{2|INT}} {{process_id}}`

- 向操作系统发送信号以立即终止程序（该程序没有机会捕获信号）：

`kill -{{9|KILL}} {{process_id}}`

- 向操作系统发送信号以暂停程序，直到接收到 SIGCONT（"继续"）信号：

`kill -{{17|STOP}} {{process_id}}`

- 向所有具有给定 GID（组 ID）的进程发送 `SIGUSR1` 信号：

`kill -{{SIGUSR1}} -{{group_id}}`