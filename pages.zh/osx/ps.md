# ps

> 关于运行中的进程的信息。
> 更多信息：<https://keith.github.io/xcode-man-pages/ps.1.html>。

- 列出所有运行中的进程：

`ps aux`

- 列出所有运行中的进程，包括完整的命令字符串：

`ps auxww`

- 搜索与字符串匹配的进程：

`ps aux | grep {{string}}`

- 获取进程的父进程ID：

`ps -o ppid= -p {{pid}}`

- 按内存使用情况排序进程：

`ps -m`

- 按CPU使用情况排序进程：

`ps -r`