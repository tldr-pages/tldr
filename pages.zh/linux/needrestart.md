# needrestart

> 检查在库升级后需要重启的守护进程。
> 更多信息：<https://github.com/liske/needrestart>。

- 列出过时的进程：

`needrestart`

- 交互式重启服务：

`sudo needrestart`

- 以 [v]erbose 或 [q]uiet 模式列出过时的进程：

`needrestart -{{v|q}}`

- 检查 [k]ernel 是否过时：

`needrestart -k`

- 检查 CPU 微码是否过时：

`needrestart -w`

- 以 [b]atch 模式列出过时的进程：

`needrestart -b`

- 使用特定的 [c]onfiguration 文件列出过时的进程：

`needrestart -c {{path/to/config}}`

- 显示帮助：

`needrestart --help`