# ps

> 关于正在运行的进程的信息。
> 更多信息：<https://keith.github.io/xcode-man-pages/ps.1.html>。

- 列出所有正在运行的进程：

`ps aux`

- 列出所有正在运行的进程，包括完整的命令字符串：

`ps auxww`

- 搜索匹配某个字符串的进程：

`ps aux | grep {{string}}`

- 获取进程的父进程 ID：

`ps -o ppid= -p {{pid}}`

- 按内存使用量排序进程：

`ps -m`

- 按 CPU 使用量排序进程：

`ps -r`