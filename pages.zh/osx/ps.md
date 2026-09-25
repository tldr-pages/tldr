# ps

> 正在运行的进程的信息。
> 更多信息：<https://keith.github.io/xcode-man-pages/ps.1.html>。

- 列出所有正在运行的进程：

`ps aux`

- 列出所有正在运行的进程，包括完整的命令字符串：

`ps auxww`

- 查找与字符串匹配的进程：

`ps aux | grep {{字符串}}`

- 获取一个进程的父进程 ID：

`ps -o ppid= -p {{进程id}}`

- 按内存使用量对进程进行排序：

`ps -m`

- 按 CPU 使用量对进程进行排序：

`ps -r`
