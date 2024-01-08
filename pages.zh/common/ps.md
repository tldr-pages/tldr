# ps

> 提供正在运行的进程的信息。
> 更多信息: <https://manned.org/ps>.

- 列出所有正在运行的进程：

`ps aux`

- 列出所有正在运行的进程，包括完整的命令字符串：

`ps auxww`

- 查找与字符串匹配的进程：

`ps aux | grep {{字符串}}`

- 以 extra full 格式列出当前用户的所有进程：

`ps --user $(id -u) -F`

- 以树形方式列出当前用户的所有进程：

`ps --user $(id -u) f`

- 获取一个进程的父进程 ID：

`ps -o ppid= -p {{进程 ID}}`

- 按内存使用量对进程进行排序：

`ps --sort size`
