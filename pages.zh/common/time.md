# 时间

> 测量一个命令运行所花费的时间。
> 注意：`time` 可以作为一个 shell 内置命令、一个独立程序或两者兼而有之。
> 更多信息：<https://manned.org/time>。

- 运行 `command` 并将时间测量结果打印到 `stdout`：

`time {{command}}`

- 创建一个非常简单的秒表（仅在 Bash 中工作）：

`time read`