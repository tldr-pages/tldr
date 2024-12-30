# pgrep

> 根据名称查找或信号进程。
> 更多信息：<https://www.manned.org/pgrep>。

- 返回任何运行的进程的PID，匹配命令字符串：

`pgrep {{process_name}}`

- 搜索包括其命令行选项的进程：

`pgrep --full "{{process_name}} {{parameter}}"`

- 搜索由特定用户运行的进程：

`pgrep --euid root {{process_name}}`