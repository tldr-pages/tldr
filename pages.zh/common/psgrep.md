# psgrep

> 使用 `grep` 搜索正在运行的进程。
> 更多信息：<https://jvz.github.io/psgrep>。

- 查找包含特定字符串的进程行：

`psgrep {{process_name}}`

- 查找包含特定字符串的进程行，排除标题：

`psgrep -n {{process_name}}`

- 使用简化格式搜索（PID、用户、命令）：

`psgrep -s {{process_name}}`