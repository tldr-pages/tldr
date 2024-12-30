# py-spy

> Python 程序的采样分析器。
> 更多信息：<https://github.com/benfred/py-spy>。

- 显示正在运行的进程中占用最多执行时间的函数的实时视图：

`py-spy top --pid {{pid}}`

- 启动一个程序并显示占用最多执行时间的函数的实时视图：

`py-spy top -- python {{path/to/file.py}}`

- 生成函数调用执行时间的 SVG 火焰图：

`py-spy record -o {{path/to/profile.svg}} --pid {{pid}}`

- 转储正在运行进程的调用栈：

`py-spy dump --pid {{pid}}`