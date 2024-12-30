# killall

> 通过名称（必须是确切名称）向所有实例发送终止信号。
> 除了 SIGKILL 和 SIGSTOP 之外，所有信号都可以被进程拦截，从而允许干净退出。
> 更多信息：<https://manned.org/killall>.

- 使用默认的 SIGTERM（终止）信号终止进程：

`killall {{process_name}}`

- 列出可用的信号名称（不带 'SIG' 前缀）：

`killall --list`

- 在终止之前交互式请求确认：

`killall -i {{process_name}}`

- 使用 SIGINT（中断）信号终止进程，该信号与按 `Ctrl + C` 时发送的信号相同：

`killall -INT {{process_name}}`

- 强制终止进程：

`killall -KILL {{process_name}}`