# gops

> 列出并诊断当前在您的系统上运行的 Go 进程。
> 更多信息：<https://github.com/google/gops>。

- 打印本地运行的所有 Go 进程：

`gops`

- 打印关于某个进程的更多信息：

`gops {{pid}}`

- 显示进程树：

`gops tree`

- 打印目标程序的当前栈跟踪：

`gops stack {{pid|addr}}`

- 打印当前运行时内存统计信息：

`gops memstats {{pid|addr}}`