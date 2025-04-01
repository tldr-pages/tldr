# gops

> 列出并诊断系统中当前运行的 Go 进程。
> 更多信息：<https://github.com/google/gops>。

- 打印所有本地运行的 Go 进程：

`gops`

- 打印有关进程的更多信息：

`gops {{pid}}`

- 显示进程树：

`gops tree`

- 打印目标程序的当前堆栈跟踪：

`gops stack {{pid|addr}}`

- 打印当前的运行时内存统计信息：

`gops memstats {{pid|addr}}`
