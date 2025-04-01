# pkill

> 通过名称向进程发送信号。
> 主要用于停止进程。
> 更多信息：<https://www.manned.org/pkill>.

- 杀死所有匹配的进程：

`pkill "{{process_name}}"`

- 杀死所有命令行完全匹配的进程，而不仅仅是进程名称：

`pkill {{[-f|--full]}} "{{command_name}}"`

- 强制杀死匹配的进程（无法被阻塞）：

`pkill -9 "{{process_name}}"`

- 向匹配的进程发送 SIGUSR1 信号：

`pkill -USR1 "{{process_name}}"`

- 杀死最老的 `firefox` 进程以关闭浏览器：

`pkill {{[-o|--oldest]}} "{{firefox}}"`
