# kill

> 发送信号给一个进程，通常与停止进程相关。
> 除了 SIGKILL 和 SIGSTOP，所有信号都可以被进程拦截，以执行干净退出。
> 更多信息：<https://manned.org/kill>。

- 使用默认的 SIGTERM（终止）信号终止一个程序：

`kill {{process_id}}`

- 列出信号值及其对应的名称（可以不带 `SIG` 前缀使用）：

`kill -L`

- 终止一个后台作业：

`kill %{{job_id}}`

- 使用 SIGHUP（挂起）信号终止一个程序。许多守护进程会重新加载而不是终止：

`kill -{{1|HUP}} {{process_id}}`

- 使用 SIGINT（中断）信号终止一个程序。这通常是通过用户按 `Ctrl + C` 发起的：

`kill -{{2|INT}} {{process_id}}`

- 向操作系统发出信号，立即终止一个程序（该程序没有机会捕获信号）：

`kill -{{9|KILL}} {{process_id}}`

- 向操作系统发出信号，暂停一个程序，直到接收到 SIGCONT（“继续”）信号：

`kill -{{17|STOP}} {{process_id}}`

- 向所有具有给定 GID（组 ID）的进程发送 `SIGUSR1` 信号：

`kill -{{SIGUSR1}} -{{group_id}}`