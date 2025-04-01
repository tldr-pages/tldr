# psgrep

> 使用 `grep` 搜索正在运行的进程。
> 更多信息：<https://jvz.github.io/psgrep>.

- 查找包含特定字符串的进程行：

`psgrep {{process_name}}`

- 查找包含特定字符串的进程行，不包括标题：

`psgrep -n {{process_name}}`

- 使用简化格式（PID、用户、命令）搜索：

`psgrep -s {{process_name}}`