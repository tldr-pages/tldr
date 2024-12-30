# top

> 显示有关正在运行的进程的动态实时信息。
> 更多信息：<https://keith.github.io/xcode-man-pages/top.1.html>。

- 启动 `top`，所有选项都可以在界面中使用：

`top`

- 启动 `top` 按内部内存大小排序进程（默认顺序 - 进程 ID）：

`top -o mem`

- 启动 `top` 首先按 CPU 排序进程，然后按运行时间排序：

`top -o cpu -O time`

- 启动 `top` 仅显示由指定用户拥有的进程：

`top -user {{user_name}}`

- 显示关于交互命令的帮助：

`?`