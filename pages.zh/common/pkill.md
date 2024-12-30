# pkill

> 按名称信号进程。
> 主要用于停止进程。
> 更多信息：<https://www.manned.org/pkill>。

- 杀死所有匹配的进程：

`pkill "{{process_name}}"`

- 杀死所有匹配完整命令的进程，而不仅仅是进程名称：

`pkill -f "{{command_name}}"`

- 强制杀死匹配的进程（无法被阻止）：

`pkill -9 "{{process_name}}"`

- 向匹配的进程发送 SIGUSR1 信号：

`pkill -USR1 "{{process_name}}"`

- 杀死主 `firefox` 进程以关闭浏览器：

`pkill --oldest "{{firefox}}"`