# killall

> 通过名称向所有进程实例发送终止信号（名称必须完全匹配）。
> 除了 SIGKILL 和 SIGSTOP 之外，所有信号都可以被进程拦截，允许安全退出。
> 更多信息：<https://manned.org/killall>。

- 使用默认的 SIGTERM（终止）信号终止进程：

`killall {{process_name}}`

- [l]ist 可用的信号名称（无需 'SIG' 前缀）：

`killall -l`

- 在终止之前以交互方式请求确认：

`killall -i {{process_name}}`

- 使用 SIGINT（中断）信号终止进程，该信号与按 `Ctrl + C` 发送的信号相同：

`killall -INT {{process_name}}`

- 强制终止进程：

`killall -KILL {{process_name}}`