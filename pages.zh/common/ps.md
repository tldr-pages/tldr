# ps

> 运行进程的信息。
> 更多信息：<https://manned.org/ps>。

- 列出所有正在运行的进程：

`ps aux`

- 列出所有正在运行的进程，包括完整的命令字符串：

`ps auxww`

- 搜索匹配特定字符串的进程（方括号将防止 `grep` 匹配自身）：

`ps aux | grep {{[s]tring}}`

- 以额外完整格式列出当前用户的所有进程：

`ps --user $(id -u) -F`

- 以树形结构列出当前用户的所有进程：

`ps --user $(id -u) f`

- 获取进程的父进程PID：

`ps -o ppid= -p {{pid}}`

- 按内存消耗对进程进行排序：

`ps --sort size`