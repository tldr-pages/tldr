# pgrep

> 通过名称查找或发送信号给进程。
> 更多信息：<https://www.manned.org/pgrep>.

- 返回带有匹配命令字符串的任何运行中进程的PID：

`pgrep {{process_name}}`

- 包括命令行选项查找进程：

`pgrep {{[-f|--full]}} "{{process_name}} {{parameter}}"`

- 查找由特定用户运行的进程：

`pgrep {{[-u|--euid]}} root {{process_name}}`