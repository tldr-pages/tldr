# kill

> 向进程发送信号，通常用于停止进程。
> 除 SIGKILL 和 SIGSTOP 外的所有信号都可以被进程捕获以执行干净的退出。
> 更多信息：<https://manned.org/kill>.

- 使用默认的 SIGTERM（终止）信号终止程序：

`kill {{process_id}}`

- 列出信号值及其对应的名称（使用时不带 `SIG` 前缀）。可用选项可能取决于 `kill` 的实现：

`kill {{-l|-L|--table}}`

- 终止后台作业：

`kill %{{job_id}}`

- 使用 SIGHUP（挂起）信号终止程序。许多守护进程会重新加载而不是终止：

`kill -{{1|HUP}} {{process_id}}`

- 使用 SIGINT（中断）信号终止程序。这通常由用户按下 `<Ctrl c>` 触发：

`kill -{{2|INT}} {{process_id}}`

- 向操作系统发送信号立即终止程序（程序没有机会捕获该信号）：

`kill -{{9|KILL}} {{process_id}}`

- 向操作系统发送信号暂停程序，直到接收到 SIGCONT（继续）信号：

`kill -{{17|STOP}} {{process_id}}`

- 向给定 GID（组 ID）的所有进程发送 `SIGUSR1` 信号：

`kill -{{SIGUSR1}} -{{group_id}}`
